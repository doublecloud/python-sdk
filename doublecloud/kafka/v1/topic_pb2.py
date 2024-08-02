# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/kafka/v1/topic.proto
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
    'doublecloud/kafka/v1/topic.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n doublecloud/kafka/v1/topic.proto\x12\x14\x64oublecloud.kafka.v1\x1a\x1egoogle/protobuf/wrappers.proto\"\x8a\x03\n\x05Topic\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\ncluster_id\x18\x02 \x01(\tR\tclusterId\x12;\n\npartitions\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\npartitions\x12J\n\x12replication_factor\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x11replicationFactor\x12N\n\x10topic_config_2_8\x18\x05 \x01(\x0b\x32#.doublecloud.kafka.v1.TopicConfig28H\x00R\rtopicConfig28\x12J\n\x0etopic_config_3\x18\x07 \x01(\x0b\x32\".doublecloud.kafka.v1.TopicConfig3H\x00R\x0ctopicConfig3\x12\x13\n\x05is_ha\x18\x08 \x01(\x08R\x04isHaB\x0e\n\x0ctopic_configJ\x04\x08\x06\x10\x07\"\xda\x02\n\tTopicSpec\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12;\n\npartitions\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\npartitions\x12J\n\x12replication_factor\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x11replicationFactor\x12N\n\x10topic_config_2_8\x18\x04 \x01(\x0b\x32#.doublecloud.kafka.v1.TopicConfig28H\x00R\rtopicConfig28\x12J\n\x0etopic_config_3\x18\x06 \x01(\x0b\x32\".doublecloud.kafka.v1.TopicConfig3H\x00R\x0ctopicConfig3B\x0e\n\x0ctopic_configJ\x04\x08\x05\x10\x06\"\x85\x06\n\rTopicConfig28\x12X\n\x0e\x63leanup_policy\x18\x01 \x01(\x0e\x32\x31.doublecloud.kafka.v1.TopicConfig28.CleanupPolicyR\rcleanupPolicy\x12^\n\x10\x63ompression_type\x18\x02 \x01(\x0e\x32\x33.doublecloud.kafka.v1.TopicConfig28.CompressionTypeR\x0f\x63ompressionType\x12\x44\n\x0fretention_bytes\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0eretentionBytes\x12>\n\x0cretention_ms\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0bretentionMs\x12G\n\x11max_message_bytes\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0fmaxMessageBytes\"\x89\x01\n\rCleanupPolicy\x12\x1a\n\x16\x43LEANUP_POLICY_INVALID\x10\x00\x12\x19\n\x15\x43LEANUP_POLICY_DELETE\x10\x01\x12\x1a\n\x16\x43LEANUP_POLICY_COMPACT\x10\x02\x12%\n!CLEANUP_POLICY_COMPACT_AND_DELETE\x10\x03\"\xde\x01\n\x0f\x43ompressionType\x12\x1c\n\x18\x43OMPRESSION_TYPE_INVALID\x10\x00\x12!\n\x1d\x43OMPRESSION_TYPE_UNCOMPRESSED\x10\x01\x12\x19\n\x15\x43OMPRESSION_TYPE_ZSTD\x10\x02\x12\x18\n\x14\x43OMPRESSION_TYPE_LZ4\x10\x03\x12\x1b\n\x17\x43OMPRESSION_TYPE_SNAPPY\x10\x04\x12\x19\n\x15\x43OMPRESSION_TYPE_GZIP\x10\x05\x12\x1d\n\x19\x43OMPRESSION_TYPE_PRODUCER\x10\x06\"\x82\x06\n\x0cTopicConfig3\x12W\n\x0e\x63leanup_policy\x18\x01 \x01(\x0e\x32\x30.doublecloud.kafka.v1.TopicConfig3.CleanupPolicyR\rcleanupPolicy\x12]\n\x10\x63ompression_type\x18\x02 \x01(\x0e\x32\x32.doublecloud.kafka.v1.TopicConfig3.CompressionTypeR\x0f\x63ompressionType\x12\x44\n\x0fretention_bytes\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0eretentionBytes\x12>\n\x0cretention_ms\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0bretentionMs\x12G\n\x11max_message_bytes\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0fmaxMessageBytes\"\x89\x01\n\rCleanupPolicy\x12\x1a\n\x16\x43LEANUP_POLICY_INVALID\x10\x00\x12\x19\n\x15\x43LEANUP_POLICY_DELETE\x10\x01\x12\x1a\n\x16\x43LEANUP_POLICY_COMPACT\x10\x02\x12%\n!CLEANUP_POLICY_COMPACT_AND_DELETE\x10\x03\"\xde\x01\n\x0f\x43ompressionType\x12\x1c\n\x18\x43OMPRESSION_TYPE_INVALID\x10\x00\x12!\n\x1d\x43OMPRESSION_TYPE_UNCOMPRESSED\x10\x01\x12\x19\n\x15\x43OMPRESSION_TYPE_ZSTD\x10\x02\x12\x18\n\x14\x43OMPRESSION_TYPE_LZ4\x10\x03\x12\x1b\n\x17\x43OMPRESSION_TYPE_SNAPPY\x10\x04\x12\x19\n\x15\x43OMPRESSION_TYPE_GZIP\x10\x05\x12\x1d\n\x19\x43OMPRESSION_TYPE_PRODUCER\x10\x06\x42?Z=github.com/doublecloud/go-genproto/doublecloud/kafka/v1;kafkab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.kafka.v1.topic_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/doublecloud/go-genproto/doublecloud/kafka/v1;kafka'
  _globals['_TOPIC']._serialized_start=91
  _globals['_TOPIC']._serialized_end=485
  _globals['_TOPICSPEC']._serialized_start=488
  _globals['_TOPICSPEC']._serialized_end=834
  _globals['_TOPICCONFIG28']._serialized_start=837
  _globals['_TOPICCONFIG28']._serialized_end=1610
  _globals['_TOPICCONFIG28_CLEANUPPOLICY']._serialized_start=1248
  _globals['_TOPICCONFIG28_CLEANUPPOLICY']._serialized_end=1385
  _globals['_TOPICCONFIG28_COMPRESSIONTYPE']._serialized_start=1388
  _globals['_TOPICCONFIG28_COMPRESSIONTYPE']._serialized_end=1610
  _globals['_TOPICCONFIG3']._serialized_start=1613
  _globals['_TOPICCONFIG3']._serialized_end=2383
  _globals['_TOPICCONFIG3_CLEANUPPOLICY']._serialized_start=1248
  _globals['_TOPICCONFIG3_CLEANUPPOLICY']._serialized_end=1385
  _globals['_TOPICCONFIG3_COMPRESSIONTYPE']._serialized_start=1388
  _globals['_TOPICCONFIG3_COMPRESSIONTYPE']._serialized_end=1610
# @@protoc_insertion_point(module_scope)
