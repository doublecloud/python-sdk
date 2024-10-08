# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/organizationmanager/v1/group_service.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from doublecloud.organizationmanager.v1 import group_pb2 as doublecloud_dot_organizationmanager_dot_v1_dot_group__pb2
from doublecloud.access.v1 import access_pb2 as doublecloud_dot_access_dot_v1_dot_access__pb2
from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6doublecloud/organizationmanager/v1/group_service.proto\x12\"doublecloud.organizationmanager.v1\x1a\x1egoogle/protobuf/duration.proto\x1a.doublecloud/organizationmanager/v1/group.proto\x1a\"doublecloud/access/v1/access.proto\x1a\x1e\x64oublecloud/v1/operation.proto\",\n\x0fGetGroupRequest\x12\x19\n\x08group_id\x18\x01 \x01(\tR\x07groupId\"\x90\x01\n\x11ListGroupsRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x1b\n\tpage_size\x18\x02 \x01(\x03R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\x12\x16\n\x06\x66ilter\x18\x04 \x01(\tR\x06\x66ilter\"\x7f\n\x12ListGroupsResponse\x12\x41\n\x06groups\x18\x01 \x03(\x0b\x32).doublecloud.organizationmanager.v1.GroupR\x06groups\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"s\n\x12\x43reateGroupRequest\x12\'\n\x0forganization_id\x18\x01 \x01(\tR\x0eorganizationId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\"e\n\x12UpdateGroupRequest\x12\x19\n\x08group_id\x18\x01 \x01(\tR\x07groupId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\"/\n\x12\x44\x65leteGroupRequest\x12\x19\n\x08group_id\x18\x01 \x01(\tR\x07groupId\"s\n\x1aListGroupOperationsRequest\x12\x19\n\x08group_id\x18\x01 \x01(\tR\x07groupId\x12\x1b\n\tpage_size\x18\x02 \x01(\x03R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\x80\x01\n\x1bListGroupOperationsResponse\x12\x39\n\noperations\x18\x01 \x03(\x0b\x32\x19.doublecloud.v1.OperationR\noperations\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"p\n\x17ListGroupMembersRequest\x12\x19\n\x08group_id\x18\x01 \x01(\tR\x07groupId\x12\x1b\n\tpage_size\x18\x02 \x01(\x03R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\x8d\x01\n\x18ListGroupMembersResponse\x12I\n\x07members\x18\x01 \x03(\x0b\x32/.doublecloud.organizationmanager.v1.GroupMemberR\x07members\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"O\n\x0bGroupMember\x12\x1d\n\nsubject_id\x18\x01 \x01(\tR\tsubjectId\x12!\n\x0csubject_type\x18\x02 \x01(\tR\x0bsubjectType\"\x8c\x01\n\x19UpdateGroupMembersRequest\x12\x19\n\x08group_id\x18\x01 \x01(\tR\x07groupId\x12T\n\rmember_deltas\x18\x02 \x03(\x0b\x32/.doublecloud.organizationmanager.v1.MemberDeltaR\x0cmemberDeltas\"\xc6\x01\n\x0bMemberDelta\x12T\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32<.doublecloud.organizationmanager.v1.MemberDelta.MemberActionR\x06\x61\x63tion\x12\x1d\n\nsubject_id\x18\x02 \x01(\tR\tsubjectId\"B\n\x0cMemberAction\x12\x1d\n\x19MEMBER_ACTION_UNSPECIFIED\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06REMOVE\x10\x02\x32\xe6\t\n\x0cGroupService\x12g\n\x03Get\x12\x33.doublecloud.organizationmanager.v1.GetGroupRequest\x1a).doublecloud.organizationmanager.v1.Group\"\x00\x12w\n\x04List\x12\x35.doublecloud.organizationmanager.v1.ListGroupsRequest\x1a\x36.doublecloud.organizationmanager.v1.ListGroupsResponse\"\x00\x12]\n\x06\x43reate\x12\x36.doublecloud.organizationmanager.v1.CreateGroupRequest\x1a\x19.doublecloud.v1.Operation\"\x00\x12]\n\x06Update\x12\x36.doublecloud.organizationmanager.v1.UpdateGroupRequest\x1a\x19.doublecloud.v1.Operation\"\x00\x12]\n\x06\x44\x65lete\x12\x36.doublecloud.organizationmanager.v1.DeleteGroupRequest\x1a\x19.doublecloud.v1.Operation\"\x00\x12\x93\x01\n\x0eListOperations\x12>.doublecloud.organizationmanager.v1.ListGroupOperationsRequest\x1a?.doublecloud.organizationmanager.v1.ListGroupOperationsResponse\"\x00\x12\x8a\x01\n\x0bListMembers\x12;.doublecloud.organizationmanager.v1.ListGroupMembersRequest\x1a<.doublecloud.organizationmanager.v1.ListGroupMembersResponse\"\x00\x12k\n\rUpdateMembers\x12=.doublecloud.organizationmanager.v1.UpdateGroupMembersRequest\x1a\x19.doublecloud.v1.Operation\"\x00\x12{\n\x12ListAccessBindings\x12\x30.doublecloud.access.v1.ListAccessBindingsRequest\x1a\x31.doublecloud.access.v1.ListAccessBindingsResponse\"\x00\x12\x61\n\x11SetAccessBindings\x12/.doublecloud.access.v1.SetAccessBindingsRequest\x1a\x19.doublecloud.v1.Operation\"\x00\x12g\n\x14UpdateAccessBindings\x12\x32.doublecloud.access.v1.UpdateAccessBindingsRequest\x1a\x19.doublecloud.v1.Operation\"\x00\x42[ZYgithub.com/doublecloud/go-genproto/doublecloud/organizationmanager/v1;organizationmanagerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.organizationmanager.v1.group_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZYgithub.com/doublecloud/go-genproto/doublecloud/organizationmanager/v1;organizationmanager'
  _globals['_GETGROUPREQUEST']._serialized_start=242
  _globals['_GETGROUPREQUEST']._serialized_end=286
  _globals['_LISTGROUPSREQUEST']._serialized_start=289
  _globals['_LISTGROUPSREQUEST']._serialized_end=433
  _globals['_LISTGROUPSRESPONSE']._serialized_start=435
  _globals['_LISTGROUPSRESPONSE']._serialized_end=562
  _globals['_CREATEGROUPREQUEST']._serialized_start=564
  _globals['_CREATEGROUPREQUEST']._serialized_end=679
  _globals['_UPDATEGROUPREQUEST']._serialized_start=681
  _globals['_UPDATEGROUPREQUEST']._serialized_end=782
  _globals['_DELETEGROUPREQUEST']._serialized_start=784
  _globals['_DELETEGROUPREQUEST']._serialized_end=831
  _globals['_LISTGROUPOPERATIONSREQUEST']._serialized_start=833
  _globals['_LISTGROUPOPERATIONSREQUEST']._serialized_end=948
  _globals['_LISTGROUPOPERATIONSRESPONSE']._serialized_start=951
  _globals['_LISTGROUPOPERATIONSRESPONSE']._serialized_end=1079
  _globals['_LISTGROUPMEMBERSREQUEST']._serialized_start=1081
  _globals['_LISTGROUPMEMBERSREQUEST']._serialized_end=1193
  _globals['_LISTGROUPMEMBERSRESPONSE']._serialized_start=1196
  _globals['_LISTGROUPMEMBERSRESPONSE']._serialized_end=1337
  _globals['_GROUPMEMBER']._serialized_start=1339
  _globals['_GROUPMEMBER']._serialized_end=1418
  _globals['_UPDATEGROUPMEMBERSREQUEST']._serialized_start=1421
  _globals['_UPDATEGROUPMEMBERSREQUEST']._serialized_end=1561
  _globals['_MEMBERDELTA']._serialized_start=1564
  _globals['_MEMBERDELTA']._serialized_end=1762
  _globals['_MEMBERDELTA_MEMBERACTION']._serialized_start=1696
  _globals['_MEMBERDELTA_MEMBERACTION']._serialized_end=1762
  _globals['_GROUPSERVICE']._serialized_start=1765
  _globals['_GROUPSERVICE']._serialized_end=3019
# @@protoc_insertion_point(module_scope)
