# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dwango/nicolive/chat/data/SimpleNotification.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dwango/nicolive/chat/data/SimpleNotification.proto',
  package='dwango.nicolive.chat.data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n2dwango/nicolive/chat/data/SimpleNotification.proto\x12\x19\x64wango.nicolive.chat.data\x1a\x1egoogle/protobuf/duration.proto\"\xc7\x01\n\x12SimpleNotification\x12\x10\n\x06ichiba\x18\x01 \x01(\tH\x00\x12\x0f\n\x05quote\x18\x02 \x01(\tH\x00\x12\x11\n\x07\x65motion\x18\x03 \x01(\tH\x00\x12\x10\n\x06\x63ruise\x18\x04 \x01(\tH\x00\x12\x1a\n\x10program_extended\x18\x05 \x01(\tH\x00\x12\x14\n\nranking_in\x18\x06 \x01(\tH\x00\x12\x19\n\x0franking_updated\x18\x08 \x01(\tH\x00\x12\x11\n\x07visited\x18\x07 \x01(\tH\x00\x42\t\n\x07messageb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])




_SIMPLENOTIFICATION = _descriptor.Descriptor(
  name='SimpleNotification',
  full_name='dwango.nicolive.chat.data.SimpleNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ichiba', full_name='dwango.nicolive.chat.data.SimpleNotification.ichiba', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quote', full_name='dwango.nicolive.chat.data.SimpleNotification.quote', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emotion', full_name='dwango.nicolive.chat.data.SimpleNotification.emotion', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cruise', full_name='dwango.nicolive.chat.data.SimpleNotification.cruise', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='program_extended', full_name='dwango.nicolive.chat.data.SimpleNotification.program_extended', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ranking_in', full_name='dwango.nicolive.chat.data.SimpleNotification.ranking_in', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ranking_updated', full_name='dwango.nicolive.chat.data.SimpleNotification.ranking_updated', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visited', full_name='dwango.nicolive.chat.data.SimpleNotification.visited', index=7,
      number=7, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='message', full_name='dwango.nicolive.chat.data.SimpleNotification.message',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=114,
  serialized_end=313,
)

_SIMPLENOTIFICATION.oneofs_by_name['message'].fields.append(
  _SIMPLENOTIFICATION.fields_by_name['ichiba'])
_SIMPLENOTIFICATION.fields_by_name['ichiba'].containing_oneof = _SIMPLENOTIFICATION.oneofs_by_name['message']
_SIMPLENOTIFICATION.oneofs_by_name['message'].fields.append(
  _SIMPLENOTIFICATION.fields_by_name['quote'])
_SIMPLENOTIFICATION.fields_by_name['quote'].containing_oneof = _SIMPLENOTIFICATION.oneofs_by_name['message']
_SIMPLENOTIFICATION.oneofs_by_name['message'].fields.append(
  _SIMPLENOTIFICATION.fields_by_name['emotion'])
_SIMPLENOTIFICATION.fields_by_name['emotion'].containing_oneof = _SIMPLENOTIFICATION.oneofs_by_name['message']
_SIMPLENOTIFICATION.oneofs_by_name['message'].fields.append(
  _SIMPLENOTIFICATION.fields_by_name['cruise'])
_SIMPLENOTIFICATION.fields_by_name['cruise'].containing_oneof = _SIMPLENOTIFICATION.oneofs_by_name['message']
_SIMPLENOTIFICATION.oneofs_by_name['message'].fields.append(
  _SIMPLENOTIFICATION.fields_by_name['program_extended'])
_SIMPLENOTIFICATION.fields_by_name['program_extended'].containing_oneof = _SIMPLENOTIFICATION.oneofs_by_name['message']
_SIMPLENOTIFICATION.oneofs_by_name['message'].fields.append(
  _SIMPLENOTIFICATION.fields_by_name['ranking_in'])
_SIMPLENOTIFICATION.fields_by_name['ranking_in'].containing_oneof = _SIMPLENOTIFICATION.oneofs_by_name['message']
_SIMPLENOTIFICATION.oneofs_by_name['message'].fields.append(
  _SIMPLENOTIFICATION.fields_by_name['ranking_updated'])
_SIMPLENOTIFICATION.fields_by_name['ranking_updated'].containing_oneof = _SIMPLENOTIFICATION.oneofs_by_name['message']
_SIMPLENOTIFICATION.oneofs_by_name['message'].fields.append(
  _SIMPLENOTIFICATION.fields_by_name['visited'])
_SIMPLENOTIFICATION.fields_by_name['visited'].containing_oneof = _SIMPLENOTIFICATION.oneofs_by_name['message']
DESCRIPTOR.message_types_by_name['SimpleNotification'] = _SIMPLENOTIFICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleNotification = _reflection.GeneratedProtocolMessageType('SimpleNotification', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLENOTIFICATION,
  __module__ = 'dwango.nicolive.chat.data.SimpleNotification_pb2'
  # @@protoc_insertion_point(class_scope:dwango.nicolive.chat.data.SimpleNotification)
  ))
_sym_db.RegisterMessage(SimpleNotification)


# @@protoc_insertion_point(module_scope)
