# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/transfer/v1/endpoint/bigquery.proto
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
    'doublecloud/transfer/v1/endpoint/bigquery.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/doublecloud/transfer/v1/endpoint/bigquery.proto\x12 doublecloud.transfer.v1.endpoint\"y\n\x0e\x42igQueryTarget\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x1d\n\ndataset_id\x18\x02 \x01(\tR\tdatasetId\x12)\n\x10\x63redentials_json\x18\x03 \x01(\tR\x0f\x63redentialsJsonBNZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.bigquery_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpoint'
  _globals['_BIGQUERYTARGET']._serialized_start=85
  _globals['_BIGQUERYTARGET']._serialized_end=206
# @@protoc_insertion_point(module_scope)
