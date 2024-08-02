# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/clickhouse/v1/config.proto
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
    'doublecloud/clickhouse/v1/config.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&doublecloud/clickhouse/v1/config.proto\x12\x19\x64oublecloud.clickhouse.v1\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xf1P\n\x10\x43lickhouseConfig\x12Q\n\tlog_level\x18\x01 \x01(\x0e\x32\x34.doublecloud.clickhouse.v1.ClickhouseConfig.LogLevelR\x08logLevel\x12\x44\n\x0fmax_connections\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0emaxConnections\x12Q\n\x16max_concurrent_queries\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x14maxConcurrentQueries\x12G\n\x12keep_alive_timeout\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x10keepAliveTimeout\x12S\n\x17uncompressed_cache_size\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x15uncompressedCacheSize\x12\x43\n\x0fmark_cache_size\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\rmarkCacheSize\x12O\n\x16max_table_size_to_drop\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x12maxTableSizeToDrop\x12W\n\x1amax_partition_size_to_drop\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x16maxPartitionSizeToDrop\x12\x38\n\x08timezone\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x08timezone\x12M\n\x14\x62\x61\x63kground_pool_size\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x12\x62\x61\x63kgroundPoolSize\x12^\n\x1d\x62\x61\x63kground_schedule_pool_size\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x1a\x62\x61\x63kgroundSchedulePoolSize\x12\\\n\x1c\x62\x61\x63kground_fetches_pool_size\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x19\x62\x61\x63kgroundFetchesPoolSize\x12V\n\x19\x62\x61\x63kground_move_pool_size\x18\r \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x16\x62\x61\x63kgroundMovePoolSize\x12Z\n\x1b\x62\x61\x63kground_common_pool_size\x18\x0e \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x18\x62\x61\x63kgroundCommonPoolSize\x12}\n-background_merges_mutations_concurrency_ratio\x18\x0f \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR)backgroundMergesMutationsConcurrencyRatio\x12X\n\x1atotal_memory_profiler_step\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x17totalMemoryProfilerStep\x12T\n\nmerge_tree\x18\x11 \x01(\x0b\x32\x35.doublecloud.clickhouse.v1.ClickhouseConfig.MergeTreeR\tmergeTree\x12Y\n\x0b\x63ompression\x18\x12 \x03(\x0b\x32\x37.doublecloud.clickhouse.v1.ClickhouseConfig.CompressionR\x0b\x63ompression\x12h\n\x0fgraphite_rollup\x18\x13 \x03(\x0b\x32?.doublecloud.clickhouse.v1.ClickhouseConfig.GraphiteRollupEntryR\x0egraphiteRollup\x12G\n\x05kafka\x18\x14 \x01(\x0b\x32\x31.doublecloud.clickhouse.v1.ClickhouseConfig.KafkaR\x05kafka\x12_\n\x0ckafka_topics\x18\x15 \x03(\x0b\x32<.doublecloud.clickhouse.v1.ClickhouseConfig.KafkaTopicsEntryR\x0bkafkaTopics\x12P\n\x08rabbitmq\x18\x16 \x01(\x0b\x32\x34.doublecloud.clickhouse.v1.ClickhouseConfig.RabbitmqR\x08rabbitmq\x12r\n\'total_memory_tracker_sample_probability\x18\x17 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR#totalMemoryTrackerSampleProbability\x12z\n,background_message_broker_schedule_pool_size\x18\x18 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\'backgroundMessageBrokerSchedulePoolSize\x12T\n\x18query_log_retention_size\x18\x19 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x15queryLogRetentionSize\x12R\n\x18query_log_retention_time\x18\x1a \x01(\x0b\x32\x19.google.protobuf.DurationR\x15queryLogRetentionTime\x12S\n\x18query_thread_log_enabled\x18\x1b \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x15queryThreadLogEnabled\x12\x61\n\x1fquery_thread_log_retention_size\x18\x1c \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x1bqueryThreadLogRetentionSize\x12_\n\x1fquery_thread_log_retention_time\x18\x1d \x01(\x0b\x32\x19.google.protobuf.DurationR\x1bqueryThreadLogRetentionTime\x12Q\n\x17query_views_log_enabled\x18\x1e \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x14queryViewsLogEnabled\x12_\n\x1equery_views_log_retention_size\x18\x1f \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x1aqueryViewsLogRetentionSize\x12]\n\x1equery_views_log_retention_time\x18  \x01(\x0b\x32\x19.google.protobuf.DurationR\x1aqueryViewsLogRetentionTime\x12R\n\x17part_log_retention_size\x18! \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x14partLogRetentionSize\x12P\n\x17part_log_retention_time\x18\" \x01(\x0b\x32\x19.google.protobuf.DurationR\x14partLogRetentionTime\x12H\n\x12metric_log_enabled\x18# \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x10metricLogEnabled\x12V\n\x19metric_log_retention_size\x18$ \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x16metricLogRetentionSize\x12T\n\x19metric_log_retention_time\x18% \x01(\x0b\x32\x19.google.protobuf.DurationR\x16metricLogRetentionTime\x12\x61\n\x1f\x61synchronous_metric_log_enabled\x18& \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x1c\x61synchronousMetricLogEnabled\x12o\n&asynchronous_metric_log_retention_size\x18\' \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\"asynchronousMetricLogRetentionSize\x12m\n&asynchronous_metric_log_retention_time\x18( \x01(\x0b\x32\x19.google.protobuf.DurationR\"asynchronousMetricLogRetentionTime\x12\x46\n\x11trace_log_enabled\x18) \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x0ftraceLogEnabled\x12T\n\x18trace_log_retention_size\x18* \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x15traceLogRetentionSize\x12R\n\x18trace_log_retention_time\x18+ \x01(\x0b\x32\x19.google.protobuf.DurationR\x15traceLogRetentionTime\x12\x44\n\x10text_log_enabled\x18, \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x0etextLogEnabled\x12R\n\x17text_log_retention_size\x18- \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x14textLogRetentionSize\x12P\n\x17text_log_retention_time\x18. \x01(\x0b\x32\x19.google.protobuf.DurationR\x14textLogRetentionTime\x12Z\n\x0etext_log_level\x18/ \x01(\x0e\x32\x34.doublecloud.clickhouse.v1.ClickhouseConfig.LogLevelR\x0ctextLogLevel\x12_\n\x1eopentelemetry_span_log_enabled\x18\x30 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x1bopentelemetrySpanLogEnabled\x12m\n%opentelemetry_span_log_retention_size\x18\x31 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR!opentelemetrySpanLogRetentionSize\x12k\n%opentelemetry_span_log_retention_time\x18\x32 \x01(\x0b\x32\x19.google.protobuf.DurationR!opentelemetrySpanLogRetentionTime\x12J\n\x13session_log_enabled\x18\x33 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x11sessionLogEnabled\x12X\n\x1asession_log_retention_size\x18\x34 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x17sessionLogRetentionSize\x12V\n\x1asession_log_retention_time\x18\x35 \x01(\x0b\x32\x19.google.protobuf.DurationR\x17sessionLogRetentionTime\x12N\n\x15zookeeper_log_enabled\x18\x36 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x13zookeeperLogEnabled\x12\\\n\x1czookeeper_log_retention_size\x18\x37 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x19zookeeperLogRetentionSize\x12Z\n\x1czookeeper_log_retention_time\x18\x38 \x01(\x0b\x32\x19.google.protobuf.DurationR\x19zookeeperLogRetentionTime\x12\x61\n\x1f\x61synchronous_insert_log_enabled\x18\x39 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x1c\x61synchronousInsertLogEnabled\x12o\n&asynchronous_insert_log_retention_size\x18: \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\"asynchronousInsertLogRetentionSize\x12m\n&asynchronous_insert_log_retention_time\x18; \x01(\x0b\x32\x19.google.protobuf.DurationR\"asynchronousInsertLogRetentionTime\x12`\n\x0ehybrid_storage\x18= \x01(\x0b\x32\x39.doublecloud.clickhouse.v1.ClickhouseConfig.HybridStorageR\rhybridStorage\x1a\xc1\x12\n\tMergeTree\x12\x63\n\x1freplicated_deduplication_window\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x1dreplicatedDeduplicationWindow\x12p\n\'replicated_deduplication_window_seconds\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR$replicatedDeduplicationWindowSeconds\x12N\n\x15parts_to_delay_insert\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x12partsToDelayInsert\x12N\n\x15parts_to_throw_insert\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x12partsToThrowInsert\x12_\n\x1emax_replicated_merges_in_queue\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x1amaxReplicatedMergesInQueue\x12\x8e\x01\n9number_of_free_entries_in_pool_to_lower_max_size_of_merge\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR.numberOfFreeEntriesInPoolToLowerMaxSizeOfMerge\x12m\n\'max_bytes_to_merge_at_min_space_in_pool\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x1fmaxBytesToMergeAtMinSpaceInPool\x12m\n\'max_bytes_to_merge_at_max_space_in_pool\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x1fmaxBytesToMergeAtMaxSpaceInPool\x12Q\n\x17min_bytes_for_wide_part\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x13minBytesForWidePart\x12O\n\x16min_rows_for_wide_part\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x12minRowsForWidePart\x12I\n\x13ttl_only_drop_parts\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x10ttlOnlyDropParts\x12_\n\x1einactive_parts_to_delay_insert\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x1ainactivePartsToDelayInsert\x12_\n\x1einactive_parts_to_throw_insert\x18\r \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x1ainactivePartsToThrowInsert\x12k\n%allow_remote_fs_zero_copy_replication\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.BoolValueR allowRemoteFsZeroCopyReplication\x12N\n\x16merge_with_ttl_timeout\x18\x0f \x01(\x0b\x32\x19.google.protobuf.DurationR\x13mergeWithTtlTimeout\x12i\n$merge_with_recompression_ttl_timeout\x18\x10 \x01(\x0b\x32\x19.google.protobuf.DurationR mergeWithRecompressionTtlTimeout\x12H\n\x12max_parts_in_total\x18\x11 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0fmaxPartsInTotal\x12j\n%max_number_of_merges_with_ttl_in_pool\x18\x12 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x1emaxNumberOfMergesWithTtlInPool\x12K\n\x14\x63leanup_delay_period\x18\x13 \x01(\x0b\x32\x19.google.protobuf.DurationR\x12\x63leanupDelayPeriod\x12\x83\x01\n2number_of_free_entries_in_pool_to_execute_mutation\x18\x14 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR*numberOfFreeEntriesInPoolToExecuteMutation\x12h\n$max_avg_part_size_for_too_many_parts\x18\x15 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x1dmaxAvgPartSizeForTooManyParts\x12\\\n\x1emin_age_to_force_merge_seconds\x18\x16 \x01(\x0b\x32\x19.google.protobuf.DurationR\x19minAgeToForceMergeSeconds\x12o\n(min_age_to_force_merge_on_partition_only\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR!minAgeToForceMergeOnPartitionOnly\x12R\n\x18merge_selecting_sleep_ms\x18\x18 \x01(\x0b\x32\x19.google.protobuf.DurationR\x15mergeSelectingSleepMs\x1a\xc3\x07\n\x05Kafka\x12o\n\x11security_protocol\x18\x01 \x01(\x0e\x32\x42.doublecloud.clickhouse.v1.ClickhouseConfig.Kafka.SecurityProtocolR\x10securityProtocol\x12\x66\n\x0esasl_mechanism\x18\x02 \x01(\x0e\x32?.doublecloud.clickhouse.v1.ClickhouseConfig.Kafka.SaslMechanismR\rsaslMechanism\x12\x41\n\rsasl_username\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x0csaslUsername\x12\x41\n\rsasl_password\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x0csaslPassword\x12i\n#enable_ssl_certificate_verification\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR enableSslCertificateVerification\x12J\n\x14max_poll_interval_ms\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationR\x11maxPollIntervalMs\x12G\n\x12session_timeout_ms\x18\x07 \x01(\x0b\x32\x19.google.protobuf.DurationR\x10sessionTimeoutMs\"\xb3\x01\n\x10SecurityProtocol\x12\x1d\n\x19SECURITY_PROTOCOL_INVALID\x10\x00\x12\x1f\n\x1bSECURITY_PROTOCOL_PLAINTEXT\x10\x01\x12\x19\n\x15SECURITY_PROTOCOL_SSL\x10\x02\x12$\n SECURITY_PROTOCOL_SASL_PLAINTEXT\x10\x03\x12\x1e\n\x1aSECURITY_PROTOCOL_SASL_SSL\x10\x04\"\xa4\x01\n\rSaslMechanism\x12\x1a\n\x16SASL_MECHANISM_INVALID\x10\x00\x12\x19\n\x15SASL_MECHANISM_GSSAPI\x10\x01\x12\x18\n\x14SASL_MECHANISM_PLAIN\x10\x02\x12 \n\x1cSASL_MECHANISM_SCRAM_SHA_256\x10\x03\x12 \n\x1cSASL_MECHANISM_SCRAM_SHA_512\x10\x04\x1a\xb2\x01\n\x08Rabbitmq\x12\x38\n\x08username\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x08username\x12\x38\n\x08password\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x08password\x12\x32\n\x05vhost\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x05vhost\x1a\xbc\x02\n\x0b\x43ompression\x12V\n\x06method\x18\x01 \x01(\x0e\x32>.doublecloud.clickhouse.v1.ClickhouseConfig.Compression.MethodR\x06method\x12\"\n\rmin_part_size\x18\x02 \x01(\x03R\x0bminPartSize\x12-\n\x13min_part_size_ratio\x18\x03 \x01(\x01R\x10minPartSizeRatio\x12\x31\n\x05level\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x05level\"O\n\x06Method\x12\x12\n\x0eMETHOD_INVALID\x10\x00\x12\x0e\n\nMETHOD_LZ4\x10\x01\x12\x0f\n\x0bMETHOD_ZSTD\x10\x02\x12\x10\n\x0cMETHOD_LZ4HC\x10\x03\x1a\x95\x03\n\x0eGraphiteRollup\x12^\n\x08patterns\x18\x01 \x03(\x0b\x32\x42.doublecloud.clickhouse.v1.ClickhouseConfig.GraphiteRollup.PatternR\x08patterns\x1a\xa2\x02\n\x07Pattern\x12\x34\n\x06regexp\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x06regexp\x12\x38\n\x08\x66unction\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x08\x66unction\x12j\n\tretention\x18\x03 \x03(\x0b\x32L.doublecloud.clickhouse.v1.ClickhouseConfig.GraphiteRollup.Pattern.RetentionR\tretention\x1a;\n\tRetention\x12\x10\n\x03\x61ge\x18\x01 \x01(\x03R\x03\x61ge\x12\x1c\n\tprecision\x18\x02 \x01(\x03R\tprecision\x1a\x8a\x02\n\rHybridStorage\x12I\n\x13prefer_not_to_merge\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x10preferNotToMerge\x12H\n\x12max_data_part_size\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0fmaxDataPartSize\x12\x64\n!max_object_storage_data_part_size\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x1cmaxObjectStorageDataPartSize\x1a}\n\x13GraphiteRollupEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12P\n\x05value\x18\x02 \x01(\x0b\x32:.doublecloud.clickhouse.v1.ClickhouseConfig.GraphiteRollupR\x05value:\x02\x38\x01\x1aq\n\x10KafkaTopicsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12G\n\x05value\x18\x02 \x01(\x0b\x32\x31.doublecloud.clickhouse.v1.ClickhouseConfig.KafkaR\x05value:\x02\x38\x01\"\x92\x01\n\x08LogLevel\x12\x15\n\x11LOG_LEVEL_DEFAULT\x10\x00\x12\x13\n\x0fLOG_LEVEL_TRACE\x10\x01\x12\x13\n\x0fLOG_LEVEL_DEBUG\x10\x02\x12\x19\n\x15LOG_LEVEL_INFORMATION\x10\x03\x12\x15\n\x11LOG_LEVEL_WARNING\x10\x04\x12\x13\n\x0fLOG_LEVEL_ERROR\x10\x05J\x04\x08<\x10=BIZGgithub.com/doublecloud/go-genproto/doublecloud/clickhouse/v1;clickhouseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.clickhouse.v1.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZGgithub.com/doublecloud/go-genproto/doublecloud/clickhouse/v1;clickhouse'
  _globals['_CLICKHOUSECONFIG_GRAPHITEROLLUPENTRY']._loaded_options = None
  _globals['_CLICKHOUSECONFIG_GRAPHITEROLLUPENTRY']._serialized_options = b'8\001'
  _globals['_CLICKHOUSECONFIG_KAFKATOPICSENTRY']._loaded_options = None
  _globals['_CLICKHOUSECONFIG_KAFKATOPICSENTRY']._serialized_options = b'8\001'
  _globals['_CLICKHOUSECONFIG']._serialized_start=134
  _globals['_CLICKHOUSECONFIG']._serialized_end=10487
  _globals['_CLICKHOUSECONFIG_MERGETREE']._serialized_start=5578
  _globals['_CLICKHOUSECONFIG_MERGETREE']._serialized_end=7947
  _globals['_CLICKHOUSECONFIG_KAFKA']._serialized_start=7950
  _globals['_CLICKHOUSECONFIG_KAFKA']._serialized_end=8913
  _globals['_CLICKHOUSECONFIG_KAFKA_SECURITYPROTOCOL']._serialized_start=8567
  _globals['_CLICKHOUSECONFIG_KAFKA_SECURITYPROTOCOL']._serialized_end=8746
  _globals['_CLICKHOUSECONFIG_KAFKA_SASLMECHANISM']._serialized_start=8749
  _globals['_CLICKHOUSECONFIG_KAFKA_SASLMECHANISM']._serialized_end=8913
  _globals['_CLICKHOUSECONFIG_RABBITMQ']._serialized_start=8916
  _globals['_CLICKHOUSECONFIG_RABBITMQ']._serialized_end=9094
  _globals['_CLICKHOUSECONFIG_COMPRESSION']._serialized_start=9097
  _globals['_CLICKHOUSECONFIG_COMPRESSION']._serialized_end=9413
  _globals['_CLICKHOUSECONFIG_COMPRESSION_METHOD']._serialized_start=9334
  _globals['_CLICKHOUSECONFIG_COMPRESSION_METHOD']._serialized_end=9413
  _globals['_CLICKHOUSECONFIG_GRAPHITEROLLUP']._serialized_start=9416
  _globals['_CLICKHOUSECONFIG_GRAPHITEROLLUP']._serialized_end=9821
  _globals['_CLICKHOUSECONFIG_GRAPHITEROLLUP_PATTERN']._serialized_start=9531
  _globals['_CLICKHOUSECONFIG_GRAPHITEROLLUP_PATTERN']._serialized_end=9821
  _globals['_CLICKHOUSECONFIG_GRAPHITEROLLUP_PATTERN_RETENTION']._serialized_start=9762
  _globals['_CLICKHOUSECONFIG_GRAPHITEROLLUP_PATTERN_RETENTION']._serialized_end=9821
  _globals['_CLICKHOUSECONFIG_HYBRIDSTORAGE']._serialized_start=9824
  _globals['_CLICKHOUSECONFIG_HYBRIDSTORAGE']._serialized_end=10090
  _globals['_CLICKHOUSECONFIG_GRAPHITEROLLUPENTRY']._serialized_start=10092
  _globals['_CLICKHOUSECONFIG_GRAPHITEROLLUPENTRY']._serialized_end=10217
  _globals['_CLICKHOUSECONFIG_KAFKATOPICSENTRY']._serialized_start=10219
  _globals['_CLICKHOUSECONFIG_KAFKATOPICSENTRY']._serialized_end=10332
  _globals['_CLICKHOUSECONFIG_LOGLEVEL']._serialized_start=10335
  _globals['_CLICKHOUSECONFIG_LOGLEVEL']._serialized_end=10481
# @@protoc_insertion_point(module_scope)
