import requests
import json
import asyncio
import websockets
import aiohttp
from bs4 import BeautifulSoup
from pathlib import Path
import sys

# generatedフォルダをPythonのモジュールパスに追加
sys.path.append(str(Path(__file__).parent / "generated"))
from generated.dwango.nicolive.chat.service.edge import ChunkedEntry_pb2, ChunkedMessage_pb2

# ChunkReaderクラスを定義
class ChunkReader:
    """
    バッファを初期化します。
    
    :param buffer: チャンクを含む入力バッファ
    """
    def __init__(self, buffer):
        self.buffer = buffer

    def read(self):
        """
        バッファからチャンクを読み取り、返します。
        
        このメソッドはバリエーション整数（varint）値をバッファからデコードし、
        それらに基づいてチャンクを生成し返します。
        
        :yield: バッファから読み取ったチャンク
        """
        t = 0
        while True:
            varint_data = self.decode_varint(self.buffer, t)
            if varint_data is None:
                break

            value, offset = varint_data['value'], varint_data['offset']
            o = offset + 1
            r = o + value

            if len(self.buffer) < r:
                break

            t = r
            chunk = self.buffer[o:t]
            yield chunk

        if t:
            self.buffer = self.buffer[t:]

    def decode_varint(self, buffer, t):
        """
        指定された位置tから始めて、バッファからバリエーション整数（varint）をデコードします。
        
        このメソッドはバッファからバイトを読み取り、それらを整数として解釈します。
        
        :param buffer: 入力バッファ
        :param t: バッファ内の開始位置
        :return: デコードされた値と新しいオフセットを含む辞書
        """
        n = 0
        o = len(buffer)
        i = 0

        while True:
            if o <= t:
                return None

            a = buffer[t]
            r = bool(128 & a)
            n |= (127 & a) << i

            if not r:
                break

            t += 1
            i += 7

        return {'value': n, 'offset': t}

class SegmentServerClient:
    def __init__(self, uri):
        self.uri = uri
        self.active = True

    async def start_receiving(self):
        headers = {
            "header": "u=1, i"
        }
        print(f"セグメントサーバー: {self.uri} に接続します。")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.uri, headers=headers) as response:
                    if response.status == 200:
                        buffer = b""
                        async for chunk in response.content.iter_chunked(1024):
                            # バッファに追加して、ChunkReaderに渡してチャンク処理
                            buffer += chunk
                            self.try_read_chunks(buffer)  # チャンクの読み取りを試行
                    else:
                        print(f"HTTPエラー: {response.status}")
        except aiohttp.ClientError as e:
            print(f"接続エラー: {e}")
        except asyncio.CancelledError:
            # タスクがキャンセルされた場合の処理
            print("タスクがキャンセルされました")

    def try_read_chunks(self, buffer):
        # ChunkReaderを使ってチャンクを処理
        chunk_reader = ChunkReader(buffer)
        for chunk in chunk_reader.read():
            self.process_chunk(chunk)

    def process_chunk(self, chunk):
        # チャンクのデータを処理する
        chunked_message = ChunkedMessage_pb2.ChunkedMessage()
        try:
            chunked_message.ParseFromString(chunk)
        except Exception as e:
            print(f"メッセージの解析に失敗しました: {e}")
            return

        output_message = []

        # chatメッセージの情報
        if chunked_message.message.HasField("chat"):
            chat_content = chunked_message.message.chat.content
            if isinstance(chat_content, bytes):
                try:
                    chat_content_decoded = chat_content.decode('utf-8')
                except UnicodeDecodeError:
                    chat_content_decoded = chat_content
            else:
                chat_content_decoded = chat_content

            output_message.append(f"message.chat.content: {chat_content_decoded}")
            output_message.append(f"message.chat.vpos: {chunked_message.message.chat.vpos}")
            output_message.append(f"message.chat.hashed_user_id: {chunked_message.message.chat.hashed_user_id}")
            output_message.append(f"message.chat.no: {chunked_message.message.chat.no}")

            # 整形して出力
            formatted_output = "\n".join(output_message)
            print("セグメントサーバーから受信したメッセージ:\n", formatted_output)

