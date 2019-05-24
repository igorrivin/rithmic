# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: end_of_day_prices.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='end_of_day_prices.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x17\x65nd_of_day_prices.proto\x12\x03rti\"\x84\x03\n\x0e\x45ndOfDayPrices\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x10\n\x06symbol\x18\x94\xdc\x06 \x01(\t\x12\x12\n\x08\x65xchange\x18\x95\xdc\x06 \x01(\t\x12\x17\n\rpresence_bits\x18\x92\x8d\t \x01(\r\x12\x14\n\nclear_bits\x18\xcb\xb7\t \x01(\r\x12\x15\n\x0bis_snapshot\x18\xa9\xdc\x06 \x01(\x08\x12\x15\n\x0b\x63lose_price\x18\xb5\x8d\x06 \x01(\x01\x12\x14\n\nclose_date\x18\xef\x8d\x06 \x01(\t\x12\x1a\n\x10settlement_price\x18\xe6\x8d\x06 \x01(\x01\x12\x19\n\x0fsettlement_date\x18\x94\xb4\t \x01(\t\x12$\n\x1aprojected_settlement_price\x18\xfd\xba\t \x01(\x01\x12\x0f\n\x05ssboe\x18\xd4\x94\t \x01(\x05\x12\x0f\n\x05usecs\x18\xd5\x94\t \x01(\x05\"C\n\x0cPresenceBits\x12\t\n\x05\x43LOSE\x10\x01\x12\x0e\n\nSETTLEMENT\x10\x02\x12\x18\n\x14PROJECTED_SETTLEMENT\x10\x04')
)



_ENDOFDAYPRICES_PRESENCEBITS = _descriptor.EnumDescriptor(
  name='PresenceBits',
  full_name='rti.EndOfDayPrices.PresenceBits',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CLOSE', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SETTLEMENT', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROJECTED_SETTLEMENT', index=2, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=354,
  serialized_end=421,
)
_sym_db.RegisterEnumDescriptor(_ENDOFDAYPRICES_PRESENCEBITS)


_ENDOFDAYPRICES = _descriptor.Descriptor(
  name='EndOfDayPrices',
  full_name='rti.EndOfDayPrices',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.EndOfDayPrices.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='rti.EndOfDayPrices.symbol', index=1,
      number=110100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='rti.EndOfDayPrices.exchange', index=2,
      number=110101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='presence_bits', full_name='rti.EndOfDayPrices.presence_bits', index=3,
      number=149138, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clear_bits', full_name='rti.EndOfDayPrices.clear_bits', index=4,
      number=154571, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_snapshot', full_name='rti.EndOfDayPrices.is_snapshot', index=5,
      number=110121, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_price', full_name='rti.EndOfDayPrices.close_price', index=6,
      number=100021, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_date', full_name='rti.EndOfDayPrices.close_date', index=7,
      number=100079, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settlement_price', full_name='rti.EndOfDayPrices.settlement_price', index=8,
      number=100070, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settlement_date', full_name='rti.EndOfDayPrices.settlement_date', index=9,
      number=154132, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='projected_settlement_price', full_name='rti.EndOfDayPrices.projected_settlement_price', index=10,
      number=155005, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ssboe', full_name='rti.EndOfDayPrices.ssboe', index=11,
      number=150100, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usecs', full_name='rti.EndOfDayPrices.usecs', index=12,
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
    _ENDOFDAYPRICES_PRESENCEBITS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=421,
)

_ENDOFDAYPRICES_PRESENCEBITS.containing_type = _ENDOFDAYPRICES
DESCRIPTOR.message_types_by_name['EndOfDayPrices'] = _ENDOFDAYPRICES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EndOfDayPrices = _reflection.GeneratedProtocolMessageType('EndOfDayPrices', (_message.Message,), dict(
  DESCRIPTOR = _ENDOFDAYPRICES,
  __module__ = 'end_of_day_prices_pb2'
  # @@protoc_insertion_point(class_scope:rti.EndOfDayPrices)
  ))
_sym_db.RegisterMessage(EndOfDayPrices)


# @@protoc_insertion_point(module_scope)
