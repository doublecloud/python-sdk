# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/transfer/v1/endpoint/airbyte/hubspot_source.proto
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
    'doublecloud/transfer/v1/endpoint/airbyte/hubspot_source.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=doublecloud/transfer/v1/endpoint/airbyte/hubspot_source.proto\x12(doublecloud.transfer.v1.endpoint.airbyte\"\x98\x03\n\rHubspotSource\x12\x1d\n\nstart_date\x18\x01 \x01(\tR\tstartDate\x12\x65\n\x0b\x63redentials\x18\x02 \x01(\x0b\x32\x43.doublecloud.transfer.v1.endpoint.airbyte.HubspotSource.CredentialsR\x0b\x63redentials\x12>\n\x1b\x65nable_experimental_streams\x18\x03 \x01(\x08R\x19\x65nableExperimentalStreams\x1a\xc0\x01\n\x0b\x43redentials\x12q\n\x0bprivate_app\x18\x01 \x01(\x0b\x32N.doublecloud.transfer.v1.endpoint.airbyte.HubspotSource.Credentials.PrivateAppH\x00R\nprivateApp\x1a/\n\nPrivateApp\x12!\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\tR\x0b\x61\x63\x63\x65ssTokenB\r\n\x0b\x61uth_methodB^Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyteb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.airbyte.hubspot_source_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyte'
  _globals['_HUBSPOTSOURCE']._serialized_start=108
  _globals['_HUBSPOTSOURCE']._serialized_end=516
  _globals['_HUBSPOTSOURCE_CREDENTIALS']._serialized_start=324
  _globals['_HUBSPOTSOURCE_CREDENTIALS']._serialized_end=516
  _globals['_HUBSPOTSOURCE_CREDENTIALS_PRIVATEAPP']._serialized_start=454
  _globals['_HUBSPOTSOURCE_CREDENTIALS_PRIVATEAPP']._serialized_end=501
# @@protoc_insertion_point(module_scope)
