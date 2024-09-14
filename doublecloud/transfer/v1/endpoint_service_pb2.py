# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/transfer/v1/endpoint_service.proto
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
    'doublecloud/transfer/v1/endpoint_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from doublecloud.transfer.v1 import endpoint_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint__pb2
from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2
from doublecloud.v1 import paging_pb2 as doublecloud_dot_v1_dot_paging__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.doublecloud/transfer/v1/endpoint_service.proto\x12\x17\x64oublecloud.transfer.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a&doublecloud/transfer/v1/endpoint.proto\x1a\x1e\x64oublecloud/v1/operation.proto\x1a\x1b\x64oublecloud/v1/paging.proto\"5\n\x12GetEndpointRequest\x12\x1f\n\x0b\x65ndpoint_id\x18\x01 \x01(\tR\nendpointId\"a\n\x14ListEndpointsRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12*\n\x04page\x18\x02 \x01(\x0b\x32\x16.doublecloud.v1.PagingR\x04page\"\x8f\x01\n\x15ListEndpointsResponse\x12?\n\tendpoints\x18\x01 \x03(\x0b\x32!.doublecloud.transfer.v1.EndpointR\tendpoints\x12\x35\n\tnext_page\x18\x02 \x01(\x0b\x32\x18.doublecloud.v1.NextPageR\x08nextPage\"\xc8\x02\n\x15\x43reateEndpointRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12R\n\x06labels\x18\x04 \x03(\x0b\x32:.doublecloud.transfer.v1.CreateEndpointRequest.LabelsEntryR\x06labels\x12\x45\n\x08settings\x18\x34 \x01(\x0b\x32).doublecloud.transfer.v1.EndpointSettingsR\x08settings\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01J\x04\x08\x05\x10\x34\"\xd0\x02\n\x15UpdateEndpointRequest\x12\x1f\n\x0b\x65ndpoint_id\x18\n \x01(\tR\nendpointId\x12\x12\n\x04name\x18\x0b \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x0c \x01(\tR\x0b\x64\x65scription\x12R\n\x06labels\x18\r \x03(\x0b\x32:.doublecloud.transfer.v1.UpdateEndpointRequest.LabelsEntryR\x06labels\x12\x45\n\x08settings\x18\x34 \x01(\x0b\x32).doublecloud.transfer.v1.EndpointSettingsR\x08settings\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01J\x04\x08\x01\x10\nJ\x04\x08\x0e\x10\x34\"8\n\x15\x44\x65leteEndpointRequest\x12\x1f\n\x0b\x65ndpoint_id\x18\x01 \x01(\tR\nendpointId2\xce\x03\n\x0f\x45ndpointService\x12U\n\x03Get\x12+.doublecloud.transfer.v1.GetEndpointRequest\x1a!.doublecloud.transfer.v1.Endpoint\x12\x65\n\x04List\x12-.doublecloud.transfer.v1.ListEndpointsRequest\x1a..doublecloud.transfer.v1.ListEndpointsResponse\x12S\n\x06\x43reate\x12..doublecloud.transfer.v1.CreateEndpointRequest\x1a\x19.doublecloud.v1.Operation\x12S\n\x06Update\x12..doublecloud.transfer.v1.UpdateEndpointRequest\x1a\x19.doublecloud.v1.Operation\x12S\n\x06\x44\x65lete\x12..doublecloud.transfer.v1.DeleteEndpointRequest\x1a\x19.doublecloud.v1.OperationBEZCgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1;transferb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZCgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1;transfer'
  _globals['_CREATEENDPOINTREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATEENDPOINTREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATEENDPOINTREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATEENDPOINTREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_GETENDPOINTREQUEST']._serialized_start=240
  _globals['_GETENDPOINTREQUEST']._serialized_end=293
  _globals['_LISTENDPOINTSREQUEST']._serialized_start=295
  _globals['_LISTENDPOINTSREQUEST']._serialized_end=392
  _globals['_LISTENDPOINTSRESPONSE']._serialized_start=395
  _globals['_LISTENDPOINTSRESPONSE']._serialized_end=538
  _globals['_CREATEENDPOINTREQUEST']._serialized_start=541
  _globals['_CREATEENDPOINTREQUEST']._serialized_end=869
  _globals['_CREATEENDPOINTREQUEST_LABELSENTRY']._serialized_start=806
  _globals['_CREATEENDPOINTREQUEST_LABELSENTRY']._serialized_end=863
  _globals['_UPDATEENDPOINTREQUEST']._serialized_start=872
  _globals['_UPDATEENDPOINTREQUEST']._serialized_end=1208
  _globals['_UPDATEENDPOINTREQUEST_LABELSENTRY']._serialized_start=806
  _globals['_UPDATEENDPOINTREQUEST_LABELSENTRY']._serialized_end=863
  _globals['_DELETEENDPOINTREQUEST']._serialized_start=1210
  _globals['_DELETEENDPOINTREQUEST']._serialized_end=1266
  _globals['_ENDPOINTSERVICE']._serialized_start=1269
  _globals['_ENDPOINTSERVICE']._serialized_end=1731
# @@protoc_insertion_point(module_scope)
