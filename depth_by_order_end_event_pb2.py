# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: depth_by_order_end_event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='depth_by_order_end_event.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1e\x64\x65pth_by_order_end_event.proto\x12\x03rti\"\x90\x01\n\x14\x44\x65pthByOrderEndEvent\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x10\n\x06symbol\x18\x94\xdc\x06 \x03(\t\x12\x12\n\x08\x65xchange\x18\x95\xdc\x06 \x03(\t\x12\x19\n\x0fsequence_number\x18\x82\xeb\x06 \x01(\x04\x12\x0f\n\x05ssboe\x18\xd4\x94\t \x01(\x05\x12\x0f\n\x05usecs\x18\xd5\x94\t \x01(\x05')
)




_DEPTHBYORDERENDEVENT = _descriptor.Descriptor(
  name='DepthByOrderEndEvent',
  full_name='rti.DepthByOrderEndEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.DepthByOrderEndEvent.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='rti.DepthByOrderEndEvent.symbol', index=1,
      number=110100, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='rti.DepthByOrderEndEvent.exchange', index=2,
      number=110101, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='rti.DepthByOrderEndEvent.sequence_number', index=3,
      number=112002, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ssboe', full_name='rti.DepthByOrderEndEvent.ssboe', index=4,
      number=150100, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usecs', full_name='rti.DepthByOrderEndEvent.usecs', index=5,
      number=150101, type=5, cpp_type=1, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=184,
)

DESCRIPTOR.message_types_by_name['DepthByOrderEndEvent'] = _DEPTHBYORDERENDEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DepthByOrderEndEvent = _reflection.GeneratedProtocolMessageType('DepthByOrderEndEvent', (_message.Message,), dict(
  DESCRIPTOR = _DEPTHBYORDERENDEVENT,
  __module__ = 'depth_by_order_end_event_pb2'
  # @@protoc_insertion_point(class_scope:rti.DepthByOrderEndEvent)
  ))
_sym_db.RegisterMessage(DepthByOrderEndEvent)


# @@protoc_insertion_point(module_scope)
