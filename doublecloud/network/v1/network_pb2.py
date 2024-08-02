# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/network/v1/network.proto
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
    'doublecloud/network/v1/network.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$doublecloud/network/v1/network.proto\x12\x16\x64oublecloud.network.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xfb\x05\n\x07Network\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\nproject_id\x18\x02 \x01(\tR\tprojectId\x12\x1d\n\ncloud_type\x18\x03 \x01(\tR\tcloudType\x12\x1b\n\tregion_id\x18\x04 \x01(\tR\x08regionId\x12;\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x12\n\x04name\x18\x06 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x07 \x01(\tR\x0b\x64\x65scription\x12&\n\x0fipv4_cidr_block\x18\x08 \x01(\tR\ripv4CidrBlock\x12&\n\x0fipv6_cidr_block\x18\t \x01(\tR\ripv6CidrBlock\x12\x45\n\x06status\x18\n \x01(\x0e\x32-.doublecloud.network.v1.Network.NetworkStatusR\x06status\x12#\n\rstatus_reason\x18\x0b \x01(\tR\x0cstatusReason\x12@\n\x03\x61ws\x18\x0c \x01(\x0b\x32,.doublecloud.network.v1.AwsExternalResourcesH\x00R\x03\x61ws\x12@\n\x03gcp\x18\x0e \x01(\x0b\x32,.doublecloud.network.v1.GcpExternalResourcesH\x00R\x03gcp\x12\x1f\n\x0bis_external\x18\r \x01(\x08R\nisExternal\"\x9a\x01\n\rNetworkStatus\x12\x1a\n\x16NETWORK_STATUS_INVALID\x10\x00\x12\x1b\n\x17NETWORK_STATUS_CREATING\x10\x01\x12\x19\n\x15NETWORK_STATUS_ACTIVE\x10\x02\x12\x1b\n\x17NETWORK_STATUS_DELETING\x10\x03\x12\x18\n\x14NETWORK_STATUS_ERROR\x10\x04\x42\x14\n\x12\x65xternal_resources\"\xfc\x02\n\x14\x41wsExternalResources\x12\x15\n\x06vpc_id\x18\x01 \x01(\tR\x05vpcId\x12;\n\naccount_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\taccountId\x12>\n\x0ciam_role_arn\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\niamRoleArn\x12\x37\n\x08stack_id\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x07stackId\x12L\n\x13\x63\x66_template_version\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x11\x63\x66TemplateVersion\x12\x43\n\x0fprivate_subnets\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x0eprivateSubnetsJ\x04\x08\x02\x10\x04\"\xb7\x02\n\x14GcpExternalResources\x12?\n\x0cproject_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x0bprojectName\x12P\n\x15service_account_email\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x13serviceAccountEmail\x12?\n\x0cnetwork_name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x0bnetworkName\x12\x45\n\x0fsubnetwork_name\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x0esubnetworkNameJ\x04\x08\x01\x10\x02\x42\x43ZAgithub.com/doublecloud/go-genproto/doublecloud/network/v1;networkb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.network.v1.network_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/doublecloud/go-genproto/doublecloud/network/v1;network'
  _globals['_NETWORK']._serialized_start=130
  _globals['_NETWORK']._serialized_end=893
  _globals['_NETWORK_NETWORKSTATUS']._serialized_start=717
  _globals['_NETWORK_NETWORKSTATUS']._serialized_end=871
  _globals['_AWSEXTERNALRESOURCES']._serialized_start=896
  _globals['_AWSEXTERNALRESOURCES']._serialized_end=1276
  _globals['_GCPEXTERNALRESOURCES']._serialized_start=1279
  _globals['_GCPEXTERNALRESOURCES']._serialized_end=1590
# @@protoc_insertion_point(module_scope)
