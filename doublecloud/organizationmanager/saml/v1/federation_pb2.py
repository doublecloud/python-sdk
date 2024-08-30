# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/organizationmanager/saml/v1/federation.proto
# Protobuf Python Version: 5.28.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    0,
    '',
    'doublecloud/organizationmanager/saml/v1/federation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8doublecloud/organizationmanager/saml/v1/federation.proto\x12\'doublecloud.organizationmanager.saml.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xec\x04\n\nFederation\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\'\n\x0forganization_id\x18\x02 \x01(\tR\x0eorganizationId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x39\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12?\n\x0e\x63ookie_max_age\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0c\x63ookieMaxAge\x12>\n\x1c\x61uto_create_account_on_login\x18\x07 \x01(\x08R\x18\x61utoCreateAccountOnLogin\x12\x16\n\x06issuer\x18\x08 \x01(\tR\x06issuer\x12U\n\x0bsso_binding\x18\t \x01(\x0e\x32\x34.doublecloud.organizationmanager.saml.v1.BindingTypeR\nssoBinding\x12\x17\n\x07sso_url\x18\n \x01(\tR\x06ssoUrl\x12p\n\x11security_settings\x18\x0b \x01(\x0b\x32\x43.doublecloud.organizationmanager.saml.v1.FederationSecuritySettingsR\x10securitySettings\x12\x39\n\x19\x63\x61se_insensitive_name_ids\x18\x0c \x01(\x08R\x16\x63\x61seInsensitiveNameIds\"O\n\x1a\x46\x65\x64\x65rationSecuritySettings\x12\x31\n\x14\x65ncrypted_assertions\x18\x01 \x01(\x08R\x13\x65ncryptedAssertions*Q\n\x0b\x42indingType\x12\x1c\n\x18\x42INDING_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04POST\x10\x01\x12\x0c\n\x08REDIRECT\x10\x02\x12\x0c\n\x08\x41RTIFACT\x10\x03\x42QZOgithub.com/doublecloud/go-genproto/doublecloud/organizationmanager/saml/v1;samlb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.organizationmanager.saml.v1.federation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZOgithub.com/doublecloud/go-genproto/doublecloud/organizationmanager/saml/v1;saml'
  _globals['_BINDINGTYPE']._serialized_start=870
  _globals['_BINDINGTYPE']._serialized_end=951
  _globals['_FEDERATION']._serialized_start=167
  _globals['_FEDERATION']._serialized_end=787
  _globals['_FEDERATIONSECURITYSETTINGS']._serialized_start=789
  _globals['_FEDERATIONSECURITYSETTINGS']._serialized_end=868
# @@protoc_insertion_point(module_scope)
