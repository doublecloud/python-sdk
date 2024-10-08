# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/network/v1/network_service.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.network.v1 import network_pb2 as doublecloud_dot_network_dot_v1_dot_network__pb2
from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2
from doublecloud.v1 import paging_pb2 as doublecloud_dot_v1_dot_paging__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,doublecloud/network/v1/network_service.proto\x12\x16\x64oublecloud.network.v1\x1a$doublecloud/network/v1/network.proto\x1a\x1e\x64oublecloud/v1/operation.proto\x1a\x1b\x64oublecloud/v1/paging.proto\x1a\x1egoogle/protobuf/wrappers.proto\"2\n\x11GetNetworkRequest\x12\x1d\n\nnetwork_id\x18\x01 \x01(\tR\tnetworkId\"\xb7\x03\n\x13ListNetworksRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12.\n\x06paging\x18\x02 \x01(\x0b\x32\x16.doublecloud.v1.PagingR\x06paging\x12J\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x32.doublecloud.network.v1.ListNetworksRequest.FilterR\x06\x66ilter\x1a\x84\x02\n\x06\x46ilter\x12;\n\ncloud_type\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\tcloudType\x12\x39\n\tregion_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x08regionId\x12\x45\n\x06status\x18\x03 \x01(\x0e\x32-.doublecloud.network.v1.Network.NetworkStatusR\x06status\x12;\n\x0bis_external\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\nisExternal\"\x8a\x01\n\x14ListNetworksResponse\x12;\n\x08networks\x18\x01 \x03(\x0b\x32\x1f.doublecloud.network.v1.NetworkR\x08networks\x12\x35\n\tnext_page\x18\x02 \x01(\x0b\x32\x18.doublecloud.v1.NextPageR\x08nextPage\"\xcf\x01\n\x14\x43reateNetworkRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x1d\n\ncloud_type\x18\x02 \x01(\tR\tcloudType\x12\x1b\n\tregion_id\x18\x03 \x01(\tR\x08regionId\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12&\n\x0fipv4_cidr_block\x18\x06 \x01(\tR\ripv4CidrBlock\"5\n\x14\x44\x65leteNetworkRequest\x12\x1d\n\nnetwork_id\x18\x01 \x01(\tR\tnetworkId\"\x80\x02\n\x14ImportNetworkRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12?\n\x03\x61ws\x18\x04 \x01(\x0b\x32+.doublecloud.network.v1.ImportAWSVPCRequestH\x00R\x03\x61ws\x12H\n\x06google\x18\x05 \x01(\x0b\x32..doublecloud.network.v1.ImportGoogleVPCRequestH\x00R\x06googleB\x08\n\x06params\"\xe8\x01\n\x13ImportAWSVPCRequest\x12\x15\n\x06vpc_id\x18\x01 \x01(\tR\x05vpcId\x12\x1b\n\tregion_id\x18\x02 \x01(\tR\x08regionId\x12\x1d\n\naccount_id\x18\x03 \x01(\tR\taccountId\x12 \n\x0ciam_role_arn\x18\x04 \x01(\tR\niamRoleArn\x12\x19\n\x08stack_id\x18\x05 \x01(\tR\x07stackId\x12\x18\n\x07version\x18\x06 \x01(\tR\x07version\x12\'\n\x0fprivate_subnets\x18\x07 \x01(\x08R\x0eprivateSubnets\"\xd8\x01\n\x16ImportGoogleVPCRequest\x12\x32\n\x15service_account_email\x18\x01 \x01(\tR\x13serviceAccountEmail\x12!\n\x0cproject_name\x18\x02 \x01(\tR\x0bprojectName\x12!\n\x0cnetwork_name\x18\x03 \x01(\tR\x0bnetworkName\x12\x1b\n\tregion_id\x18\x04 \x01(\tR\x08regionId\x12\'\n\x0fsubnetwork_name\x18\x05 \x01(\tR\x0esubnetworkName2\xbf\x03\n\x0eNetworkService\x12Q\n\x03Get\x12).doublecloud.network.v1.GetNetworkRequest\x1a\x1f.doublecloud.network.v1.Network\x12\x61\n\x04List\x12+.doublecloud.network.v1.ListNetworksRequest\x1a,.doublecloud.network.v1.ListNetworksResponse\x12Q\n\x06\x43reate\x12,.doublecloud.network.v1.CreateNetworkRequest\x1a\x19.doublecloud.v1.Operation\x12Q\n\x06\x44\x65lete\x12,.doublecloud.network.v1.DeleteNetworkRequest\x1a\x19.doublecloud.v1.Operation\x12Q\n\x06Import\x12,.doublecloud.network.v1.ImportNetworkRequest\x1a\x19.doublecloud.v1.OperationBCZAgithub.com/doublecloud/go-genproto/doublecloud/network/v1;networkb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.network.v1.network_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/doublecloud/go-genproto/doublecloud/network/v1;network'
  _globals['_GETNETWORKREQUEST']._serialized_start=203
  _globals['_GETNETWORKREQUEST']._serialized_end=253
  _globals['_LISTNETWORKSREQUEST']._serialized_start=256
  _globals['_LISTNETWORKSREQUEST']._serialized_end=695
  _globals['_LISTNETWORKSREQUEST_FILTER']._serialized_start=435
  _globals['_LISTNETWORKSREQUEST_FILTER']._serialized_end=695
  _globals['_LISTNETWORKSRESPONSE']._serialized_start=698
  _globals['_LISTNETWORKSRESPONSE']._serialized_end=836
  _globals['_CREATENETWORKREQUEST']._serialized_start=839
  _globals['_CREATENETWORKREQUEST']._serialized_end=1046
  _globals['_DELETENETWORKREQUEST']._serialized_start=1048
  _globals['_DELETENETWORKREQUEST']._serialized_end=1101
  _globals['_IMPORTNETWORKREQUEST']._serialized_start=1104
  _globals['_IMPORTNETWORKREQUEST']._serialized_end=1360
  _globals['_IMPORTAWSVPCREQUEST']._serialized_start=1363
  _globals['_IMPORTAWSVPCREQUEST']._serialized_end=1595
  _globals['_IMPORTGOOGLEVPCREQUEST']._serialized_start=1598
  _globals['_IMPORTGOOGLEVPCREQUEST']._serialized_end=1814
  _globals['_NETWORKSERVICE']._serialized_start=1817
  _globals['_NETWORKSERVICE']._serialized_end=2264
# @@protoc_insertion_point(module_scope)
