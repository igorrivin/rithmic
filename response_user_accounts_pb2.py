# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_user_accounts.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_user_accounts.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1cresponse_user_accounts.proto\x12\x03rti\"\xab\x01\n\x14ResponseUserAccounts\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x12\n\x08user_msg\x18\x98\x8d\x08 \x03(\t\x12\x1c\n\x12rq_handler_rp_code\x18\x9c\x8d\x08 \x03(\t\x12\x11\n\x07rp_code\x18\x9e\x8d\x08 \x03(\t\x12\x10\n\x06\x66\x63m_id\x18\x9d\xb3\t \x01(\t\x12\x0f\n\x05ib_id\x18\x9e\xb3\t \x01(\t\x12\x14\n\naccount_id\x18\x98\xb3\t \x01(\t')
)




_RESPONSEUSERACCOUNTS = _descriptor.Descriptor(
  name='ResponseUserAccounts',
  full_name='rti.ResponseUserAccounts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.ResponseUserAccounts.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_msg', full_name='rti.ResponseUserAccounts.user_msg', index=1,
      number=132760, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rq_handler_rp_code', full_name='rti.ResponseUserAccounts.rq_handler_rp_code', index=2,
      number=132764, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rp_code', full_name='rti.ResponseUserAccounts.rp_code', index=3,
      number=132766, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fcm_id', full_name='rti.ResponseUserAccounts.fcm_id', index=4,
      number=154013, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ib_id', full_name='rti.ResponseUserAccounts.ib_id', index=5,
      number=154014, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='rti.ResponseUserAccounts.account_id', index=6,
      number=154008, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=209,
)

DESCRIPTOR.message_types_by_name['ResponseUserAccounts'] = _RESPONSEUSERACCOUNTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseUserAccounts = _reflection.GeneratedProtocolMessageType('ResponseUserAccounts', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEUSERACCOUNTS,
  __module__ = 'response_user_accounts_pb2'
  # @@protoc_insertion_point(class_scope:rti.ResponseUserAccounts)
  ))
_sym_db.RegisterMessage(ResponseUserAccounts)


# @@protoc_insertion_point(module_scope)
