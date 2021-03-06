# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_give_tick_size_type_table.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_give_tick_size_type_table.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n(response_give_tick_size_type_table.proto\x12\x03rti\"\xc9\x03\n\x1dResponseGiveTickSizeTypeTable\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x12\n\x08user_msg\x18\x98\x8d\x08 \x03(\t\x12\x1c\n\x12rq_handler_rp_code\x18\x9c\x8d\x08 \x03(\t\x12\x11\n\x07rp_code\x18\x9e\x8d\x08 \x03(\t\x12\x17\n\rpresence_bits\x18\x92\x8d\t \x01(\r\x12\x18\n\x0etick_size_type\x18\xb7\xb4\t \x01(\t\x12\x1f\n\x15tick_size_fp_operator\x18\xba\xb4\t \x01(\t\x12\x1f\n\x15tick_size_lp_operator\x18\xbb\xb4\t \x01(\t\x12\x1b\n\x11min_fprice_change\x18\x93\xb6\t \x01(\x01\x12\x1f\n\x15tick_size_first_price\x18\xb8\xb4\t \x01(\x01\x12\x1e\n\x14tick_size_last_price\x18\xb9\xb4\t \x01(\x01\"y\n\x0cPresenceBits\x12\x19\n\x15TICK_SIZE_FIRST_PRICE\x10\x01\x12\x18\n\x14TICK_SIZE_LAST_PRICE\x10\x02\x12\x19\n\x15TICK_SIZE_FP_OPERATOR\x10\x04\x12\x19\n\x15TICK_SIZE_LP_OPERATOR\x10\x08')
)



_RESPONSEGIVETICKSIZETYPETABLE_PRESENCEBITS = _descriptor.EnumDescriptor(
  name='PresenceBits',
  full_name='rti.ResponseGiveTickSizeTypeTable.PresenceBits',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TICK_SIZE_FIRST_PRICE', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TICK_SIZE_LAST_PRICE', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TICK_SIZE_FP_OPERATOR', index=2, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TICK_SIZE_LP_OPERATOR', index=3, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=386,
  serialized_end=507,
)
_sym_db.RegisterEnumDescriptor(_RESPONSEGIVETICKSIZETYPETABLE_PRESENCEBITS)


_RESPONSEGIVETICKSIZETYPETABLE = _descriptor.Descriptor(
  name='ResponseGiveTickSizeTypeTable',
  full_name='rti.ResponseGiveTickSizeTypeTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.ResponseGiveTickSizeTypeTable.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_msg', full_name='rti.ResponseGiveTickSizeTypeTable.user_msg', index=1,
      number=132760, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rq_handler_rp_code', full_name='rti.ResponseGiveTickSizeTypeTable.rq_handler_rp_code', index=2,
      number=132764, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rp_code', full_name='rti.ResponseGiveTickSizeTypeTable.rp_code', index=3,
      number=132766, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='presence_bits', full_name='rti.ResponseGiveTickSizeTypeTable.presence_bits', index=4,
      number=149138, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tick_size_type', full_name='rti.ResponseGiveTickSizeTypeTable.tick_size_type', index=5,
      number=154167, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tick_size_fp_operator', full_name='rti.ResponseGiveTickSizeTypeTable.tick_size_fp_operator', index=6,
      number=154170, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tick_size_lp_operator', full_name='rti.ResponseGiveTickSizeTypeTable.tick_size_lp_operator', index=7,
      number=154171, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_fprice_change', full_name='rti.ResponseGiveTickSizeTypeTable.min_fprice_change', index=8,
      number=154387, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tick_size_first_price', full_name='rti.ResponseGiveTickSizeTypeTable.tick_size_first_price', index=9,
      number=154168, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tick_size_last_price', full_name='rti.ResponseGiveTickSizeTypeTable.tick_size_last_price', index=10,
      number=154169, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSEGIVETICKSIZETYPETABLE_PRESENCEBITS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=507,
)

_RESPONSEGIVETICKSIZETYPETABLE_PRESENCEBITS.containing_type = _RESPONSEGIVETICKSIZETYPETABLE
DESCRIPTOR.message_types_by_name['ResponseGiveTickSizeTypeTable'] = _RESPONSEGIVETICKSIZETYPETABLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseGiveTickSizeTypeTable = _reflection.GeneratedProtocolMessageType('ResponseGiveTickSizeTypeTable', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEGIVETICKSIZETYPETABLE,
  __module__ = 'response_give_tick_size_type_table_pb2'
  # @@protoc_insertion_point(class_scope:rti.ResponseGiveTickSizeTypeTable)
  ))
_sym_db.RegisterMessage(ResponseGiveTickSizeTypeTable)


# @@protoc_insertion_point(module_scope)
