# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dwango/nicolive/chat/data/OperatorComment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dwango.nicolive.chat.data import Chat_pb2 as dwango_dot_nicolive_dot_chat_dot_data_dot_Chat__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dwango/nicolive/chat/data/OperatorComment.proto',
  package='dwango.nicolive.chat.data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n/dwango/nicolive/chat/data/OperatorComment.proto\x12\x19\x64wango.nicolive.chat.data\x1a$dwango/nicolive/chat/data/Chat.proto\"z\n\x0fOperatorComment\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12:\n\x08modifier\x18\x03 \x01(\x0b\x32(.dwango.nicolive.chat.data.Chat.Modifier\x12\x0c\n\x04link\x18\x04 \x01(\tb\x06proto3')
  ,
  dependencies=[dwango_dot_nicolive_dot_chat_dot_data_dot_Chat__pb2.DESCRIPTOR,])




_OPERATORCOMMENT = _descriptor.Descriptor(
  name='OperatorComment',
  full_name='dwango.nicolive.chat.data.OperatorComment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='dwango.nicolive.chat.data.OperatorComment.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dwango.nicolive.chat.data.OperatorComment.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modifier', full_name='dwango.nicolive.chat.data.OperatorComment.modifier', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link', full_name='dwango.nicolive.chat.data.OperatorComment.link', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=116,
  serialized_end=238,
)

_OPERATORCOMMENT.fields_by_name['modifier'].message_type = dwango_dot_nicolive_dot_chat_dot_data_dot_Chat__pb2._CHAT_MODIFIER
DESCRIPTOR.message_types_by_name['OperatorComment'] = _OPERATORCOMMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OperatorComment = _reflection.GeneratedProtocolMessageType('OperatorComment', (_message.Message,), dict(
  DESCRIPTOR = _OPERATORCOMMENT,
  __module__ = 'dwango.nicolive.chat.data.OperatorComment_pb2'
  # @@protoc_insertion_point(class_scope:dwango.nicolive.chat.data.OperatorComment)
  ))
_sym_db.RegisterMessage(OperatorComment)


# @@protoc_insertion_point(module_scope)
