# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/logs/v1/log_source.proto
# Protobuf Python Version: 5.28.1
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
    1,
    '',
    'doublecloud/logs/v1/log_source.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$doublecloud/logs/v1/log_source.proto\x12\x13\x64oublecloud.logs.v1\"S\n\tLogSource\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32\".doublecloud.logs.v1.LogSourceTypeR\x04type\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id*\x85\x01\n\rLogSourceType\x12\x1b\n\x17LOG_SOURCE_TYPE_INVALID\x10\x00\x12\x1e\n\x1aLOG_SOURCE_TYPE_CLICKHOUSE\x10\x01\x12\x19\n\x15LOG_SOURCE_TYPE_KAFKA\x10\x02\x12\x1c\n\x18LOG_SOURCE_TYPE_TRANSFER\x10\x03\x42=Z;github.com/doublecloud/go-genproto/doublecloud/logs/v1;logsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.logs.v1.log_source_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z;github.com/doublecloud/go-genproto/doublecloud/logs/v1;logs'
  _globals['_LOGSOURCETYPE']._serialized_start=147
  _globals['_LOGSOURCETYPE']._serialized_end=280
  _globals['_LOGSOURCE']._serialized_start=61
  _globals['_LOGSOURCE']._serialized_end=144
# @@protoc_insertion_point(module_scope)
