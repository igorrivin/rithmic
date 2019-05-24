# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_account_rms_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_account_rms_info.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1fresponse_account_rms_info.proto\x12\x03rti\"\xf3\x07\n\x16ResponseAccountRmsInfo\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x12\n\x08user_msg\x18\x98\x8d\x08 \x03(\t\x12\x1c\n\x12rq_handler_rp_code\x18\x9c\x8d\x08 \x03(\t\x12\x11\n\x07rp_code\x18\x9e\x8d\x08 \x03(\t\x12\x17\n\rpresence_bits\x18\x96\xb0\t \x01(\r\x12\x10\n\x06\x66\x63m_id\x18\x9d\xb3\t \x01(\t\x12\x0f\n\x05ib_id\x18\x9e\xb3\t \x01(\t\x12\x14\n\naccount_id\x18\x98\xb3\t \x01(\t\x12\x12\n\x08\x63urrency\x18\x8f\xb6\t \x01(\t\x12\x10\n\x06status\x18\x93\xb3\t \x01(\t\x12\x13\n\talgorithm\x18\xfe\x94\t \x01(\t\x12!\n\x17\x61uto_liquidate_criteria\x18\xdc\xff\x07 \x01(\t\x12G\n\x0e\x61uto_liquidate\x18\xdb\xff\x07 \x01(\x0e\x32-.rti.ResponseAccountRmsInfo.AutoLiquidateFlag\x12R\n\x19\x64isable_on_auto_liquidate\x18\xde\xff\x07 \x01(\x0e\x32-.rti.ResponseAccountRmsInfo.AutoLiquidateFlag\x12\"\n\x18\x61uto_liquidate_threshold\x18\xdd\xff\x07 \x01(\x01\x12\x30\n&auto_liquidate_max_min_account_balance\x18\xdf\xff\x07 \x01(\x01\x12\x14\n\nloss_limit\x18\xa3\xb3\t \x01(\x01\x12\x1d\n\x13min_account_balance\x18\xa8\xca\t \x01(\x01\x12\x1c\n\x12min_margin_balance\x18\xb0\xca\t \x01(\x01\x12\x1c\n\x12\x64\x65\x66\x61ult_commission\x18\x98\xae\t \x01(\x01\x12\x13\n\tbuy_limit\x18\x99\xb3\t \x01(\x05\x12\x1c\n\x12max_order_quantity\x18\x99\xdc\x06 \x01(\x05\x12\x14\n\nsell_limit\x18\xb3\xb3\t \x01(\x05\x12#\n\x19\x63heck_min_account_balance\x18\xac\xca\t \x01(\x08\"\xca\x01\n\x0cPresenceBits\x12\r\n\tBUY_LIMIT\x10\x01\x12\x0e\n\nSELL_LIMIT\x10\x02\x12\x0e\n\nLOSS_LIMIT\x10\x04\x12\x16\n\x12MAX_ORDER_QUANTITY\x10\x08\x12\x17\n\x13MIN_ACCOUNT_BALANCE\x10\x10\x12\x16\n\x12MIN_MARGIN_BALANCE\x10 \x12\r\n\tALGORITHM\x10@\x12\x0b\n\x06STATUS\x10\x80\x01\x12\r\n\x08\x43URRENCY\x10\x80\x02\x12\x17\n\x12\x44\x45\x46\x41ULT_COMMISSION\x10\x80\x04\".\n\x11\x41utoLiquidateFlag\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02')
)



_RESPONSEACCOUNTRMSINFO_PRESENCEBITS = _descriptor.EnumDescriptor(
  name='PresenceBits',
  full_name='rti.ResponseAccountRmsInfo.PresenceBits',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUY_LIMIT', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SELL_LIMIT', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOSS_LIMIT', index=2, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX_ORDER_QUANTITY', index=3, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIN_ACCOUNT_BALANCE', index=4, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIN_MARGIN_BALANCE', index=5, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALGORITHM', index=6, number=64,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS', index=7, number=128,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CURRENCY', index=8, number=256,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFAULT_COMMISSION', index=9, number=512,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=802,
  serialized_end=1004,
)
_sym_db.RegisterEnumDescriptor(_RESPONSEACCOUNTRMSINFO_PRESENCEBITS)

_RESPONSEACCOUNTRMSINFO_AUTOLIQUIDATEFLAG = _descriptor.EnumDescriptor(
  name='AutoLiquidateFlag',
  full_name='rti.ResponseAccountRmsInfo.AutoLiquidateFlag',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENABLED', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISABLED', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1006,
  serialized_end=1052,
)
_sym_db.RegisterEnumDescriptor(_RESPONSEACCOUNTRMSINFO_AUTOLIQUIDATEFLAG)


