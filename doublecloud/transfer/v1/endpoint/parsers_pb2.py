# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/transfer/v1/endpoint/parsers.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.transfer.v1.endpoint import common_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.doublecloud/transfer/v1/endpoint/parsers.proto\x12 doublecloud.transfer.v1.endpoint\x1a-doublecloud/transfer/v1/endpoint/common.proto\"\xc6\x01\n\x06Parser\x12X\n\x0bjson_parser\x18\x01 \x01(\x0b\x32\x35.doublecloud.transfer.v1.endpoint.GenericParserCommonH\x00R\njsonParser\x12X\n\x0btskv_parser\x18\x06 \x01(\x0b\x32\x35.doublecloud.transfer.v1.endpoint.GenericParserCommonH\x00R\ntskvParserB\x08\n\x06parser\"\xb8\x01\n\x13GenericParserCommon\x12M\n\x0b\x64\x61ta_schema\x18\x01 \x01(\x0b\x32,.doublecloud.transfer.v1.endpoint.DataSchemaR\ndataSchema\x12*\n\x11null_keys_allowed\x18\x02 \x01(\x08R\x0fnullKeysAllowed\x12&\n\x0f\x61\x64\x64_rest_column\x18\x03 \x01(\x08R\raddRestColumnBFZDgithub.com/doublecloud/api/doublecloud/transfer/v1/endpoint;endpointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.parsers_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZDgithub.com/doublecloud/api/doublecloud/transfer/v1/endpoint;endpoint'
  _globals['_PARSER']._serialized_start=132
  _globals['_PARSER']._serialized_end=330
  _globals['_GENERICPARSERCOMMON']._serialized_start=333
  _globals['_GENERICPARSERCOMMON']._serialized_end=517
# @@protoc_insertion_point(module_scope)
