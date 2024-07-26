# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/logs/v1/log_service.proto
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
    'doublecloud/logs/v1/log_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2
from doublecloud.v1 import paging_pb2 as doublecloud_dot_v1_dot_paging__pb2
from doublecloud.logs.v1 import log_pb2 as doublecloud_dot_logs_dot_v1_dot_log__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%doublecloud/logs/v1/log_service.proto\x12\x13\x64oublecloud.logs.v1\x1a\x1e\x64oublecloud/v1/operation.proto\x1a\x1b\x64oublecloud/v1/paging.proto\x1a\x1d\x64oublecloud/logs/v1/log.proto\"\x8e\x01\n\x0fReadLogsRequest\x12\x32\n\x06paging\x18\x01 \x01(\x0b\x32\x18.doublecloud.v1.NextPageH\x00R\x06paging\x12;\n\x08\x63riteria\x18\x02 \x01(\x0b\x32\x1d.doublecloud.logs.v1.CriteriaH\x00R\x08\x63riteriaB\n\n\x08selector\"~\n\rReadLogRecord\x12\x36\n\x06record\x18\x01 \x01(\x0b\x32\x1e.doublecloud.logs.v1.LogRecordR\x06record\x12\x35\n\tnext_page\x18\x02 \x01(\x0b\x32\x18.doublecloud.v1.NextPageR\x08nextPage2`\n\nLogService\x12R\n\x04Read\x12$.doublecloud.logs.v1.ReadLogsRequest\x1a\".doublecloud.logs.v1.ReadLogRecord0\x01\x42=Z;github.com/doublecloud/go-genproto/doublecloud/logs/v1;logsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.logs.v1.log_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z;github.com/doublecloud/go-genproto/doublecloud/logs/v1;logs'
  _globals['_READLOGSREQUEST']._serialized_start=155
  _globals['_READLOGSREQUEST']._serialized_end=297
  _globals['_READLOGRECORD']._serialized_start=299
  _globals['_READLOGRECORD']._serialized_end=425
  _globals['_LOGSERVICE']._serialized_start=427
  _globals['_LOGSERVICE']._serialized_end=523
# @@protoc_insertion_point(module_scope)