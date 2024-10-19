# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dwango/nicolive/chat/data/TrialPanel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dwango/nicolive/chat/data/TrialPanel.proto',
  package='dwango.nicolive.chat.data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n*dwango/nicolive/chat/data/TrialPanel.proto\x12\x19\x64wango.nicolive.chat.data\"\xe4\x01\n\nTrialPanel\x12:\n\x05panel\x18\x01 \x01(\x0e\x32+.dwango.nicolive.chat.data.TrialPanel.Panel\x12\x44\n\x10unqualified_user\x18\x02 \x01(\x0e\x32*.dwango.nicolive.chat.data.TrialPanel.Mode\" \n\x05Panel\x12\n\n\x06Hidden\x10\x00\x12\x0b\n\x07\x44isplay\x10\x01\"2\n\x04Mode\x12\x0b\n\x07\x41llowed\x10\x00\x12\x0e\n\nRestricted\x10\x01\x12\r\n\tForbidden\x10\x02\x62\x06proto3')
)



_TRIALPANEL_PANEL = _descriptor.EnumDescriptor(
  name='Panel',
  full_name='dwango.nicolive.chat.data.TrialPanel.Panel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Hidden', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Display', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=218,
  serialized_end=250,
)
_sym_db.RegisterEnumDescriptor(_TRIALPANEL_PANEL)

_TRIALPANEL_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='dwango.nicolive.chat.data.TrialPanel.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Allowed', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Restricted', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Forbidden', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=252,
  serialized_end=302,
)
_sym_db.RegisterEnumDescriptor(_TRIALPANEL_MODE)


_TRIALPANEL = _descriptor.Descriptor(
  name='TrialPanel',
  full_name='dwango.nicolive.chat.data.TrialPanel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='panel', full_name='dwango.nicolive.chat.data.TrialPanel.panel', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unqualified_user', full_name='dwango.nicolive.chat.data.TrialPanel.unqualified_user', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRIALPANEL_PANEL,
    _TRIALPANEL_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=302,
)

_TRIALPANEL.fields_by_name['panel'].enum_type = _TRIALPANEL_PANEL
_TRIALPANEL.fields_by_name['unqualified_user'].enum_type = _TRIALPANEL_MODE
_TRIALPANEL_PANEL.containing_type = _TRIALPANEL
_TRIALPANEL_MODE.containing_type = _TRIALPANEL
DESCRIPTOR.message_types_by_name['TrialPanel'] = _TRIALPANEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrialPanel = _reflection.GeneratedProtocolMessageType('TrialPanel', (_message.Message,), dict(
  DESCRIPTOR = _TRIALPANEL,
  __module__ = 'dwango.nicolive.chat.data.TrialPanel_pb2'
  # @@protoc_insertion_point(class_scope:dwango.nicolive.chat.data.TrialPanel)
  ))
_sym_db.RegisterMessage(TrialPanel)


# @@protoc_insertion_point(module_scope)
