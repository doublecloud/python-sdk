# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/transfer/v1/endpoint/serializers.proto
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
    'doublecloud/transfer/v1/endpoint/serializers.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2doublecloud/transfer/v1/endpoint/serializers.proto\x12 doublecloud.transfer.v1.endpoint\"\x10\n\x0eSerializerAuto\"\x10\n\x0eSerializerJSON\"E\n\x1b\x44\x65\x62\x65ziumSerializerParameter\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"\x88\x01\n\x12SerializerDebezium\x12r\n\x15serializer_parameters\x18\x01 \x03(\x0b\x32=.doublecloud.transfer.v1.endpoint.DebeziumSerializerParameterR\x14serializerParameters\"\xbd\x02\n\nSerializer\x12[\n\x0fserializer_auto\x18\x01 \x01(\x0b\x32\x30.doublecloud.transfer.v1.endpoint.SerializerAutoH\x00R\x0eserializerAuto\x12[\n\x0fserializer_json\x18\x02 \x01(\x0b\x32\x30.doublecloud.transfer.v1.endpoint.SerializerJSONH\x00R\x0eserializerJson\x12g\n\x13serializer_debezium\x18\x03 \x01(\x0b\x32\x34.doublecloud.transfer.v1.endpoint.SerializerDebeziumH\x00R\x12serializerDebeziumB\x0c\n\nserializerBNZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.serializers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpoint'
  _globals['_SERIALIZERAUTO']._serialized_start=88
  _globals['_SERIALIZERAUTO']._serialized_end=104
  _globals['_SERIALIZERJSON']._serialized_start=106
  _globals['_SERIALIZERJSON']._serialized_end=122
  _globals['_DEBEZIUMSERIALIZERPARAMETER']._serialized_start=124
  _globals['_DEBEZIUMSERIALIZERPARAMETER']._serialized_end=193
  _globals['_SERIALIZERDEBEZIUM']._serialized_start=196
  _globals['_SERIALIZERDEBEZIUM']._serialized_end=332
  _globals['_SERIALIZER']._serialized_start=335
  _globals['_SERIALIZER']._serialized_end=652
# @@protoc_insertion_point(module_scope)
