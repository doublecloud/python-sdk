# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/transfer/v1/endpoint/airbyte/linkedin_ads_source.proto
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
    'doublecloud/transfer/v1/endpoint/airbyte/linkedin_ads_source.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBdoublecloud/transfer/v1/endpoint/airbyte/linkedin_ads_source.proto\x12(doublecloud.transfer.v1.endpoint.airbyte\"\xd9\x03\n\x11LinkedinAdsSource\x12\x1d\n\nstart_date\x18\x01 \x01(\tR\tstartDate\x12\x1f\n\x0b\x61\x63\x63ount_ids\x18\x02 \x03(\x03R\naccountIds\x12i\n\x0b\x63redentials\x18\x03 \x01(\x0b\x32G.doublecloud.transfer.v1.endpoint.airbyte.LinkedinAdsSource.CredentialsR\x0b\x63redentials\x1a\x98\x02\n\x0b\x43redentials\x12\x65\n\x05oauth\x18\x01 \x01(\x0b\x32M.doublecloud.transfer.v1.endpoint.airbyte.LinkedinAdsSource.Credentials.OAuthH\x00R\x05oauth\x12#\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\tH\x00R\x0b\x61\x63\x63\x65ssToken\x1an\n\x05OAuth\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\x12#\n\rclient_secret\x18\x02 \x01(\tR\x0c\x63lientSecret\x12#\n\rrefresh_token\x18\x03 \x01(\tR\x0crefreshTokenB\r\n\x0b\x63redentialsB^Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyteb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.airbyte.linkedin_ads_source_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyte'
  _globals['_LINKEDINADSSOURCE']._serialized_start=113
  _globals['_LINKEDINADSSOURCE']._serialized_end=586
  _globals['_LINKEDINADSSOURCE_CREDENTIALS']._serialized_start=306
  _globals['_LINKEDINADSSOURCE_CREDENTIALS']._serialized_end=586
  _globals['_LINKEDINADSSOURCE_CREDENTIALS_OAUTH']._serialized_start=461
  _globals['_LINKEDINADSSOURCE_CREDENTIALS_OAUTH']._serialized_end=571
# @@protoc_insertion_point(module_scope)
