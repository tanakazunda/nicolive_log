# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dwango/nicolive/chat/data/Marque.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from dwango.nicolive.chat.data import OperatorComment_pb2 as dwango_dot_nicolive_dot_chat_dot_data_dot_OperatorComment__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dwango/nicolive/chat/data/Marque.proto',
  package='dwango.nicolive.chat.data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&dwango/nicolive/chat/data/Marque.proto\x12\x19\x64wango.nicolive.chat.data\x1a\x1egoogle/protobuf/duration.proto\x1a/dwango/nicolive/chat/data/OperatorComment.proto\"\xc2\x01\n\x06Marque\x12:\n\x07\x64isplay\x18\x01 \x01(\x0b\x32).dwango.nicolive.chat.data.Marque.Display\x1a|\n\x07\x44isplay\x12\x44\n\x10operator_comment\x18\x01 \x01(\x0b\x32*.dwango.nicolive.chat.data.OperatorComment\x12+\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Durationb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,dwango_dot_nicolive_dot_chat_dot_data_dot_OperatorComment__pb2.DESCRIPTOR,])




_MARQUE_DISPLAY = _descriptor.Descriptor(
  name='Display',
  full_name='dwango.nicolive.chat.data.Marque.Display',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operator_comment', full_name='dwango.nicolive.chat.data.Marque.Display.operator_comment', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='dwango.nicolive.chat.data.Marque.Display.duration', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=221,
  serialized_end=345,
)

_MARQUE = _descriptor.Descriptor(
  name='Marque',
  full_name='dwango.nicolive.chat.data.Marque',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='display', full_name='dwango.nicolive.chat.data.Marque.display', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MARQUE_DISPLAY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=345,
)

_MARQUE_DISPLAY.fields_by_name['operator_comment'].message_type = dwango_dot_nicolive_dot_chat_dot_data_dot_OperatorComment__pb2._OPERATORCOMMENT
_MARQUE_DISPLAY.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_MARQUE_DISPLAY.containing_type = _MARQUE
_MARQUE.fields_by_name['display'].message_type = _MARQUE_DISPLAY
DESCRIPTOR.message_types_by_name['Marque'] = _MARQUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Marque = _reflection.GeneratedProtocolMessageType('Marque', (_message.Message,), dict(

  Display = _reflection.GeneratedProtocolMessageType('Display', (_message.Message,), dict(
    DESCRIPTOR = _MARQUE_DISPLAY,
    __module__ = 'dwango.nicolive.chat.data.Marque_pb2'
    # @@protoc_insertion_point(class_scope:dwango.nicolive.chat.data.Marque.Display)
    ))
  ,
  DESCRIPTOR = _MARQUE,
  __module__ = 'dwango.nicolive.chat.data.Marque_pb2'
  # @@protoc_insertion_point(class_scope:dwango.nicolive.chat.data.Marque)
  ))
_sym_db.RegisterMessage(Marque)
_sym_db.RegisterMessage(Marque.Display)


# @@protoc_insertion_point(module_scope)
