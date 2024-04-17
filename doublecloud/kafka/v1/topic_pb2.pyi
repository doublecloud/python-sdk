from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Topic(_message.Message):
    __slots__ = ("name", "cluster_id", "partitions", "replication_factor", "topic_config_2_8", "topic_config_3", "is_ha")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    TOPIC_CONFIG_2_8_FIELD_NUMBER: _ClassVar[int]
    TOPIC_CONFIG_3_FIELD_NUMBER: _ClassVar[int]
    IS_HA_FIELD_NUMBER: _ClassVar[int]
    name: str
    cluster_id: str
    partitions: _wrappers_pb2.Int64Value
    replication_factor: _wrappers_pb2.Int64Value
    topic_config_2_8: TopicConfig28
    topic_config_3: TopicConfig3
    is_ha: bool
    def __init__(self, name: _Optional[str] = ..., cluster_id: _Optional[str] = ..., partitions: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., replication_factor: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., topic_config_2_8: _Optional[_Union[TopicConfig28, _Mapping]] = ..., topic_config_3: _Optional[_Union[TopicConfig3, _Mapping]] = ..., is_ha: bool = ...) -> None: ...

class TopicSpec(_message.Message):
    __slots__ = ("name", "partitions", "replication_factor", "topic_config_2_8", "topic_config_3")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    TOPIC_CONFIG_2_8_FIELD_NUMBER: _ClassVar[int]
    TOPIC_CONFIG_3_FIELD_NUMBER: _ClassVar[int]
    name: str
    partitions: _wrappers_pb2.Int64Value
    replication_factor: _wrappers_pb2.Int64Value
    topic_config_2_8: TopicConfig28
    topic_config_3: TopicConfig3
    def __init__(self, name: _Optional[str] = ..., partitions: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., replication_factor: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., topic_config_2_8: _Optional[_Union[TopicConfig28, _Mapping]] = ..., topic_config_3: _Optional[_Union[TopicConfig3, _Mapping]] = ...) -> None: ...

