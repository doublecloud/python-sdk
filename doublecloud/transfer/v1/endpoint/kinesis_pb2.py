# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/transfer/v1/endpoint/kinesis.proto
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
    'doublecloud/transfer/v1/endpoint/kinesis.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.transfer.v1.endpoint import parsers_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_parsers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.doublecloud/transfer/v1/endpoint/kinesis.proto\x12 doublecloud.transfer.v1.endpoint\x1a.doublecloud/transfer/v1/endpoint/parsers.proto\"\xe8\x01\n\rKinesisSource\x12\x16\n\x06region\x18\x01 \x01(\tR\x06region\x12\x1f\n\x0bstream_name\x18\x02 \x01(\tR\nstreamName\x12)\n\x11\x61ws_access_key_id\x18\x03 \x01(\tR\x0e\x61wsAccessKeyId\x12\x31\n\x15\x61ws_secret_access_key\x18\x04 \x01(\tR\x12\x61wsSecretAccessKey\x12@\n\x06parser\x18\x05 \x01(\x0b\x32(.doublecloud.transfer.v1.endpoint.ParserR\x06parserBNZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.kinesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpoint'
  _globals['_KINESISSOURCE']._serialized_start=133
  _globals['_KINESISSOURCE']._serialized_end=365
# @@protoc_insertion_point(module_scope)
