# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/v1/operation.proto
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
    'doublecloud/v1/operation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x64oublecloud/v1/operation.proto\x12\x0e\x64oublecloud.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\"\x8e\x05\n\tOperation\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\nproject_id\x18\x02 \x01(\tR\tprojectId\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1d\n\ncreated_by\x18\x04 \x01(\tR\tcreatedBy\x12\x43\n\x08metadata\x18\x05 \x03(\x0b\x32\'.doublecloud.v1.Operation.MetadataEntryR\x08metadata\x12;\n\x0b\x63reate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x39\n\nstart_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12;\n\x0b\x66inish_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nfinishTime\x12\x38\n\x06status\x18\t \x01(\x0e\x32 .doublecloud.v1.Operation.StatusR\x06status\x12(\n\x05\x65rror\x18\n \x01(\x0b\x32\x12.google.rpc.StatusR\x05\x65rror\x12\x1f\n\x0bresource_id\x18\x0b \x01(\tR\nresourceId\x1a;\n\rMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"U\n\x06Status\x12\x12\n\x0eSTATUS_INVALID\x10\x00\x12\x12\n\x0eSTATUS_PENDING\x10\x01\x12\x12\n\x0eSTATUS_RUNNING\x10\x02\x12\x0f\n\x0bSTATUS_DONE\x10\x03\x42?Z=github.com/doublecloud/go-genproto/doublecloud/v1;doublecloudb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.v1.operation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/doublecloud/go-genproto/doublecloud/v1;doublecloud'
  _globals['_OPERATION_METADATAENTRY']._loaded_options = None
  _globals['_OPERATION_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_OPERATION']._serialized_start=109
  _globals['_OPERATION']._serialized_end=763
  _globals['_OPERATION_METADATAENTRY']._serialized_start=617
  _globals['_OPERATION_METADATAENTRY']._serialized_end=676
  _globals['_OPERATION_STATUS']._serialized_start=678
  _globals['_OPERATION_STATUS']._serialized_end=763
# @@protoc_insertion_point(module_scope)
