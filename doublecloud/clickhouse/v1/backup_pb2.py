# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/clickhouse/v1/backup.proto
# Protobuf Python Version: 5.27.3
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
    3,
    '',
    'doublecloud/clickhouse/v1/backup.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&doublecloud/clickhouse/v1/backup.proto\x12\x19\x64oublecloud.clickhouse.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xfe\x02\n\x06\x42\x61\x63kup\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\nproject_id\x18\x02 \x01(\tR\tprojectId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12;\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x39\n\nstart_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12*\n\x11source_cluster_id\x18\x06 \x01(\tR\x0fsourceClusterId\x12\x12\n\x04size\x18\x07 \x01(\x03R\x04size\x12:\n\x04type\x18\x08 \x01(\x0e\x32&.doublecloud.clickhouse.v1.Backup.TypeR\x04type\"=\n\x04Type\x12\x10\n\x0cTYPE_INVALID\x10\x00\x12\x12\n\x0eTYPE_AUTOMATED\x10\x01\x12\x0f\n\x0bTYPE_MANUAL\x10\x02\x42IZGgithub.com/doublecloud/go-genproto/doublecloud/clickhouse/v1;clickhouseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.clickhouse.v1.backup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZGgithub.com/doublecloud/go-genproto/doublecloud/clickhouse/v1;clickhouse'
  _globals['_BACKUP']._serialized_start=103
  _globals['_BACKUP']._serialized_end=485
  _globals['_BACKUP_TYPE']._serialized_start=424
  _globals['_BACKUP_TYPE']._serialized_end=485
# @@protoc_insertion_point(module_scope)
