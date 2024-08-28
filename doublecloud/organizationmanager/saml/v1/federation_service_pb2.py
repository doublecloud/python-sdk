# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/organizationmanager/saml/v1/federation_service.proto
# Protobuf Python Version: 5.27.4
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    4,
    '',
    'doublecloud/organizationmanager/saml/v1/federation_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from doublecloud.organizationmanager.saml.v1 import federation_pb2 as doublecloud_dot_organizationmanager_dot_saml_dot_v1_dot_federation__pb2
from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@doublecloud/organizationmanager/saml/v1/federation_service.proto\x12\'doublecloud.organizationmanager.saml.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x38\x64oublecloud/organizationmanager/saml/v1/federation.proto\x1a\x1e\x64oublecloud/v1/operation.proto\";\n\x14GetFederationRequest\x12#\n\rfederation_id\x18\x01 \x01(\tR\x0c\x66\x65\x64\x65rationId\"\xae\x04\n\x17\x43reateFederationRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12?\n\x0e\x63ookie_max_age\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0c\x63ookieMaxAge\x12>\n\x1c\x61uto_create_account_on_login\x18\x05 \x01(\x08R\x18\x61utoCreateAccountOnLogin\x12\x16\n\x06issuer\x18\x06 \x01(\tR\x06issuer\x12U\n\x0bsso_binding\x18\x07 \x01(\x0e\x32\x34.doublecloud.organizationmanager.saml.v1.BindingTypeR\nssoBinding\x12\x17\n\x07sso_url\x18\x08 \x01(\tR\x06ssoUrl\x12p\n\x11security_settings\x18\t \x01(\x0b\x32\x43.doublecloud.organizationmanager.saml.v1.FederationSecuritySettingsR\x10securitySettings\x12\x39\n\x19\x63\x61se_insensitive_name_ids\x18\n \x01(\x08R\x16\x63\x61seInsensitiveNameIds\"\xaa\x04\n\x17UpdateFederationRequest\x12#\n\rfederation_id\x18\x01 \x01(\tR\x0c\x66\x65\x64\x65rationId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12?\n\x0e\x63ookie_max_age\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0c\x63ookieMaxAge\x12>\n\x1c\x61uto_create_account_on_login\x18\x06 \x01(\x08R\x18\x61utoCreateAccountOnLogin\x12\x16\n\x06issuer\x18\x07 \x01(\tR\x06issuer\x12U\n\x0bsso_binding\x18\x08 \x01(\x0e\x32\x34.doublecloud.organizationmanager.saml.v1.BindingTypeR\nssoBinding\x12\x17\n\x07sso_url\x18\t \x01(\tR\x06ssoUrl\x12p\n\x11security_settings\x18\n \x01(\x0b\x32\x43.doublecloud.organizationmanager.saml.v1.FederationSecuritySettingsR\x10securitySettings\x12\x39\n\x19\x63\x61se_insensitive_name_ids\x18\x0c \x01(\x08R\x16\x63\x61seInsensitiveNameIds\">\n\x17\x44\x65leteFederationRequest\x12#\n\rfederation_id\x18\x01 \x01(\tR\x0c\x66\x65\x64\x65rationId2\xcb\x03\n\x11\x46\x65\x64\x65rationService\x12{\n\x03Get\x12=.doublecloud.organizationmanager.saml.v1.GetFederationRequest\x1a\x33.doublecloud.organizationmanager.saml.v1.Federation\"\x00\x12g\n\x06\x43reate\x12@.doublecloud.organizationmanager.saml.v1.CreateFederationRequest\x1a\x19.doublecloud.v1.Operation\"\x00\x12g\n\x06Update\x12@.doublecloud.organizationmanager.saml.v1.UpdateFederationRequest\x1a\x19.doublecloud.v1.Operation\"\x00\x12g\n\x06\x44\x65lete\x12@.doublecloud.organizationmanager.saml.v1.DeleteFederationRequest\x1a\x19.doublecloud.v1.Operation\"\x00\x42QZOgithub.com/doublecloud/go-genproto/doublecloud/organizationmanager/saml/v1;samlb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.organizationmanager.saml.v1.federation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZOgithub.com/doublecloud/go-genproto/doublecloud/organizationmanager/saml/v1;saml'
  _globals['_GETFEDERATIONREQUEST']._serialized_start=231
  _globals['_GETFEDERATIONREQUEST']._serialized_end=290
  _globals['_CREATEFEDERATIONREQUEST']._serialized_start=293
  _globals['_CREATEFEDERATIONREQUEST']._serialized_end=851
  _globals['_UPDATEFEDERATIONREQUEST']._serialized_start=854
  _globals['_UPDATEFEDERATIONREQUEST']._serialized_end=1408
  _globals['_DELETEFEDERATIONREQUEST']._serialized_start=1410
  _globals['_DELETEFEDERATIONREQUEST']._serialized_end=1472
  _globals['_FEDERATIONSERVICE']._serialized_start=1475
  _globals['_FEDERATIONSERVICE']._serialized_end=1934
# @@protoc_insertion_point(module_scope)
