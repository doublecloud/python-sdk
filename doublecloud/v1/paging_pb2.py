# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/v1/paging.proto
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
    'doublecloud/v1/paging.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x64oublecloud/v1/paging.proto\x12\x0e\x64oublecloud.v1\"D\n\x06Paging\x12\x1b\n\tpage_size\x18\x01 \x01(\x03R\x08pageSize\x12\x1d\n\npage_token\x18\x02 \x01(\tR\tpageToken\" \n\x08NextPage\x12\x14\n\x05token\x18\x01 \x01(\tR\x05tokenB?Z=github.com/doublecloud/go-genproto/doublecloud/v1;doublecloudb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.v1.paging_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/doublecloud/go-genproto/doublecloud/v1;doublecloud'
  _globals['_PAGING']._serialized_start=47
  _globals['_PAGING']._serialized_end=115
  _globals['_NEXTPAGE']._serialized_start=117
  _globals['_NEXTPAGE']._serialized_end=149
# @@protoc_insertion_point(module_scope)
