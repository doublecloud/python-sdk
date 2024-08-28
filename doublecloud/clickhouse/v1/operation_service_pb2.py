# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/clickhouse/v1/operation_service.proto
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
    'doublecloud/clickhouse/v1/operation_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2
from doublecloud.v1 import paging_pb2 as doublecloud_dot_v1_dot_paging__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1doublecloud/clickhouse/v1/operation_service.proto\x12\x19\x64oublecloud.clickhouse.v1\x1a\x1e\x64oublecloud/v1/operation.proto\x1a\x1b\x64oublecloud/v1/paging.proto\"8\n\x13GetOperationRequest\x12!\n\x0coperation_id\x18\x01 \x01(\tR\x0boperationId\"f\n\x15ListOperationsRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12.\n\x06paging\x18\x02 \x01(\x0b\x32\x16.doublecloud.v1.PagingR\x06paging\"\x8a\x01\n\x16ListOperationsResponse\x12\x39\n\noperations\x18\x01 \x03(\x0b\x32\x19.doublecloud.v1.OperationR\noperations\x12\x35\n\tnext_page\x18\x02 \x01(\x0b\x32\x18.doublecloud.v1.NextPageR\x08nextPage2\xd1\x01\n\x10OperationService\x12P\n\x03Get\x12..doublecloud.clickhouse.v1.GetOperationRequest\x1a\x19.doublecloud.v1.Operation\x12k\n\x04List\x12\x30.doublecloud.clickhouse.v1.ListOperationsRequest\x1a\x31.doublecloud.clickhouse.v1.ListOperationsResponseBIZGgithub.com/doublecloud/go-genproto/doublecloud/clickhouse/v1;clickhouseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.clickhouse.v1.operation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZGgithub.com/doublecloud/go-genproto/doublecloud/clickhouse/v1;clickhouse'
  _globals['_GETOPERATIONREQUEST']._serialized_start=141
  _globals['_GETOPERATIONREQUEST']._serialized_end=197
  _globals['_LISTOPERATIONSREQUEST']._serialized_start=199
  _globals['_LISTOPERATIONSREQUEST']._serialized_end=301
  _globals['_LISTOPERATIONSRESPONSE']._serialized_start=304
  _globals['_LISTOPERATIONSRESPONSE']._serialized_end=442
  _globals['_OPERATIONSERVICE']._serialized_start=445
  _globals['_OPERATIONSERVICE']._serialized_end=654
# @@protoc_insertion_point(module_scope)
