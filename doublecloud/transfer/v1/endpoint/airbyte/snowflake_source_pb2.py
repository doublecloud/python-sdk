# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/transfer/v1/endpoint/airbyte/snowflake_source.proto
# Protobuf Python Version: 5.27.2
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
    2,
    '',
    'doublecloud/transfer/v1/endpoint/airbyte/snowflake_source.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?doublecloud/transfer/v1/endpoint/airbyte/snowflake_source.proto\x12(doublecloud.transfer.v1.endpoint.airbyte\"\xf7\x05\n\x0fSnowflakeSource\x12\x12\n\x04host\x18\x01 \x01(\tR\x04host\x12\x12\n\x04role\x18\x02 \x01(\tR\x04role\x12\x1c\n\twarehouse\x18\x03 \x01(\tR\twarehouse\x12\x1a\n\x08\x64\x61tabase\x18\x04 \x01(\tR\x08\x64\x61tabase\x12\x16\n\x06schema\x18\x05 \x01(\tR\x06schema\x12&\n\x0fjdbc_url_params\x18\x06 \x01(\tR\rjdbcUrlParams\x12g\n\x0b\x63redentials\x18\x07 \x01(\x0b\x32\x45.doublecloud.transfer.v1.endpoint.airbyte.SnowflakeSource.CredentialsR\x0b\x63redentials\x1a\xd8\x03\n\x0b\x43redentials\x12\x63\n\x05oauth\x18\x01 \x01(\x0b\x32K.doublecloud.transfer.v1.endpoint.airbyte.SnowflakeSource.Credentials.OAuthH\x00R\x05oauth\x12p\n\nbasic_auth\x18\x02 \x01(\x0b\x32O.doublecloud.transfer.v1.endpoint.airbyte.SnowflakeSource.Credentials.BasicAuthH\x00R\tbasicAuth\x1a\x97\x01\n\x05OAuth\x12\x1b\n\tclient_id\x18\x02 \x01(\tR\x08\x63lientId\x12#\n\rclient_secret\x18\x03 \x01(\tR\x0c\x63lientSecret\x12!\n\x0c\x61\x63\x63\x65ss_token\x18\x04 \x01(\tR\x0b\x61\x63\x63\x65ssToken\x12#\n\rrefresh_token\x18\x05 \x01(\tR\x0crefreshTokenJ\x04\x08\x01\x10\x02\x1aI\n\tBasicAuth\x12\x1a\n\x08username\x18\x02 \x01(\tR\x08username\x12\x1a\n\x08password\x18\x03 \x01(\tR\x08passwordJ\x04\x08\x01\x10\x02\x42\r\n\x0b\x63redentialsB^Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyteb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.airbyte.snowflake_source_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyte'
  _globals['_SNOWFLAKESOURCE']._serialized_start=110
  _globals['_SNOWFLAKESOURCE']._serialized_end=869
  _globals['_SNOWFLAKESOURCE_CREDENTIALS']._serialized_start=397
  _globals['_SNOWFLAKESOURCE_CREDENTIALS']._serialized_end=869
  _globals['_SNOWFLAKESOURCE_CREDENTIALS_OAUTH']._serialized_start=628
  _globals['_SNOWFLAKESOURCE_CREDENTIALS_OAUTH']._serialized_end=779
  _globals['_SNOWFLAKESOURCE_CREDENTIALS_BASICAUTH']._serialized_start=781
  _globals['_SNOWFLAKESOURCE_CREDENTIALS_BASICAUTH']._serialized_end=854
# @@protoc_insertion_point(module_scope)
