# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/transfer/v1/endpoint/delta_lake.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.transfer.v1.endpoint.airbyte import s3_source_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_airbyte_dot_s3__source__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1doublecloud/transfer/v1/endpoint/delta_lake.proto\x12 doublecloud.transfer.v1.endpoint\x1a\x38\x64oublecloud/transfer/v1/endpoint/airbyte/s3_source.proto\"\x81\x02\n\x0f\x44\x65ltaLakeSource\x12W\n\x08provider\x18\x01 \x01(\x0b\x32;.doublecloud.transfer.v1.endpoint.airbyte.S3Source.ProviderR\x08provider\x12H\n\x05table\x18\x02 \x01(\x0b\x32\x32.doublecloud.transfer.v1.endpoint.DeltaResultTableR\x05table\x12K\n\x08settings\x18\x03 \x01(\x0b\x32/.doublecloud.transfer.v1.endpoint.DeltaSettingsR\x08settings\"\x12\n\x10\x44\x65ltaResultTable\"\'\n\rDeltaSettings\x12\x16\n\x06region\x18\x02 \x01(\tR\x06regionBNZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.delta_lake_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpoint'
  _globals['_DELTALAKESOURCE']._serialized_start=146
  _globals['_DELTALAKESOURCE']._serialized_end=403
  _globals['_DELTARESULTTABLE']._serialized_start=405
  _globals['_DELTARESULTTABLE']._serialized_end=423
  _globals['_DELTASETTINGS']._serialized_start=425
  _globals['_DELTASETTINGS']._serialized_end=464
# @@protoc_insertion_point(module_scope)