# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/transfer/v1/endpoint/clickhouse.proto
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
    'doublecloud/transfer/v1/endpoint/clickhouse.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from doublecloud.transfer.v1.endpoint import common_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1doublecloud/transfer/v1/endpoint/clickhouse.proto\x12 doublecloud.transfer.v1.endpoint\x1a\x1bgoogle/protobuf/empty.proto\x1a-doublecloud/transfer/v1/endpoint/common.proto\";\n\x0f\x43lickhouseShard\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05hosts\x18\x02 \x03(\tR\x05hosts\"\xf0\x01\n\x13OnPremiseClickhouse\x12I\n\x06shards\x18\x01 \x03(\x0b\x32\x31.doublecloud.transfer.v1.endpoint.ClickhouseShardR\x06shards\x12\x1b\n\thttp_port\x18\x03 \x01(\x03R\x08httpPort\x12\x1f\n\x0bnative_port\x18\x04 \x01(\x03R\nnativePort\x12\x44\n\x08tls_mode\x18\x08 \x01(\x0b\x32).doublecloud.transfer.v1.endpoint.TLSModeR\x07tlsModeJ\x04\x08\x02\x10\x03J\x04\x08\x05\x10\x08\"\xaa\x02\n\x1b\x43lickhouseConnectionOptions\x12V\n\non_premise\x18\x02 \x01(\x0b\x32\x35.doublecloud.transfer.v1.endpoint.OnPremiseClickhouseH\x00R\tonPremise\x12&\n\x0emdb_cluster_id\x18\x05 \x01(\tH\x00R\x0cmdbClusterId\x12\x12\n\x04user\x18\x06 \x01(\tR\x04user\x12\x44\n\x08password\x18\x07 \x01(\x0b\x32(.doublecloud.transfer.v1.endpoint.SecretR\x08password\x12\x1a\n\x08\x64\x61tabase\x18\x08 \x01(\tR\x08\x64\x61tabaseB\t\n\x07\x61\x64\x64ressJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x05\"\x94\x01\n\x14\x43lickhouseConnection\x12n\n\x12\x63onnection_options\x18\x01 \x01(\x0b\x32=.doublecloud.transfer.v1.endpoint.ClickhouseConnectionOptionsH\x00R\x11\x63onnectionOptionsB\x0c\n\nconnection\"\xd9\x05\n\x12\x43lickhouseSharding\x12r\n\x11\x63olumn_value_hash\x18\x01 \x01(\x0b\x32\x44.doublecloud.transfer.v1.endpoint.ClickhouseSharding.ColumnValueHashH\x00R\x0f\x63olumnValueHash\x12p\n\x0e\x63ustom_mapping\x18\x02 \x01(\x0b\x32G.doublecloud.transfer.v1.endpoint.ClickhouseSharding.ColumnValueMappingH\x00R\rcustomMapping\x12\x39\n\x0btransfer_id\x18\x03 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00R\ntransferId\x12\x39\n\x0bround_robin\x18\x04 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00R\nroundRobin\x1a\x32\n\x0f\x43olumnValueHash\x12\x1f\n\x0b\x63olumn_name\x18\x01 \x01(\tR\ncolumnName\x1a\xa6\x02\n\x12\x43olumnValueMapping\x12\x1f\n\x0b\x63olumn_name\x18\x01 \x01(\tR\ncolumnName\x12n\n\x07mapping\x18\x02 \x03(\x0b\x32T.doublecloud.transfer.v1.endpoint.ClickhouseSharding.ColumnValueMapping.ValueToShardR\x07mapping\x1a\x7f\n\x0cValueToShard\x12P\n\x0c\x63olumn_value\x18\x01 \x01(\x0b\x32-.doublecloud.transfer.v1.endpoint.ColumnValueR\x0b\x63olumnValue\x12\x1d\n\nshard_name\x18\x02 \x01(\tR\tshardNameB\n\n\x08sharding\"J\n\x1a\x43lickhouseMigrationOptions\x12&\n\x0f\x61\x64\x64_new_columns\x18\x12 \x01(\x08R\raddNewColumnsJ\x04\x08\x01\x10\x12\"b\n\x17\x43lickhouseInsertOptions\x12G\n materialized_views_ignore_errors\x18\x01 \x01(\x08R\x1dmaterializedViewsIgnoreErrors\"\xbe\x01\n\x10\x43lickhouseSource\x12V\n\nconnection\x18\x01 \x01(\x0b\x32\x36.doublecloud.transfer.v1.endpoint.ClickhouseConnectionR\nconnection\x12%\n\x0einclude_tables\x18\x07 \x03(\tR\rincludeTables\x12%\n\x0e\x65xclude_tables\x18\x08 \x03(\tR\rexcludeTablesJ\x04\x08\x02\x10\x07\"\x83\x05\n\x10\x43lickhouseTarget\x12V\n\nconnection\x18\x02 \x01(\x0b\x32\x36.doublecloud.transfer.v1.endpoint.ClickhouseConnectionR\nconnection\x12\x46\n\talt_names\x18\x11 \x03(\x0b\x32).doublecloud.transfer.v1.endpoint.AltNameR\x08\x61ltNames\x12i\n\x11migration_options\x18\x12 \x01(\x0b\x32<.doublecloud.transfer.v1.endpoint.ClickhouseMigrationOptionsR\x10migrationOptions\x12`\n\x0e\x63leanup_policy\x18\x15 \x01(\x0e\x32\x39.doublecloud.transfer.v1.endpoint.ClickhouseCleanupPolicyR\rcleanupPolicy\x12P\n\x08sharding\x18\x16 \x01(\x0b\x32\x34.doublecloud.transfer.v1.endpoint.ClickhouseShardingR\x08sharding\x12`\n\x0einsert_options\x18\x17 \x01(\x0b\x32\x39.doublecloud.transfer.v1.endpoint.ClickhouseInsertOptionsR\rinsertOptions\x12\x36\n\x17\x63lickhouse_cluster_name\x18\x32 \x01(\tR\x15\x63lickhouseClusterNameJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x11J\x04\x08\x13\x10\x15J\x04\x08\x18\x10\x32*\xb8\x01\n\x17\x43lickhouseCleanupPolicy\x12)\n%CLICKHOUSE_CLEANUP_POLICY_UNSPECIFIED\x10\x00\x12&\n\"CLICKHOUSE_CLEANUP_POLICY_DISABLED\x10\x01\x12\"\n\x1e\x43LICKHOUSE_CLEANUP_POLICY_DROP\x10\x02\x12&\n\"CLICKHOUSE_CLEANUP_POLICY_TRUNCATE\x10\x03\x42NZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.clickhouse_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpoint'
  _globals['_CLICKHOUSECLEANUPPOLICY']._serialized_start=2667
  _globals['_CLICKHOUSECLEANUPPOLICY']._serialized_end=2851
  _globals['_CLICKHOUSESHARD']._serialized_start=163
  _globals['_CLICKHOUSESHARD']._serialized_end=222
  _globals['_ONPREMISECLICKHOUSE']._serialized_start=225
  _globals['_ONPREMISECLICKHOUSE']._serialized_end=465
  _globals['_CLICKHOUSECONNECTIONOPTIONS']._serialized_start=468
  _globals['_CLICKHOUSECONNECTIONOPTIONS']._serialized_end=766
  _globals['_CLICKHOUSECONNECTION']._serialized_start=769
  _globals['_CLICKHOUSECONNECTION']._serialized_end=917
  _globals['_CLICKHOUSESHARDING']._serialized_start=920
  _globals['_CLICKHOUSESHARDING']._serialized_end=1649
  _globals['_CLICKHOUSESHARDING_COLUMNVALUEHASH']._serialized_start=1290
  _globals['_CLICKHOUSESHARDING_COLUMNVALUEHASH']._serialized_end=1340
  _globals['_CLICKHOUSESHARDING_COLUMNVALUEMAPPING']._serialized_start=1343
  _globals['_CLICKHOUSESHARDING_COLUMNVALUEMAPPING']._serialized_end=1637
  _globals['_CLICKHOUSESHARDING_COLUMNVALUEMAPPING_VALUETOSHARD']._serialized_start=1510
  _globals['_CLICKHOUSESHARDING_COLUMNVALUEMAPPING_VALUETOSHARD']._serialized_end=1637
  _globals['_CLICKHOUSEMIGRATIONOPTIONS']._serialized_start=1651
  _globals['_CLICKHOUSEMIGRATIONOPTIONS']._serialized_end=1725
  _globals['_CLICKHOUSEINSERTOPTIONS']._serialized_start=1727
  _globals['_CLICKHOUSEINSERTOPTIONS']._serialized_end=1825
  _globals['_CLICKHOUSESOURCE']._serialized_start=1828
  _globals['_CLICKHOUSESOURCE']._serialized_end=2018
  _globals['_CLICKHOUSETARGET']._serialized_start=2021
  _globals['_CLICKHOUSETARGET']._serialized_end=2664
# @@protoc_insertion_point(module_scope)
