# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/logs/v1/operation_service.proto
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
    'doublecloud/logs/v1/operation_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+doublecloud/logs/v1/operation_service.proto\x12\x13\x64oublecloud.logs.v1\x1a\x1e\x64oublecloud/v1/operation.proto\"8\n\x13GetOperationRequest\x12!\n\x0coperation_id\x18\x01 \x01(\tR\x0boperationId2^\n\x10OperationService\x12J\n\x03Get\x12(.doublecloud.logs.v1.GetOperationRequest\x1a\x19.doublecloud.v1.OperationB=Z;github.com/doublecloud/go-genproto/doublecloud/logs/v1;logsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.logs.v1.operation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z;github.com/doublecloud/go-genproto/doublecloud/logs/v1;logs'
  _globals['_GETOPERATIONREQUEST']._serialized_start=100
  _globals['_GETOPERATIONREQUEST']._serialized_end=156
  _globals['_OPERATIONSERVICE']._serialized_start=158
  _globals['_OPERATIONSERVICE']._serialized_end=252
# @@protoc_insertion_point(module_scope)