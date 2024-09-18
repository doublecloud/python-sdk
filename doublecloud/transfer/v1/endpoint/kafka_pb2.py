# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/transfer/v1/endpoint/kafka.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.transfer.v1.endpoint import common_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_common__pb2
from doublecloud.transfer.v1.endpoint import parsers_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_parsers__pb2
from doublecloud.transfer.v1.endpoint import serializers_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_serializers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,doublecloud/transfer/v1/endpoint/kafka.proto\x12 doublecloud.transfer.v1.endpoint\x1a-doublecloud/transfer/v1/endpoint/common.proto\x1a.doublecloud/transfer/v1/endpoint/parsers.proto\x1a\x32\x64oublecloud/transfer/v1/endpoint/serializers.proto\"\x9a\x01\n\x16KafkaConnectionOptions\x12\x1f\n\ncluster_id\x18\x01 \x01(\tH\x00R\tclusterId\x12Q\n\non_premise\x18\x02 \x01(\x0b\x32\x30.doublecloud.transfer.v1.endpoint.OnPremiseKafkaH\x00R\tonPremiseB\x0c\n\nconnection\"}\n\x0eOnPremiseKafka\x12\x1f\n\x0b\x62roker_urls\x18\x01 \x03(\tR\nbrokerUrls\x12\x44\n\x08tls_mode\x18\x05 \x01(\x0b\x32).doublecloud.transfer.v1.endpoint.TLSModeR\x07tlsModeJ\x04\x08\x02\x10\x05\"\xa7\x01\n\tKafkaAuth\x12I\n\x04sasl\x18\x01 \x01(\x0b\x32\x33.doublecloud.transfer.v1.endpoint.KafkaSaslSecurityH\x00R\x04sasl\x12\x43\n\x07no_auth\x18\x02 \x01(\x0b\x32(.doublecloud.transfer.v1.endpoint.NoAuthH\x00R\x06noAuthB\n\n\x08security\"\xc3\x01\n\x11KafkaSaslSecurity\x12\x12\n\x04user\x18\x01 \x01(\tR\x04user\x12N\n\tmechanism\x18\x03 \x01(\x0e\x32\x30.doublecloud.transfer.v1.endpoint.KafkaMechanismR\tmechanism\x12\x44\n\x08password\x18\x04 \x01(\x0b\x32(.doublecloud.transfer.v1.endpoint.SecretR\x08passwordJ\x04\x08\x02\x10\x03\"\xba\x02\n\x0bKafkaSource\x12X\n\nconnection\x18\x01 \x01(\x0b\x32\x38.doublecloud.transfer.v1.endpoint.KafkaConnectionOptionsR\nconnection\x12?\n\x04\x61uth\x18\x02 \x01(\x0b\x32+.doublecloud.transfer.v1.endpoint.KafkaAuthR\x04\x61uth\x12!\n\ntopic_name\x18\x04 \x01(\tB\x02\x18\x01R\ttopicName\x12@\n\x06parser\x18\x07 \x01(\x0b\x32(.doublecloud.transfer.v1.endpoint.ParserR\x06parser\x12\x1f\n\x0btopic_names\x18\x08 \x03(\tR\ntopicNamesJ\x04\x08\x03\x10\x04J\x04\x08\x05\x10\x07\"\xbd\x03\n\x0bKafkaTarget\x12X\n\nconnection\x18\x01 \x01(\x0b\x32\x38.doublecloud.transfer.v1.endpoint.KafkaConnectionOptionsR\nconnection\x12?\n\x04\x61uth\x18\x02 \x01(\x0b\x32+.doublecloud.transfer.v1.endpoint.KafkaAuthR\x04\x61uth\x12\x61\n\x0etopic_settings\x18\x07 \x01(\x0b\x32:.doublecloud.transfer.v1.endpoint.KafkaTargetTopicSettingsR\rtopicSettings\x12L\n\nserializer\x18\x08 \x01(\x0b\x32,.doublecloud.transfer.v1.endpoint.SerializerR\nserializer\x12\\\n\x0b\x63ompression\x18\t \x01(\x0e\x32:.doublecloud.transfer.v1.endpoint.KafkaCompressionEncodingR\x0b\x63ompressionJ\x04\x08\x03\x10\x07\"\x83\x02\n\x18KafkaTargetTopicSettings\x12J\n\x05topic\x18\x01 \x01(\x0b\x32\x32.doublecloud.transfer.v1.endpoint.KafkaTargetTopicH\x00R\x05topic\x12#\n\x0ctopic_prefix\x18\x02 \x01(\tH\x00R\x0btopicPrefix\x12\x64\n\x14topic_config_entries\x18\x03 \x03(\x0b\x32\x32.doublecloud.transfer.v1.endpoint.TopicConfigEntryR\x12topicConfigEntriesB\x10\n\x0etopic_settings\"U\n\x10KafkaTargetTopic\x12\x1d\n\ntopic_name\x18\x01 \x01(\tR\ttopicName\x12\"\n\rsave_tx_order\x18\x02 \x01(\x08R\x0bsaveTxOrder\"V\n\x10TopicConfigEntry\x12\x1f\n\x0b\x63onfig_name\x18\x01 \x01(\tR\nconfigName\x12!\n\x0c\x63onfig_value\x18\x02 \x01(\tR\x0b\x63onfigValue*i\n\x0eKafkaMechanism\x12\x1f\n\x1bKAFKA_MECHANISM_UNSPECIFIED\x10\x00\x12\x1a\n\x16KAFKA_MECHANISM_SHA256\x10\x01\x12\x1a\n\x16KAFKA_MECHANISM_SHA512\x10\x02*\xdb\x01\n\x18KafkaCompressionEncoding\x12*\n&KAFKA_COMPRESSION_ENCODING_UNSPECIFIED\x10\x00\x12#\n\x1fKAFKA_COMPRESSION_ENCODING_GZIP\x10\x01\x12%\n!KAFKA_COMPRESSION_ENCODING_SNAPPY\x10\x02\x12\"\n\x1eKAFKA_COMPRESSION_ENCODING_LZ4\x10\x03\x12#\n\x1fKAFKA_COMPRESSION_ENCODING_ZSTD\x10\x04\x42NZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.kafka_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpoint'
  _globals['_KAFKASOURCE'].fields_by_name['topic_name']._options = None
  _globals['_KAFKASOURCE'].fields_by_name['topic_name']._serialized_options = b'\030\001'
  _globals['_KAFKAMECHANISM']._serialized_start=2083
  _globals['_KAFKAMECHANISM']._serialized_end=2188
  _globals['_KAFKACOMPRESSIONENCODING']._serialized_start=2191
  _globals['_KAFKACOMPRESSIONENCODING']._serialized_end=2410
  _globals['_KAFKACONNECTIONOPTIONS']._serialized_start=230
  _globals['_KAFKACONNECTIONOPTIONS']._serialized_end=384
  _globals['_ONPREMISEKAFKA']._serialized_start=386
  _globals['_ONPREMISEKAFKA']._serialized_end=511
  _globals['_KAFKAAUTH']._serialized_start=514
  _globals['_KAFKAAUTH']._serialized_end=681
  _globals['_KAFKASASLSECURITY']._serialized_start=684
  _globals['_KAFKASASLSECURITY']._serialized_end=879
  _globals['_KAFKASOURCE']._serialized_start=882
  _globals['_KAFKASOURCE']._serialized_end=1196
  _globals['_KAFKATARGET']._serialized_start=1199
  _globals['_KAFKATARGET']._serialized_end=1644
  _globals['_KAFKATARGETTOPICSETTINGS']._serialized_start=1647
  _globals['_KAFKATARGETTOPICSETTINGS']._serialized_end=1906
  _globals['_KAFKATARGETTOPIC']._serialized_start=1908
  _globals['_KAFKATARGETTOPIC']._serialized_end=1993
  _globals['_TOPICCONFIGENTRY']._serialized_start=1995
  _globals['_TOPICCONFIGENTRY']._serialized_end=2081
# @@protoc_insertion_point(module_scope)