class TopicConfig28(_message.Message):
    __slots__ = ("cleanup_policy", "compression_type", "retention_bytes", "retention_ms", "max_message_bytes")
    class CleanupPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLEANUP_POLICY_INVALID: _ClassVar[TopicConfig28.CleanupPolicy]
        CLEANUP_POLICY_DELETE: _ClassVar[TopicConfig28.CleanupPolicy]
        CLEANUP_POLICY_COMPACT: _ClassVar[TopicConfig28.CleanupPolicy]
        CLEANUP_POLICY_COMPACT_AND_DELETE: _ClassVar[TopicConfig28.CleanupPolicy]
    CLEANUP_POLICY_INVALID: TopicConfig28.CleanupPolicy
    CLEANUP_POLICY_DELETE: TopicConfig28.CleanupPolicy
    CLEANUP_POLICY_COMPACT: TopicConfig28.CleanupPolicy
    CLEANUP_POLICY_COMPACT_AND_DELETE: TopicConfig28.CleanupPolicy
    class CompressionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPRESSION_TYPE_INVALID: _ClassVar[TopicConfig28.CompressionType]
        COMPRESSION_TYPE_UNCOMPRESSED: _ClassVar[TopicConfig28.CompressionType]
        COMPRESSION_TYPE_ZSTD: _ClassVar[TopicConfig28.CompressionType]
        COMPRESSION_TYPE_LZ4: _ClassVar[TopicConfig28.CompressionType]
        COMPRESSION_TYPE_SNAPPY: _ClassVar[TopicConfig28.CompressionType]
        COMPRESSION_TYPE_GZIP: _ClassVar[TopicConfig28.CompressionType]
        COMPRESSION_TYPE_PRODUCER: _ClassVar[TopicConfig28.CompressionType]
    COMPRESSION_TYPE_INVALID: TopicConfig28.CompressionType
    COMPRESSION_TYPE_UNCOMPRESSED: TopicConfig28.CompressionType
    COMPRESSION_TYPE_ZSTD: TopicConfig28.CompressionType
    COMPRESSION_TYPE_LZ4: TopicConfig28.CompressionType
    COMPRESSION_TYPE_SNAPPY: TopicConfig28.CompressionType
    COMPRESSION_TYPE_GZIP: TopicConfig28.CompressionType
    COMPRESSION_TYPE_PRODUCER: TopicConfig28.CompressionType
    CLEANUP_POLICY_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    RETENTION_BYTES_FIELD_NUMBER: _ClassVar[int]
    RETENTION_MS_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    cleanup_policy: TopicConfig28.CleanupPolicy
    compression_type: TopicConfig28.CompressionType
    retention_bytes: _wrappers_pb2.Int64Value
    retention_ms: _wrappers_pb2.Int64Value
    max_message_bytes: _wrappers_pb2.Int64Value
    def __init__(self, cleanup_policy: _Optional[_Union[TopicConfig28.CleanupPolicy, str]] = ..., compression_type: _Optional[_Union[TopicConfig28.CompressionType, str]] = ..., retention_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., retention_ms: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_message_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class TopicConfig3(_message.Message):
    __slots__ = ("cleanup_policy", "compression_type", "retention_bytes", "retention_ms", "max_message_bytes")
    class CleanupPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLEANUP_POLICY_INVALID: _ClassVar[TopicConfig3.CleanupPolicy]
        CLEANUP_POLICY_DELETE: _ClassVar[TopicConfig3.CleanupPolicy]
        CLEANUP_POLICY_COMPACT: _ClassVar[TopicConfig3.CleanupPolicy]
        CLEANUP_POLICY_COMPACT_AND_DELETE: _ClassVar[TopicConfig3.CleanupPolicy]
    CLEANUP_POLICY_INVALID: TopicConfig3.CleanupPolicy
    CLEANUP_POLICY_DELETE: TopicConfig3.CleanupPolicy
    CLEANUP_POLICY_COMPACT: TopicConfig3.CleanupPolicy
    CLEANUP_POLICY_COMPACT_AND_DELETE: TopicConfig3.CleanupPolicy
    class CompressionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMPRESSION_TYPE_INVALID: _ClassVar[TopicConfig3.CompressionType]
        COMPRESSION_TYPE_UNCOMPRESSED: _ClassVar[TopicConfig3.CompressionType]
        COMPRESSION_TYPE_ZSTD: _ClassVar[TopicConfig3.CompressionType]
        COMPRESSION_TYPE_LZ4: _ClassVar[TopicConfig3.CompressionType]
        COMPRESSION_TYPE_SNAPPY: _ClassVar[TopicConfig3.CompressionType]
        COMPRESSION_TYPE_GZIP: _ClassVar[TopicConfig3.CompressionType]
        COMPRESSION_TYPE_PRODUCER: _ClassVar[TopicConfig3.CompressionType]
    COMPRESSION_TYPE_INVALID: TopicConfig3.CompressionType
    COMPRESSION_TYPE_UNCOMPRESSED: TopicConfig3.CompressionType
    COMPRESSION_TYPE_ZSTD: TopicConfig3.CompressionType
    COMPRESSION_TYPE_LZ4: TopicConfig3.CompressionType
    COMPRESSION_TYPE_SNAPPY: TopicConfig3.CompressionType
    COMPRESSION_TYPE_GZIP: TopicConfig3.CompressionType
    COMPRESSION_TYPE_PRODUCER: TopicConfig3.CompressionType
    CLEANUP_POLICY_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    RETENTION_BYTES_FIELD_NUMBER: _ClassVar[int]
    RETENTION_MS_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    cleanup_policy: TopicConfig3.CleanupPolicy
    compression_type: TopicConfig3.CompressionType
    retention_bytes: _wrappers_pb2.Int64Value
    retention_ms: _wrappers_pb2.Int64Value
    max_message_bytes: _wrappers_pb2.Int64Value
    def __init__(self, cleanup_policy: _Optional[_Union[TopicConfig3.CleanupPolicy, str]] = ..., compression_type: _Optional[_Union[TopicConfig3.CompressionType, str]] = ..., retention_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., retention_ms: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_message_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...
