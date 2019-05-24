# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: symbol_margin_rate.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='symbol_margin_rate.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x18symbol_margin_rate.proto\x12\x03rti\"}\n\x10SymbolMarginRate\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x10\n\x06symbol\x18\x94\xdc\x06 \x01(\t\x12\x12\n\x08\x65xchange\x18\x95\xdc\x06 \x01(\t\x12\x15\n\x0bis_snapshot\x18\xa9\xdc\x06 \x01(\x08\x12\x15\n\x0bmargin_rate\x18\xf7\xb3\t \x01(\x01')
)




_SYMBOLMARGINRATE = _descriptor.Descriptor(
  name='SymbolMarginRate',
  full_name='rti.SymbolMarginRate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.SymbolMarginRate.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='rti.SymbolMarginRate.symbol', index=1,
      number=110100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='rti.SymbolMarginRate.exchange', index=2,
      number=110101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_snapshot', full_name='rti.SymbolMarginRate.is_snapshot', index=3,
      number=110121, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='margin_rate', full_name='rti.SymbolMarginRate.margin_rate', index=4,
      number=154103, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=33,
  serialized_end=158,
)

DESCRIPTOR.message_types_by_name['SymbolMarginRate'] = _SYMBOLMARGINRATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SymbolMarginRate = _reflection.GeneratedProtocolMessageType('SymbolMarginRate', (_message.Message,), dict(
  DESCRIPTOR = _SYMBOLMARGINRATE,
  __module__ = 'symbol_margin_rate_pb2'
  # @@protoc_insertion_point(class_scope:rti.SymbolMarginRate)
  ))
_sym_db.RegisterMessage(SymbolMarginRate)


# @@protoc_insertion_point(module_scope)
