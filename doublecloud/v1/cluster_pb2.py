# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/v1/cluster.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x64oublecloud/v1/cluster.proto\x12\x0e\x64oublecloud.v1\x1a\x1egoogle/protobuf/wrappers.proto\"\xb8\x04\n\x06\x41\x63\x63\x65ss\x12N\n\x10ipv4_cidr_blocks\x18\x01 \x01(\x0b\x32$.doublecloud.v1.Access.CidrBlockListR\x0eipv4CidrBlocks\x12N\n\x10ipv6_cidr_blocks\x18\x02 \x01(\x0b\x32$.doublecloud.v1.Access.CidrBlockListR\x0eipv6CidrBlocks\x12K\n\rdata_services\x18\x03 \x01(\x0b\x32&.doublecloud.v1.Access.DataServiceListR\x0c\x64\x61taServices\x1a\x43\n\tCidrBlock\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x1aI\n\rCidrBlockList\x12\x38\n\x06values\x18\x01 \x03(\x0b\x32 .doublecloud.v1.Access.CidrBlockR\x06values\x1aM\n\x0f\x44\x61taServiceList\x12:\n\x06values\x18\x01 \x03(\x0e\x32\".doublecloud.v1.Access.DataServiceR\x06values\"b\n\x0b\x44\x61taService\x12\x18\n\x14\x44\x41TA_SERVICE_INVALID\x10\x00\x12\x1e\n\x1a\x44\x41TA_SERVICE_VISUALIZATION\x10\x01\x12\x19\n\x15\x44\x41TA_SERVICE_TRANSFER\x10\x02\"J\n\x0e\x44\x61taEncryption\x12\x38\n\x07\x65nabled\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\x02\x18\x01R\x07\x65nabled*\xc1\x02\n\rClusterStatus\x12\x1a\n\x16\x43LUSTER_STATUS_INVALID\x10\x00\x12\x18\n\x14\x43LUSTER_STATUS_ALIVE\x10\x01\x12\x1b\n\x17\x43LUSTER_STATUS_DEGRADED\x10\x02\x12\x17\n\x13\x43LUSTER_STATUS_DEAD\x10\x03\x12\x1a\n\x16\x43LUSTER_STATUS_UNKNOWN\x10\x04\x12\x1b\n\x17\x43LUSTER_STATUS_CREATING\x10\x05\x12\x1b\n\x17\x43LUSTER_STATUS_UPDATING\x10\x06\x12\x1b\n\x17\x43LUSTER_STATUS_STOPPING\x10\x07\x12\x1a\n\x16\x43LUSTER_STATUS_STOPPED\x10\x08\x12\x1b\n\x17\x43LUSTER_STATUS_STARTING\x10\t\x12\x18\n\x14\x43LUSTER_STATUS_ERROR\x10\n*l\n\nHostStatus\x12\x17\n\x13HOST_STATUS_INVALID\x10\x00\x12\x15\n\x11HOST_STATUS_ALIVE\x10\x01\x12\x14\n\x10HOST_STATUS_DEAD\x10\x02\x12\x18\n\x14HOST_STATUS_DEGRADED\x10\x03\x42?Z=github.com/doublecloud/go-genproto/doublecloud/v1;doublecloudb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.v1.cluster_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/doublecloud/go-genproto/doublecloud/v1;doublecloud'
  _globals['_DATAENCRYPTION'].fields_by_name['enabled']._loaded_options = None
  _globals['_DATAENCRYPTION'].fields_by_name['enabled']._serialized_options = b'\030\001'
  _globals['_CLUSTERSTATUS']._serialized_start=728
  _globals['_CLUSTERSTATUS']._serialized_end=1049
  _globals['_HOSTSTATUS']._serialized_start=1051
  _globals['_HOSTSTATUS']._serialized_end=1159
  _globals['_ACCESS']._serialized_start=81
  _globals['_ACCESS']._serialized_end=649
  _globals['_ACCESS_CIDRBLOCK']._serialized_start=328
  _globals['_ACCESS_CIDRBLOCK']._serialized_end=395
  _globals['_ACCESS_CIDRBLOCKLIST']._serialized_start=397
  _globals['_ACCESS_CIDRBLOCKLIST']._serialized_end=470
  _globals['_ACCESS_DATASERVICELIST']._serialized_start=472
  _globals['_ACCESS_DATASERVICELIST']._serialized_end=549
  _globals['_ACCESS_DATASERVICE']._serialized_start=551
  _globals['_ACCESS_DATASERVICE']._serialized_end=649
  _globals['_DATAENCRYPTION']._serialized_start=651
  _globals['_DATAENCRYPTION']._serialized_end=725
# @@protoc_insertion_point(module_scope)
