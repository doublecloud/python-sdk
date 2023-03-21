# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/network/v1/network_connection.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/doublecloud/network/v1/network_connection.proto\x12\x16\x64oublecloud.network.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xff\x04\n\x11NetworkConnection\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\nnetwork_id\x18\x02 \x01(\tR\tnetworkId\x12\x44\n\x03\x61ws\x18\x04 \x01(\x0b\x32\x30.doublecloud.network.v1.AWSNetworkConnectionInfoH\x00R\x03\x61ws\x12;\n\x0b\x63reate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12 \n\x0b\x64\x65scription\x18\x08 \x01(\tR\x0b\x64\x65scription\x12Y\n\x06status\x18\t \x01(\x0e\x32\x41.doublecloud.network.v1.NetworkConnection.NetworkConnectionStatusR\x06status\x12#\n\rstatus_reason\x18\n \x01(\tR\x0cstatusReason\"\x82\x02\n\x17NetworkConnectionStatus\x12%\n!NETWORK_CONNECTION_STATUS_INVALID\x10\x00\x12&\n\"NETWORK_CONNECTION_STATUS_CREATING\x10\x01\x12%\n!NETWORK_CONNECTION_STATUS_PENDING\x10\x02\x12$\n NETWORK_CONNECTION_STATUS_ACTIVE\x10\x03\x12&\n\"NETWORK_CONNECTION_STATUS_DELETING\x10\x04\x12#\n\x1fNETWORK_CONNECTION_STATUS_ERROR\x10\x05\x42\x11\n\x0f\x63onnection_info\"w\n\x18\x41WSNetworkConnectionInfo\x12S\n\x07peering\x18\x01 \x01(\x0b\x32\x37.doublecloud.network.v1.AWSNetworkConnectionPeeringInfoH\x00R\x07peeringB\x06\n\x04type\"\xe6\x02\n\x1f\x41WSNetworkConnectionPeeringInfo\x12\x15\n\x06vpc_id\x18\x01 \x01(\tR\x05vpcId\x12\x1d\n\naccount_id\x18\x02 \x01(\tR\taccountId\x12\x1b\n\tregion_id\x18\x03 \x01(\tR\x08regionId\x12&\n\x0fipv4_cidr_block\x18\x04 \x01(\tR\ripv4CidrBlock\x12&\n\x0fipv6_cidr_block\x18\x05 \x01(\tR\ripv6CidrBlock\x12\x32\n\x15peering_connection_id\x18\x06 \x01(\tR\x13peeringConnectionId\x12\x35\n\x17managed_ipv4_cidr_block\x18\x07 \x01(\tR\x14managedIpv4CidrBlock\x12\x35\n\x17managed_ipv6_cidr_block\x18\x08 \x01(\tR\x14managedIpv6CidrBlockB;Z9github.com/doublecloud/api/doublecloud/network/v1;networkb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.network.v1.network_connection_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z9github.com/doublecloud/api/doublecloud/network/v1;network'
  _globals['_NETWORKCONNECTION']._serialized_start=109
  _globals['_NETWORKCONNECTION']._serialized_end=748
  _globals['_NETWORKCONNECTION_NETWORKCONNECTIONSTATUS']._serialized_start=471
  _globals['_NETWORKCONNECTION_NETWORKCONNECTIONSTATUS']._serialized_end=729
  _globals['_AWSNETWORKCONNECTIONINFO']._serialized_start=750
  _globals['_AWSNETWORKCONNECTIONINFO']._serialized_end=869
  _globals['_AWSNETWORKCONNECTIONPEERINGINFO']._serialized_start=872
  _globals['_AWSNETWORKCONNECTIONPEERINGINFO']._serialized_end=1230
# @@protoc_insertion_point(module_scope)
