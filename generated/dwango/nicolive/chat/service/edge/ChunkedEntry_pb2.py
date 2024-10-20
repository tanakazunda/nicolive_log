# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dwango/nicolive/chat/service/edge/ChunkedEntry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from dwango.nicolive.chat.service.edge import MessageSegment_pb2 as dwango_dot_nicolive_dot_chat_dot_service_dot_edge_dot_MessageSegment__pb2
from dwango.nicolive.chat.service.edge import BackwardSegment_pb2 as dwango_dot_nicolive_dot_chat_dot_service_dot_edge_dot_BackwardSegment__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dwango/nicolive/chat/service/edge/ChunkedEntry.proto',
  package='dwango.nicolive.chat.service.edge',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n4dwango/nicolive/chat/service/edge/ChunkedEntry.proto\x12!dwango.nicolive.chat.service.edge\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x36\x64wango/nicolive/chat/service/edge/MessageSegment.proto\x1a\x37\x64wango/nicolive/chat/service/edge/BackwardSegment.proto\"\xd6\x02\n\x0c\x43hunkedEntry\x12\x44\n\x07segment\x18\x01 \x01(\x0b\x32\x31.dwango.nicolive.chat.service.edge.MessageSegmentH\x00\x12\x46\n\x08\x62\x61\x63kward\x18\x02 \x01(\x0b\x32\x32.dwango.nicolive.chat.service.edge.BackwardSegmentH\x00\x12\x45\n\x08previous\x18\x03 \x01(\x0b\x32\x31.dwango.nicolive.chat.service.edge.MessageSegmentH\x00\x12L\n\x04next\x18\x04 \x01(\x0b\x32<.dwango.nicolive.chat.service.edge.ChunkedEntry.ReadyForNextH\x00\x1a\x1a\n\x0cReadyForNext\x12\n\n\x02\x61t\x18\x01 \x01(\x03\x42\x07\n\x05\x65ntryb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,dwango_dot_nicolive_dot_chat_dot_service_dot_edge_dot_MessageSegment__pb2.DESCRIPTOR,dwango_dot_nicolive_dot_chat_dot_service_dot_edge_dot_BackwardSegment__pb2.DESCRIPTOR,])




_CHUNKEDENTRY_READYFORNEXT = _descriptor.Descriptor(
  name='ReadyForNext',
  full_name='dwango.nicolive.chat.service.edge.ChunkedEntry.ReadyForNext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='at', full_name='dwango.nicolive.chat.service.edge.ChunkedEntry.ReadyForNext.at', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=545,
  serialized_end=571,
)

_CHUNKEDENTRY = _descriptor.Descriptor(
  name='ChunkedEntry',
  full_name='dwango.nicolive.chat.service.edge.ChunkedEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='segment', full_name='dwango.nicolive.chat.service.edge.ChunkedEntry.segment', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backward', full_name='dwango.nicolive.chat.service.edge.ChunkedEntry.backward', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='previous', full_name='dwango.nicolive.chat.service.edge.ChunkedEntry.previous', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next', full_name='dwango.nicolive.chat.service.edge.ChunkedEntry.next', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CHUNKEDENTRY_READYFORNEXT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='entry', full_name='dwango.nicolive.chat.service.edge.ChunkedEntry.entry',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=238,
  serialized_end=580,
)

_CHUNKEDENTRY_READYFORNEXT.containing_type = _CHUNKEDENTRY
_CHUNKEDENTRY.fields_by_name['segment'].message_type = dwango_dot_nicolive_dot_chat_dot_service_dot_edge_dot_MessageSegment__pb2._MESSAGESEGMENT
_CHUNKEDENTRY.fields_by_name['backward'].message_type = dwango_dot_nicolive_dot_chat_dot_service_dot_edge_dot_BackwardSegment__pb2._BACKWARDSEGMENT
_CHUNKEDENTRY.fields_by_name['previous'].message_type = dwango_dot_nicolive_dot_chat_dot_service_dot_edge_dot_MessageSegment__pb2._MESSAGESEGMENT
_CHUNKEDENTRY.fields_by_name['next'].message_type = _CHUNKEDENTRY_READYFORNEXT
_CHUNKEDENTRY.oneofs_by_name['entry'].fields.append(
  _CHUNKEDENTRY.fields_by_name['segment'])
_CHUNKEDENTRY.fields_by_name['segment'].containing_oneof = _CHUNKEDENTRY.oneofs_by_name['entry']
_CHUNKEDENTRY.oneofs_by_name['entry'].fields.append(
  _CHUNKEDENTRY.fields_by_name['backward'])
_CHUNKEDENTRY.fields_by_name['backward'].containing_oneof = _CHUNKEDENTRY.oneofs_by_name['entry']
_CHUNKEDENTRY.oneofs_by_name['entry'].fields.append(
  _CHUNKEDENTRY.fields_by_name['previous'])
_CHUNKEDENTRY.fields_by_name['previous'].containing_oneof = _CHUNKEDENTRY.oneofs_by_name['entry']
_CHUNKEDENTRY.oneofs_by_name['entry'].fields.append(
  _CHUNKEDENTRY.fields_by_name['next'])
_CHUNKEDENTRY.fields_by_name['next'].containing_oneof = _CHUNKEDENTRY.oneofs_by_name['entry']
DESCRIPTOR.message_types_by_name['ChunkedEntry'] = _CHUNKEDENTRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChunkedEntry = _reflection.GeneratedProtocolMessageType('ChunkedEntry', (_message.Message,), dict(

  ReadyForNext = _reflection.GeneratedProtocolMessageType('ReadyForNext', (_message.Message,), dict(
    DESCRIPTOR = _CHUNKEDENTRY_READYFORNEXT,
    __module__ = 'dwango.nicolive.chat.service.edge.ChunkedEntry_pb2'
    # @@protoc_insertion_point(class_scope:dwango.nicolive.chat.service.edge.ChunkedEntry.ReadyForNext)
    ))
  ,
  DESCRIPTOR = _CHUNKEDENTRY,
  __module__ = 'dwango.nicolive.chat.service.edge.ChunkedEntry_pb2'
  # @@protoc_insertion_point(class_scope:dwango.nicolive.chat.service.edge.ChunkedEntry)
  ))
_sym_db.RegisterMessage(ChunkedEntry)
_sym_db.RegisterMessage(ChunkedEntry.ReadyForNext)


# @@protoc_insertion_point(module_scope)
