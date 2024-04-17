# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/network/v1/operation_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2
from doublecloud.v1 import paging_pb2 as doublecloud_dot_v1_dot_paging__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.doublecloud/network/v1/operation_service.proto\x12\x16\x64oublecloud.network.v1\x1a\x1e\x64oublecloud/v1/operation.proto\x1a\x1b\x64oublecloud/v1/paging.proto\"8\n\x13GetOperationRequest\x12!\n\x0coperation_id\x18\x01 \x01(\tR\x0boperationId\"f\n\x15ListOperationsRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12.\n\x06paging\x18\x02 \x01(\x0b\x32\x16.doublecloud.v1.PagingR\x06paging\"\x8a\x01\n\x16ListOperationsResponse\x12\x39\n\noperations\x18\x01 \x03(\x0b\x32\x19.doublecloud.v1.OperationR\noperations\x12\x35\n\tnext_page\x18\x02 \x01(\x0b\x32\x18.doublecloud.v1.NextPageR\x08nextPage2\xc8\x01\n\x10OperationService\x12M\n\x03Get\x12+.doublecloud.network.v1.GetOperationRequest\x1a\x19.doublecloud.v1.Operation\x12\x65\n\x04List\x12-.doublecloud.network.v1.ListOperationsRequest\x1a..doublecloud.network.v1.ListOperationsResponseBCZAgithub.com/doublecloud/go-genproto/doublecloud/network/v1;networkb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.network.v1.operation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/doublecloud/go-genproto/doublecloud/network/v1;network'
  _globals['_GETOPERATIONREQUEST']._serialized_start=135
  _globals['_GETOPERATIONREQUEST']._serialized_end=191
  _globals['_LISTOPERATIONSREQUEST']._serialized_start=193
  _globals['_LISTOPERATIONSREQUEST']._serialized_end=295
  _globals['_LISTOPERATIONSRESPONSE']._serialized_start=298
  _globals['_LISTOPERATIONSRESPONSE']._serialized_end=436
  _globals['_OPERATIONSERVICE']._serialized_start=439
  _globals['_OPERATIONSERVICE']._serialized_end=639
# @@protoc_insertion_point(module_scope)
