# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/kafka/v1/user_service.proto
# Protobuf Python Version: 5.28.0
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
    0,
    '',
    'doublecloud/kafka/v1/user_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2
from doublecloud.v1 import paging_pb2 as doublecloud_dot_v1_dot_paging__pb2
from doublecloud.kafka.v1 import user_pb2 as doublecloud_dot_kafka_dot_v1_dot_user__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'doublecloud/kafka/v1/user_service.proto\x12\x14\x64oublecloud.kafka.v1\x1a\x1e\x64oublecloud/v1/operation.proto\x1a\x1b\x64oublecloud/v1/paging.proto\x1a\x1f\x64oublecloud/kafka/v1/user.proto\x1a\x1egoogle/protobuf/wrappers.proto\"L\n\x0eGetUserRequest\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12\x1b\n\tuser_name\x18\x02 \x01(\tR\x08userName\"a\n\x10ListUsersRequest\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12.\n\x06paging\x18\x02 \x01(\x0b\x32\x16.doublecloud.v1.PagingR\x06paging\"|\n\x11ListUsersResponse\x12\x30\n\x05users\x18\x01 \x03(\x0b\x32\x1a.doublecloud.kafka.v1.UserR\x05users\x12\x35\n\tnext_page\x18\x02 \x01(\x0b\x32\x18.doublecloud.v1.NextPageR\x08nextPage\"o\n\x11\x43reateUserRequest\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12;\n\tuser_spec\x18\x02 \x01(\x0b\x32\x1e.doublecloud.kafka.v1.UserSpecR\x08userSpec\"\xae\x03\n\x11UpdateUserRequest\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12\x1b\n\tuser_name\x18\x02 \x01(\tR\x08userName\x12S\n\x0bupdate_spec\x18\x03 \x01(\x0b\x32\x32.doublecloud.kafka.v1.UpdateUserRequest.UpdateSpecR\nupdateSpec\x1a\x87\x02\n\nUpdateSpec\x12\x38\n\x08password\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x08password\x12\x66\n\x0bpermissions\x18\x02 \x01(\x0b\x32\x44.doublecloud.kafka.v1.UpdateUserRequest.UpdateSpec.UpdatePermissionsR\x0bpermissions\x1aW\n\x11UpdatePermissions\x12\x42\n\x0bpermissions\x18\x01 \x03(\x0b\x32 .doublecloud.kafka.v1.PermissionR\x0bpermissions\"O\n\x11\x44\x65leteUserRequest\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12\x1b\n\tuser_name\x18\x02 \x01(\tR\x08userName\"\x9a\x01\n\x1aGrantUserPermissionRequest\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12\x1b\n\tuser_name\x18\x02 \x01(\tR\x08userName\x12@\n\npermission\x18\x03 \x01(\x0b\x32 .doublecloud.kafka.v1.PermissionR\npermission\"\x9b\x01\n\x1bRevokeUserPermissionRequest\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12\x1b\n\tuser_name\x18\x02 \x01(\tR\x08userName\x12@\n\npermission\x18\x03 \x01(\x0b\x32 .doublecloud.kafka.v1.PermissionR\npermission2\xdb\x04\n\x0bUserService\x12G\n\x03Get\x12$.doublecloud.kafka.v1.GetUserRequest\x1a\x1a.doublecloud.kafka.v1.User\x12W\n\x04List\x12&.doublecloud.kafka.v1.ListUsersRequest\x1a\'.doublecloud.kafka.v1.ListUsersResponse\x12L\n\x06\x43reate\x12\'.doublecloud.kafka.v1.CreateUserRequest\x1a\x19.doublecloud.v1.Operation\x12L\n\x06Update\x12\'.doublecloud.kafka.v1.UpdateUserRequest\x1a\x19.doublecloud.v1.Operation\x12L\n\x06\x44\x65lete\x12\'.doublecloud.kafka.v1.DeleteUserRequest\x1a\x19.doublecloud.v1.Operation\x12^\n\x0fGrantPermission\x12\x30.doublecloud.kafka.v1.GrantUserPermissionRequest\x1a\x19.doublecloud.v1.Operation\x12`\n\x10RevokePermission\x12\x31.doublecloud.kafka.v1.RevokeUserPermissionRequest\x1a\x19.doublecloud.v1.OperationB?Z=github.com/doublecloud/go-genproto/doublecloud/kafka/v1;kafkab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.kafka.v1.user_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/doublecloud/go-genproto/doublecloud/kafka/v1;kafka'
  _globals['_GETUSERREQUEST']._serialized_start=191
  _globals['_GETUSERREQUEST']._serialized_end=267
  _globals['_LISTUSERSREQUEST']._serialized_start=269
  _globals['_LISTUSERSREQUEST']._serialized_end=366
  _globals['_LISTUSERSRESPONSE']._serialized_start=368
  _globals['_LISTUSERSRESPONSE']._serialized_end=492
  _globals['_CREATEUSERREQUEST']._serialized_start=494
  _globals['_CREATEUSERREQUEST']._serialized_end=605
  _globals['_UPDATEUSERREQUEST']._serialized_start=608
  _globals['_UPDATEUSERREQUEST']._serialized_end=1038
  _globals['_UPDATEUSERREQUEST_UPDATESPEC']._serialized_start=775
  _globals['_UPDATEUSERREQUEST_UPDATESPEC']._serialized_end=1038
  _globals['_UPDATEUSERREQUEST_UPDATESPEC_UPDATEPERMISSIONS']._serialized_start=951
  _globals['_UPDATEUSERREQUEST_UPDATESPEC_UPDATEPERMISSIONS']._serialized_end=1038
  _globals['_DELETEUSERREQUEST']._serialized_start=1040
  _globals['_DELETEUSERREQUEST']._serialized_end=1119
  _globals['_GRANTUSERPERMISSIONREQUEST']._serialized_start=1122
  _globals['_GRANTUSERPERMISSIONREQUEST']._serialized_end=1276
  _globals['_REVOKEUSERPERMISSIONREQUEST']._serialized_start=1279
  _globals['_REVOKEUSERPERMISSIONREQUEST']._serialized_end=1434
  _globals['_USERSERVICE']._serialized_start=1437
  _globals['_USERSERVICE']._serialized_end=2040
# @@protoc_insertion_point(module_scope)
