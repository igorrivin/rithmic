# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_pnl_position_updates.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_pnl_position_updates.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n#response_pnl_position_updates.proto\x12\x03rti\"Z\n\x1aResponsePnLPositionUpdates\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x12\n\x08user_msg\x18\x98\x8d\x08 \x03(\t\x12\x11\n\x07rp_code\x18\x9e\x8d\x08 \x03(\t')
)




_RESPONSEPNLPOSITIONUPDATES = _descriptor.Descriptor(
  name='ResponsePnLPositionUpdates',
  full_name='rti.ResponsePnLPositionUpdates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.ResponsePnLPositionUpdates.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_msg', full_name='rti.ResponsePnLPositionUpdates.user_msg', index=1,
      number=132760, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rp_code', full_name='rti.ResponsePnLPositionUpdates.rp_code', index=2,
      number=132766, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['ResponsePnLPositionUpdates'] = _RESPONSEPNLPOSITIONUPDATES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponsePnLPositionUpdates = _reflection.GeneratedProtocolMessageType('ResponsePnLPositionUpdates', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEPNLPOSITIONUPDATES,
  __module__ = 'response_pnl_position_updates_pb2'
  # @@protoc_insertion_point(class_scope:rti.ResponsePnLPositionUpdates)
  ))
_sym_db.RegisterMessage(ResponsePnLPositionUpdates)


# @@protoc_insertion_point(module_scope)
