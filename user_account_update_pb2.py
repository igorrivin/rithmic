# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_account_update.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user_account_update.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x19user_account_update.proto\x12\x03rti\"\x8b\x03\n\x11UserAccountUpdate\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x38\n\x0bupdate_type\x18\xb0\xb5\t \x01(\x0e\x32!.rti.UserAccountUpdate.UpdateType\x12\x38\n\x0b\x61\x63\x63\x65ss_type\x18\x90\xb3\t \x01(\x0e\x32!.rti.UserAccountUpdate.AccessType\x12\x18\n\x0esource_user_id\x18\x87\xb5\t \x01(\t\x12\x0e\n\x04user\x18\xbb\xff\x07 \x01(\t\x12\x10\n\x06\x66\x63m_id\x18\x9d\xb3\t \x01(\t\x12\x0f\n\x05ib_id\x18\x9e\xb3\t \x01(\t\x12\x14\n\naccount_id\x18\x98\xb3\t \x01(\t\x12\x16\n\x0c\x61\x63\x63ount_name\x18\x92\xb3\t \x01(\t\x12\x0f\n\x05ssboe\x18\xd4\x94\t \x01(\x05\x12\x0f\n\x05usecs\x18\xd5\x94\t \x01(\x05\"!\n\nUpdateType\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06REMOVE\x10\x02\"+\n\nAccessType\x12\r\n\tREAD_ONLY\x10\x00\x12\x0e\n\nREAD_WRITE\x10\x01')
)



_USERACCOUNTUPDATE_UPDATETYPE = _descriptor.EnumDescriptor(
  name='UpdateType',
  full_name='rti.UserAccountUpdate.UpdateType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADD', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=352,
  serialized_end=385,
)
_sym_db.RegisterEnumDescriptor(_USERACCOUNTUPDATE_UPDATETYPE)

_USERACCOUNTUPDATE_ACCESSTYPE = _descriptor.EnumDescriptor(
  name='AccessType',
  full_name='rti.UserAccountUpdate.AccessType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='READ_ONLY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_WRITE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=387,
  serialized_end=430,
)
_sym_db.RegisterEnumDescriptor(_USERACCOUNTUPDATE_ACCESSTYPE)


_USERACCOUNTUPDATE = _descriptor.Descriptor(
  name='UserAccountUpdate',
  full_name='rti.UserAccountUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.UserAccountUpdate.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_type', full_name='rti.UserAccountUpdate.update_type', index=1,
      number=154288, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_type', full_name='rti.UserAccountUpdate.access_type', index=2,
      number=154000, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_user_id', full_name='rti.UserAccountUpdate.source_user_id', index=3,
      number=154247, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='rti.UserAccountUpdate.user', index=4,
      number=131003, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fcm_id', full_name='rti.UserAccountUpdate.fcm_id', index=5,
      number=154013, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ib_id', full_name='rti.UserAccountUpdate.ib_id', index=6,
      number=154014, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='rti.UserAccountUpdate.account_id', index=7,
      number=154008, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_name', full_name='rti.UserAccountUpdate.account_name', index=8,
      number=154002, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ssboe', full_name='rti.UserAccountUpdate.ssboe', index=9,
      number=150100, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usecs', full_name='rti.UserAccountUpdate.usecs', index=10,
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
    _USERACCOUNTUPDATE_UPDATETYPE,
    _USERACCOUNTUPDATE_ACCESSTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=430,
)

_USERACCOUNTUPDATE.fields_by_name['update_type'].enum_type = _USERACCOUNTUPDATE_UPDATETYPE
_USERACCOUNTUPDATE.fields_by_name['access_type'].enum_type = _USERACCOUNTUPDATE_ACCESSTYPE
_USERACCOUNTUPDATE_UPDATETYPE.containing_type = _USERACCOUNTUPDATE
_USERACCOUNTUPDATE_ACCESSTYPE.containing_type = _USERACCOUNTUPDATE
DESCRIPTOR.message_types_by_name['UserAccountUpdate'] = _USERACCOUNTUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserAccountUpdate = _reflection.GeneratedProtocolMessageType('UserAccountUpdate', (_message.Message,), dict(
  DESCRIPTOR = _USERACCOUNTUPDATE,
  __module__ = 'user_account_update_pb2'
  # @@protoc_insertion_point(class_scope:rti.UserAccountUpdate)
  ))
_sym_db.RegisterMessage(UserAccountUpdate)


# @@protoc_insertion_point(module_scope)