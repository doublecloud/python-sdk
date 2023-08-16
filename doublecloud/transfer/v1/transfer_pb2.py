# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/transfer/v1/transfer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.transfer.v1 import endpoint_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&doublecloud/transfer/v1/transfer.proto\x12\x17\x64oublecloud.transfer.v1\x1a&doublecloud/transfer/v1/endpoint.proto\"\xfd\x03\n\x08Transfer\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\nproject_id\x18\x02 \x01(\tR\tprojectId\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12\x45\n\x06labels\x18\x06 \x03(\x0b\x32-.doublecloud.transfer.v1.Transfer.LabelsEntryR\x06labels\x12\x39\n\x06source\x18\x07 \x01(\x0b\x32!.doublecloud.transfer.v1.EndpointR\x06source\x12\x39\n\x06target\x18\x08 \x01(\x0b\x32!.doublecloud.transfer.v1.EndpointR\x06target\x12?\n\x06status\x18\n \x01(\x0e\x32\'.doublecloud.transfer.v1.TransferStatusR\x06status\x12\x39\n\x04type\x18\x0c \x01(\x0e\x32%.doublecloud.transfer.v1.TransferTypeR\x04type\x12\x18\n\x07warning\x18\x0f \x01(\tR\x07warning\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01*p\n\x0cTransferType\x12\x1d\n\x19TRANSFER_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16SNAPSHOT_AND_INCREMENT\x10\x01\x12\x11\n\rSNAPSHOT_ONLY\x10\x02\x12\x12\n\x0eINCREMENT_ONLY\x10\x03*\x9b\x01\n\x0eTransferStatus\x12\x1f\n\x1bTRANSFER_STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0b\n\x07\x43REATED\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\x0c\n\x08STOPPING\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\t\n\x05\x45RROR\x10\x06\x12\x10\n\x0cSNAPSHOTTING\x10\x07\x12\x08\n\x04\x44ONE\x10\x08\x42\x45ZCgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1;transferb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.transfer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZCgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1;transfer'
  _TRANSFER_LABELSENTRY._options = None
  _TRANSFER_LABELSENTRY._serialized_options = b'8\001'
  _globals['_TRANSFERTYPE']._serialized_start=619
  _globals['_TRANSFERTYPE']._serialized_end=731
  _globals['_TRANSFERSTATUS']._serialized_start=734
  _globals['_TRANSFERSTATUS']._serialized_end=889
  _globals['_TRANSFER']._serialized_start=108
  _globals['_TRANSFER']._serialized_end=617
  _globals['_TRANSFER_LABELSENTRY']._serialized_start=560
  _globals['_TRANSFER_LABELSENTRY']._serialized_end=617
# @@protoc_insertion_point(module_scope)
