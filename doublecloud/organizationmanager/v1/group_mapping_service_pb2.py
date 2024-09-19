# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/organizationmanager/v1/group_mapping_service.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from doublecloud.organizationmanager.v1 import group_mapping_pb2 as doublecloud_dot_organizationmanager_dot_v1_dot_group__mapping__pb2
from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>doublecloud/organizationmanager/v1/group_mapping_service.proto\x12\"doublecloud.organizationmanager.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x36\x64oublecloud/organizationmanager/v1/group_mapping.proto\x1a\x1e\x64oublecloud/v1/operation.proto\"=\n\x16GetGroupMappingRequest\x12#\n\rfederation_id\x18\x01 \x01(\tR\x0c\x66\x65\x64\x65rationId\"p\n\x17GetGroupMappingResponse\x12U\n\rgroup_mapping\x18\x01 \x01(\x0b\x32\x30.doublecloud.organizationmanager.v1.GroupMappingR\x0cgroupMapping\"Z\n\x19\x43reateGroupMappingRequest\x12#\n\rfederation_id\x18\x01 \x01(\tR\x0c\x66\x65\x64\x65rationId\x12\x18\n\x07\x65nabled\x18\x03 \x01(\x08R\x07\x65nabled\"Z\n\x19UpdateGroupMappingRequest\x12#\n\rfederation_id\x18\x01 \x01(\tR\x0c\x66\x65\x64\x65rationId\x12\x18\n\x07\x65nabled\x18\x03 \x01(\x08R\x07\x65nabled\"@\n\x19\x44\x65leteGroupMappingRequest\x12#\n\rfederation_id\x18\x01 \x01(\tR\x0c\x66\x65\x64\x65rationId\"\xbb\x01\n\x1eUpdateGroupMappingItemsRequest\x12#\n\rfederation_id\x18\x01 \x01(\tR\x0c\x66\x65\x64\x65rationId\x12t\n\x19group_mapping_item_deltas\x18\x04 \x03(\x0b\x32\x39.doublecloud.organizationmanager.v1.GroupMappingItemDeltaR\x16groupMappingItemDeltas\"\xf2\x01\n\x15GroupMappingItemDelta\x12H\n\x04item\x18\x01 \x01(\x0b\x32\x34.doublecloud.organizationmanager.v1.GroupMappingItemR\x04item\x12X\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32@.doublecloud.organizationmanager.v1.GroupMappingItemDelta.ActionR\x06\x61\x63tion\"5\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_UNSPECIFIED\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06REMOVE\x10\x02\"\x97\x01\n\x1fUpdateGroupMappingItemsResponse\x12t\n\x19group_mapping_item_deltas\x18\x04 \x03(\x0b\x32\x39.doublecloud.organizationmanager.v1.GroupMappingItemDeltaR\x16groupMappingItemDeltas\"\x97\x01\n\x1cListGroupMappingItemsRequest\x12#\n\rfederation_id\x18\x01 \x01(\tR\x0c\x66\x65\x64\x65rationId\x12\x1b\n\tpage_size\x18\x02 \x01(\x03R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\x12\x16\n\x06\x66ilter\x18\x04 \x01(\tR\x06\x66ilter\"\xad\x01\n\x1dListGroupMappingItemsResponse\x12\x64\n\x13group_mapping_items\x18\x01 \x03(\x0b\x32\x34.doublecloud.organizationmanager.v1.GroupMappingItemR\x11groupMappingItems\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken2\xca\x05\n\x13GroupMappingService\x12~\n\x03Get\x12:.doublecloud.organizationmanager.v1.GetGroupMappingRequest\x1a;.doublecloud.organizationmanager.v1.GetGroupMappingResponse\x12\x64\n\x06\x43reate\x12=.doublecloud.organizationmanager.v1.CreateGroupMappingRequest\x1a\x19.doublecloud.v1.Operation\"\x00\x12\x64\n\x06Update\x12=.doublecloud.organizationmanager.v1.UpdateGroupMappingRequest\x1a\x19.doublecloud.v1.Operation\"\x00\x12\x64\n\x06\x44\x65lete\x12=.doublecloud.organizationmanager.v1.DeleteGroupMappingRequest\x1a\x19.doublecloud.v1.Operation\"\x00\x12\x90\x01\n\tListItems\x12@.doublecloud.organizationmanager.v1.ListGroupMappingItemsRequest\x1a\x41.doublecloud.organizationmanager.v1.ListGroupMappingItemsResponse\x12n\n\x0bUpdateItems\x12\x42.doublecloud.organizationmanager.v1.UpdateGroupMappingItemsRequest\x1a\x19.doublecloud.v1.Operation\"\x00\x42[ZYgithub.com/doublecloud/go-genproto/doublecloud/organizationmanager/v1;organizationmanagerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.organizationmanager.v1.group_mapping_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZYgithub.com/doublecloud/go-genproto/doublecloud/organizationmanager/v1;organizationmanager'
  _globals['_GETGROUPMAPPINGREQUEST']._serialized_start=222
  _globals['_GETGROUPMAPPINGREQUEST']._serialized_end=283
  _globals['_GETGROUPMAPPINGRESPONSE']._serialized_start=285
  _globals['_GETGROUPMAPPINGRESPONSE']._serialized_end=397
  _globals['_CREATEGROUPMAPPINGREQUEST']._serialized_start=399
  _globals['_CREATEGROUPMAPPINGREQUEST']._serialized_end=489
  _globals['_UPDATEGROUPMAPPINGREQUEST']._serialized_start=491
  _globals['_UPDATEGROUPMAPPINGREQUEST']._serialized_end=581
  _globals['_DELETEGROUPMAPPINGREQUEST']._serialized_start=583
  _globals['_DELETEGROUPMAPPINGREQUEST']._serialized_end=647
  _globals['_UPDATEGROUPMAPPINGITEMSREQUEST']._serialized_start=650
  _globals['_UPDATEGROUPMAPPINGITEMSREQUEST']._serialized_end=837
  _globals['_GROUPMAPPINGITEMDELTA']._serialized_start=840
  _globals['_GROUPMAPPINGITEMDELTA']._serialized_end=1082
  _globals['_GROUPMAPPINGITEMDELTA_ACTION']._serialized_start=1029
  _globals['_GROUPMAPPINGITEMDELTA_ACTION']._serialized_end=1082
  _globals['_UPDATEGROUPMAPPINGITEMSRESPONSE']._serialized_start=1085
  _globals['_UPDATEGROUPMAPPINGITEMSRESPONSE']._serialized_end=1236
  _globals['_LISTGROUPMAPPINGITEMSREQUEST']._serialized_start=1239
  _globals['_LISTGROUPMAPPINGITEMSREQUEST']._serialized_end=1390
  _globals['_LISTGROUPMAPPINGITEMSRESPONSE']._serialized_start=1393
  _globals['_LISTGROUPMAPPINGITEMSRESPONSE']._serialized_end=1566
  _globals['_GROUPMAPPINGSERVICE']._serialized_start=1569
  _globals['_GROUPMAPPINGSERVICE']._serialized_end=2283
# @@protoc_insertion_point(module_scope)