class MessageServerClient:
    def __init__(self, uri, is_message_server=True):
        self.uri = uri
        self.is_message_server = is_message_server
        self.next_stream_at = "now" if is_message_server else None
        self.active = True  # タスクがアクティブかどうかのフラグ

    async def start_receiving(self):
        headers = {
            "header": "u=1, i"
        }
        message_server_url = f"{self.uri}?at={self.next_stream_at}" if self.next_stream_at else self.uri
        print(f"メッセージサーバー: {message_server_url} に接続します。")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(message_server_url, headers=headers) as response:
                    if response.status == 200:
                        buffer = b""
                        async for chunk in response.content.iter_chunked(1024):
                            buffer += chunk
                            chunk_reader = ChunkReader(buffer)      
                            for chunk in chunk_reader.read():
                                if self.is_message_server:
                                    # ChunkedEntryのprotobuf解析を実行
                                    chunked_entry = ChunkedEntry_pb2.ChunkedEntry()
                                    chunked_entry.ParseFromString(chunk)
                                    # Nextイベントの処理
                                    if chunked_entry.HasField("next"):
                                        self.next_stream_at = chunked_entry.next.at
                                        print(f"次の配信時刻を更新: {self.next_stream_at}")
                                        # 次の接続を自動的に再開
                                        await self.reconnect()
                                        break

                                    # Segmentイベントの処理
                                    if chunked_entry.HasField("segment"):
                                        segment_uri = chunked_entry.segment.uri
                                        # SegmentServerClientを利用する
                                        segment_server_client = SegmentServerClient(segment_uri)
                                        await segment_server_client.start_receiving()
                    else:
                        print(f"HTTPエラー: {response.status}")
        except aiohttp.ClientError as e:
            print(f"接続エラー: {e}")
            # 異常が発生した場合は再接続を試みる
            await self.reconnect()
        except asyncio.CancelledError:
            # タスクがキャンセルされた場合の処理
            print("タスクがキャンセルされました")

    async def reconnect(self):
        # 自動的に次の接続を再開する処理を実装
        if self.next_stream_at:
            await self.start_receiving()

    def disconnect(self):
        # 現在の接続を切断する処理を実装
        self.active = False
        print("接続を切断しました。")
        # 必要に応じて他のリソースの解放処理を実装

def login(email, password):
    """
    ニコニコ動画のログインを行う関数
    
    Args:
        email (str): ニコニコ動画のメールアドレス
        password (str): ニコニコ動画のパスワード
        
    Returns:
        requests.Session: ログイン後のセッションオブジェクト
    Raises:
        requests.RequestException: ログインに失敗した場合
    """

    # ニコニコ動画のログインURL
    login_url = "https://account.nicovideo.jp/login/redirector"

    # セッションの作成
    session = requests.Session()

    # ログイン用のデータを作成
    login_data = {
        "mail": email,
        "password": password
    }
    
    try:
        # ログインリクエストを送信
        response = session.post(login_url, data=login_data, allow_redirects=False)

        # ログイン成功の確認
        if response.status_code == 302 and 'set-cookie' in response.headers:
            print("ログイン成功")
            return session
        else:
            print(f"ログイン失敗: ステータスコード {response.status_code}")
            raise requests.RequestException("ログインに失敗しました")
    except requests.RequestException as e:
        print(f"エラーが発生しました: {e}")
        raise

def get_page_info(url, session=None):
    """
    指定されたURLからページ情報を取得する
    
    Args:
        url (str): 取得したいページのURL
        session (requests.Session, optional): セッションオブジェクト。省略時は新しく作成します。
    
    Returns:
        tuple: web_socket_url, message_server_url
    """
    # ページのHTMLを取得
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.49 Safari/537.36",
    }
    if session is None:
        session = requests.Session()
    
    response = session.get(url, headers=headers)

    if response.status_code == 200:
        page_source = response.text
        # BeautifulSoupを使ってHTMLをパース
        soup = BeautifulSoup(page_source, "html.parser")

        # embedded-dataの要素を取得
        embedded_data_element = soup.find(id="embedded-data")
        if embedded_data_element and 'data-props' in embedded_data_element.attrs:
            data_props_json_str = embedded_data_element['data-props']
            try:
                # JSONとしてパース
                data_props = json.loads(data_props_json_str)
                # webSocketUrlを取得
                web_socket_url = data_props.get("site", {}).get("relive", {}).get("webSocketUrl")
                if web_socket_url:
                    print("webSocketUrl:", web_socket_url)
                    return web_socket_url
                else:
                    print("webSocketUrlが見つかりませんでした。")
                    return None
            except json.JSONDecodeError as e:
                print(f"data-propsの内容がJSONとして正しくパースできませんでした: {e}")
                return None
        else:
            print("embedded-dataの要素またはdata-props属性が見つかりませんでした。")
    else:
        print(f"HTTPリクエストが失敗しました。ステータスコード: {response.status_code}")