_RESPONSEACCOUNTRMSINFO = _descriptor.Descriptor(
  name='ResponseAccountRmsInfo',
  full_name='rti.ResponseAccountRmsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.ResponseAccountRmsInfo.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_msg', full_name='rti.ResponseAccountRmsInfo.user_msg', index=1,
      number=132760, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rq_handler_rp_code', full_name='rti.ResponseAccountRmsInfo.rq_handler_rp_code', index=2,
      number=132764, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rp_code', full_name='rti.ResponseAccountRmsInfo.rp_code', index=3,
      number=132766, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='presence_bits', full_name='rti.ResponseAccountRmsInfo.presence_bits', index=4,
      number=153622, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fcm_id', full_name='rti.ResponseAccountRmsInfo.fcm_id', index=5,
      number=154013, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ib_id', full_name='rti.ResponseAccountRmsInfo.ib_id', index=6,
      number=154014, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='rti.ResponseAccountRmsInfo.account_id', index=7,
      number=154008, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency', full_name='rti.ResponseAccountRmsInfo.currency', index=8,
      number=154383, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='rti.ResponseAccountRmsInfo.status', index=9,
      number=154003, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='rti.ResponseAccountRmsInfo.algorithm', index=10,
      number=150142, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auto_liquidate_criteria', full_name='rti.ResponseAccountRmsInfo.auto_liquidate_criteria', index=11,
      number=131036, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auto_liquidate', full_name='rti.ResponseAccountRmsInfo.auto_liquidate', index=12,
      number=131035, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disable_on_auto_liquidate', full_name='rti.ResponseAccountRmsInfo.disable_on_auto_liquidate', index=13,
      number=131038, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auto_liquidate_threshold', full_name='rti.ResponseAccountRmsInfo.auto_liquidate_threshold', index=14,
      number=131037, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auto_liquidate_max_min_account_balance', full_name='rti.ResponseAccountRmsInfo.auto_liquidate_max_min_account_balance', index=15,
      number=131039, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss_limit', full_name='rti.ResponseAccountRmsInfo.loss_limit', index=16,
      number=154019, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_account_balance', full_name='rti.ResponseAccountRmsInfo.min_account_balance', index=17,
      number=156968, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_margin_balance', full_name='rti.ResponseAccountRmsInfo.min_margin_balance', index=18,
      number=156976, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_commission', full_name='rti.ResponseAccountRmsInfo.default_commission', index=19,
      number=153368, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buy_limit', full_name='rti.ResponseAccountRmsInfo.buy_limit', index=20,
      number=154009, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_order_quantity', full_name='rti.ResponseAccountRmsInfo.max_order_quantity', index=21,
      number=110105, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sell_limit', full_name='rti.ResponseAccountRmsInfo.sell_limit', index=22,
      number=154035, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='check_min_account_balance', full_name='rti.ResponseAccountRmsInfo.check_min_account_balance', index=23,
      number=156972, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSEACCOUNTRMSINFO_PRESENCEBITS,
    _RESPONSEACCOUNTRMSINFO_AUTOLIQUIDATEFLAG,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=1052,
)

_RESPONSEACCOUNTRMSINFO.fields_by_name['auto_liquidate'].enum_type = _RESPONSEACCOUNTRMSINFO_AUTOLIQUIDATEFLAG
_RESPONSEACCOUNTRMSINFO.fields_by_name['disable_on_auto_liquidate'].enum_type = _RESPONSEACCOUNTRMSINFO_AUTOLIQUIDATEFLAG
_RESPONSEACCOUNTRMSINFO_PRESENCEBITS.containing_type = _RESPONSEACCOUNTRMSINFO
_RESPONSEACCOUNTRMSINFO_AUTOLIQUIDATEFLAG.containing_type = _RESPONSEACCOUNTRMSINFO
DESCRIPTOR.message_types_by_name['ResponseAccountRmsInfo'] = _RESPONSEACCOUNTRMSINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseAccountRmsInfo = _reflection.GeneratedProtocolMessageType('ResponseAccountRmsInfo', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEACCOUNTRMSINFO,
  __module__ = 'response_account_rms_info_pb2'
  # @@protoc_insertion_point(class_scope:rti.ResponseAccountRmsInfo)
  ))
_sym_db.RegisterMessage(ResponseAccountRmsInfo)


# @@protoc_insertion_point(module_scope)
