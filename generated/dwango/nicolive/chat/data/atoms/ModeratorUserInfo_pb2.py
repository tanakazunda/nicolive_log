# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dwango/nicolive/chat/data/atoms/ModeratorUserInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dwango/nicolive/chat/data/atoms/ModeratorUserInfo.proto',
  package='dwango.nicolive.chat.data.atoms',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n7dwango/nicolive/chat/data/atoms/ModeratorUserInfo.proto\x12\x1f\x64wango.nicolive.chat.data.atoms\"G\n\x11ModeratorUserInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\x0f\n\x07iconUrl\x18\x04 \x01(\tb\x06proto3')
)




_MODERATORUSERINFO = _descriptor.Descriptor(
  name='ModeratorUserInfo',
  full_name='dwango.nicolive.chat.data.atoms.ModeratorUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='dwango.nicolive.chat.data.atoms.ModeratorUserInfo.user_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='dwango.nicolive.chat.data.atoms.ModeratorUserInfo.nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iconUrl', full_name='dwango.nicolive.chat.data.atoms.ModeratorUserInfo.iconUrl', index=2,
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
  serialized_start=92,
  serialized_end=163,
)

DESCRIPTOR.message_types_by_name['ModeratorUserInfo'] = _MODERATORUSERINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModeratorUserInfo = _reflection.GeneratedProtocolMessageType('ModeratorUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _MODERATORUSERINFO,
  __module__ = 'dwango.nicolive.chat.data.atoms.ModeratorUserInfo_pb2'
  # @@protoc_insertion_point(class_scope:dwango.nicolive.chat.data.atoms.ModeratorUserInfo)
  ))
_sym_db.RegisterMessage(ModeratorUserInfo)


# @@protoc_insertion_point(module_scope)