# keepSeat メッセージを送信する関数
async def send_keep_seat(websocket, interval):
    try:
        while True:
            await asyncio.sleep(interval)
            await websocket.send(json.dumps({"type": "keepSeat"}))
            print("keepSeat メッセージを送信しました。")
    except websockets.exceptions.ConnectionClosed:
        print("WebSocket 接続が閉じられたため、keepSeat メッセージの送信を停止します。")

async def connect_to_websocket():
    try:
        async with websockets.connect(web_socket_url) as websocket:
            # ウェルカムメッセージの作成
            welcome_message = {
                "type": "startWatching",
                "data": {
                    "stream": {
                        "quality": "abr",  # 以前の指摘に基づき「abr」を使用
                        "protocol": "hls",
                        "latency": "high",
                        "chasePlay": False
                    },
                    "room": {
                        "protocol": "webSocket",
                        "commentable": True
                    },
                    "reconnect": False
                }
            }
            # ウェルカムメッセージを JSON 形式で送信
            await websocket.send(json.dumps(welcome_message))
            print("ウェルカムメッセージを送信しました。")

            keep_interval = None
            http_receiver = None
            # サーバーからの応答を継続的に受信
            while True:
                response = await websocket.recv()
                data = json.loads(response)
                # print("受信したメッセージ:", json.dumps(data, indent=2, ensure_ascii=False))

                # keepSeat イベントの処理
                if data.get("type") == "seat":
                    keep_interval = data.get("data", {}).get("keepIntervalSec", 30)
                    print(f"keepSeat イベントを受信しました。{keep_interval}秒ごとに keepSeat を送信します。")

                    # keepSeat メッセージの送信タスクを作成
                    asyncio.create_task(send_keep_seat(websocket, keep_interval))

                # ping イベントの処理
                if data.get("type") == "ping":
                    await websocket.send(json.dumps({"type": "pong"}))
                    print("pong メッセージを送信しました。")

                # disconnect イベントの処理
                if data.get("type") == "disconnect":
                    reason = data.get("data", {}).get("reason")
                    if reason == "END_PROGRAM":
                        print("配信が終了しました。WebSocket 接続を閉じます。")
                        break
                    else:
                        print(f"WebSocket 接続に異常があります: {reason}")
                        break

                # error イベントの処理
                if data.get("type") == "error":
                    code = data.get("body", {}).get("code")
                    if code == "CONNECT_ERROR":
                        print("配信が終了したWebSocket URLに接続しようとしました。接続を終了します。")
                    elif code == "INVALID_MESSAGE":
                        print("クライアントが異常なメッセージを送信しました。接続を終了します。")
                    else:
                        print(f"エラーが発生しました: {code}")
                    break

                # messageServer イベントの処理
                if data.get("type") == "messageServer":
                    message_server_url = data.get("data", {}).get("viewUri")
                    if message_server_url:
                        print(f"新しいメッセージサーバーURLを受信しました: {message_server_url}。接続を切り替えます。")
                        if http_receiver is not None:
                            # 古い接続があればキャンセルする
                            http_receiver.cancel()
                         # 新しい接続を作成して実行
                        http_receiver = asyncio.create_task(MessageServerClient(uri=message_server_url, is_message_server=True).start_receiving())

    except websockets.exceptions.ConnectionClosed as e:
        print(f"接続が閉じられました: {e}")

    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    email = "XXX"
    password = "XXX"
    # 対象のURL　例：https://live.nicovideo.jp/watch/lvxxxxxxx
    url = ""
    try:
        # session = login(email, password)
        web_socket_url = get_page_info(url)
        if web_socket_url:
            asyncio.run(connect_to_websocket())
        else:
            print("webSocketUrlが見つかりませんでした。")
    except requests.RequestException as e:
        print(f"ログインに失敗しました: {e}")