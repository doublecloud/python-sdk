# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/organizationmanager/v1/group_mapping.proto
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
    'doublecloud/organizationmanager/v1/group_mapping.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6doublecloud/organizationmanager/v1/group_mapping.proto\x12\"doublecloud.organizationmanager.v1\"j\n\x10GroupMappingItem\x12*\n\x11\x65xternal_group_id\x18\x01 \x01(\tR\x0f\x65xternalGroupId\x12*\n\x11internal_group_id\x18\x02 \x01(\tR\x0finternalGroupId\"M\n\x0cGroupMapping\x12#\n\rfederation_id\x18\x01 \x01(\tR\x0c\x66\x65\x64\x65rationId\x12\x18\n\x07\x65nabled\x18\x02 \x01(\x08R\x07\x65nabledB[ZYgithub.com/doublecloud/go-genproto/doublecloud/organizationmanager/v1;organizationmanagerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.organizationmanager.v1.group_mapping_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZYgithub.com/doublecloud/go-genproto/doublecloud/organizationmanager/v1;organizationmanager'
  _globals['_GROUPMAPPINGITEM']._serialized_start=94
  _globals['_GROUPMAPPINGITEM']._serialized_end=200
  _globals['_GROUPMAPPING']._serialized_start=202
  _globals['_GROUPMAPPING']._serialized_end=279
# @@protoc_insertion_point(module_scope)