# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/transfer/v1/endpoint/mongo.proto
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
    'doublecloud/transfer/v1/endpoint/mongo.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.transfer.v1.endpoint import common_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,doublecloud/transfer/v1/endpoint/mongo.proto\x12 doublecloud.transfer.v1.endpoint\x1a-doublecloud/transfer/v1/endpoint/common.proto\"\x8d\x01\n\x08SrvMongo\x12\x1a\n\x08hostname\x18\x01 \x01(\tR\x08hostname\x12\x1f\n\x0breplica_set\x18\x02 \x01(\tR\nreplicaSet\x12\x44\n\x08tls_mode\x18\x03 \x01(\x0b\x32).doublecloud.transfer.v1.endpoint.TLSModeR\x07tlsMode\"\xa7\x01\n\x0eOnPremiseMongo\x12\x14\n\x05hosts\x18\x01 \x03(\tR\x05hosts\x12\x12\n\x04port\x18\x02 \x01(\x03R\x04port\x12\x1f\n\x0breplica_set\x18\x05 \x01(\tR\nreplicaSet\x12\x44\n\x08tls_mode\x18\x06 \x01(\x0b\x32).doublecloud.transfer.v1.endpoint.TLSModeR\x07tlsModeJ\x04\x08\x03\x10\x05\"\xb7\x02\n\x16MongoConnectionOptions\x12Q\n\non_premise\x18\x02 \x01(\x0b\x32\x30.doublecloud.transfer.v1.endpoint.OnPremiseMongoH\x00R\tonPremise\x12>\n\x03srv\x18\x06 \x01(\x0b\x32*.doublecloud.transfer.v1.endpoint.SrvMongoH\x00R\x03srv\x12\x12\n\x04user\x18\x03 \x01(\tR\x04user\x12\x44\n\x08password\x18\x04 \x01(\x0b\x32(.doublecloud.transfer.v1.endpoint.SecretR\x08password\x12\x1f\n\x0b\x61uth_source\x18\x05 \x01(\tR\nauthSourceB\t\n\x07\x61\x64\x64ressJ\x04\x08\x01\x10\x02\"\x90\x01\n\x0fMongoConnection\x12i\n\x12\x63onnection_options\x18\x03 \x01(\x0b\x32\x38.doublecloud.transfer.v1.endpoint.MongoConnectionOptionsH\x00R\x11\x63onnectionOptionsB\x0c\n\nconnectionJ\x04\x08\x01\x10\x03\"_\n\x0fMongoCollection\x12#\n\rdatabase_name\x18\x01 \x01(\tR\x0c\x64\x61tabaseName\x12\'\n\x0f\x63ollection_name\x18\x02 \x01(\tR\x0e\x63ollectionName\"\xdb\x02\n\x0bMongoSource\x12Q\n\nconnection\x18\x01 \x01(\x0b\x32\x31.doublecloud.transfer.v1.endpoint.MongoConnectionR\nconnection\x12S\n\x0b\x63ollections\x18\x06 \x03(\x0b\x32\x31.doublecloud.transfer.v1.endpoint.MongoCollectionR\x0b\x63ollections\x12\x64\n\x14\x65xcluded_collections\x18\x07 \x03(\x0b\x32\x31.doublecloud.transfer.v1.endpoint.MongoCollectionR\x13\x65xcludedCollections\x12\x38\n\x18secondary_preferred_mode\x18\x08 \x01(\x08R\x16secondaryPreferredModeJ\x04\x08\x02\x10\x06\"\xda\x01\n\x0bMongoTarget\x12Q\n\nconnection\x18\x01 \x01(\x0b\x32\x31.doublecloud.transfer.v1.endpoint.MongoConnectionR\nconnection\x12\x1a\n\x08\x64\x61tabase\x18\x02 \x01(\tR\x08\x64\x61tabase\x12V\n\x0e\x63leanup_policy\x18\x06 \x01(\x0e\x32/.doublecloud.transfer.v1.endpoint.CleanupPolicyR\rcleanupPolicyJ\x04\x08\x03\x10\x06\x42NZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.mongo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpoint'
  _globals['_SRVMONGO']._serialized_start=130
  _globals['_SRVMONGO']._serialized_end=271
  _globals['_ONPREMISEMONGO']._serialized_start=274
  _globals['_ONPREMISEMONGO']._serialized_end=441
  _globals['_MONGOCONNECTIONOPTIONS']._serialized_start=444
  _globals['_MONGOCONNECTIONOPTIONS']._serialized_end=755
  _globals['_MONGOCONNECTION']._serialized_start=758
  _globals['_MONGOCONNECTION']._serialized_end=902
  _globals['_MONGOCOLLECTION']._serialized_start=904
  _globals['_MONGOCOLLECTION']._serialized_end=999
  _globals['_MONGOSOURCE']._serialized_start=1002
  _globals['_MONGOSOURCE']._serialized_end=1349
  _globals['_MONGOTARGET']._serialized_start=1352
  _globals['_MONGOTARGET']._serialized_end=1570
# @@protoc_insertion_point(module_scope)
