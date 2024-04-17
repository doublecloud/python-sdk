from doublecloud.transfer.v1.endpoint import common_pb2 as _common_pb2
from doublecloud.transfer.v1.endpoint import parsers_pb2 as _parsers_pb2
from doublecloud.transfer.v1.endpoint import serializers_pb2 as _serializers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KafkaMechanism(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KAFKA_MECHANISM_UNSPECIFIED: _ClassVar[KafkaMechanism]
    KAFKA_MECHANISM_SHA256: _ClassVar[KafkaMechanism]
    KAFKA_MECHANISM_SHA512: _ClassVar[KafkaMechanism]

class KafkaCompressionEncoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KAFKA_COMPRESSION_ENCODING_UNSPECIFIED: _ClassVar[KafkaCompressionEncoding]
    KAFKA_COMPRESSION_ENCODING_GZIP: _ClassVar[KafkaCompressionEncoding]
    KAFKA_COMPRESSION_ENCODING_SNAPPY: _ClassVar[KafkaCompressionEncoding]
    KAFKA_COMPRESSION_ENCODING_LZ4: _ClassVar[KafkaCompressionEncoding]
    KAFKA_COMPRESSION_ENCODING_ZSTD: _ClassVar[KafkaCompressionEncoding]
KAFKA_MECHANISM_UNSPECIFIED: KafkaMechanism
KAFKA_MECHANISM_SHA256: KafkaMechanism
KAFKA_MECHANISM_SHA512: KafkaMechanism
KAFKA_COMPRESSION_ENCODING_UNSPECIFIED: KafkaCompressionEncoding
KAFKA_COMPRESSION_ENCODING_GZIP: KafkaCompressionEncoding
KAFKA_COMPRESSION_ENCODING_SNAPPY: KafkaCompressionEncoding
KAFKA_COMPRESSION_ENCODING_LZ4: KafkaCompressionEncoding
KAFKA_COMPRESSION_ENCODING_ZSTD: KafkaCompressionEncoding

class KafkaConnectionOptions(_message.Message):
    __slots__ = ("cluster_id", "on_premise")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ON_PREMISE_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    on_premise: OnPremiseKafka
    def __init__(self, cluster_id: _Optional[str] = ..., on_premise: _Optional[_Union[OnPremiseKafka, _Mapping]] = ...) -> None: ...

class OnPremiseKafka(_message.Message):
    __slots__ = ("broker_urls", "tls_mode")
    BROKER_URLS_FIELD_NUMBER: _ClassVar[int]
    TLS_MODE_FIELD_NUMBER: _ClassVar[int]
    broker_urls: _containers.RepeatedScalarFieldContainer[str]
    tls_mode: _common_pb2.TLSMode
    def __init__(self, broker_urls: _Optional[_Iterable[str]] = ..., tls_mode: _Optional[_Union[_common_pb2.TLSMode, _Mapping]] = ...) -> None: ...

class KafkaAuth(_message.Message):
    __slots__ = ("sasl", "no_auth")
    SASL_FIELD_NUMBER: _ClassVar[int]
    NO_AUTH_FIELD_NUMBER: _ClassVar[int]
    sasl: KafkaSaslSecurity
    no_auth: _common_pb2.NoAuth
    def __init__(self, sasl: _Optional[_Union[KafkaSaslSecurity, _Mapping]] = ..., no_auth: _Optional[_Union[_common_pb2.NoAuth, _Mapping]] = ...) -> None: ...

class KafkaSaslSecurity(_message.Message):
    __slots__ = ("user", "mechanism", "password")
    USER_FIELD_NUMBER: _ClassVar[int]
    MECHANISM_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    mechanism: KafkaMechanism
    password: _common_pb2.Secret
    def __init__(self, user: _Optional[str] = ..., mechanism: _Optional[_Union[KafkaMechanism, str]] = ..., password: _Optional[_Union[_common_pb2.Secret, _Mapping]] = ...) -> None: ...

class KafkaSource(_message.Message):
    __slots__ = ("connection", "auth", "topic_name", "parser", "topic_names")
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    PARSER_FIELD_NUMBER: _ClassVar[int]
    TOPIC_NAMES_FIELD_NUMBER: _ClassVar[int]
    connection: KafkaConnectionOptions
    auth: KafkaAuth
    topic_name: str
    parser: _parsers_pb2.Parser
    topic_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, connection: _Optional[_Union[KafkaConnectionOptions, _Mapping]] = ..., auth: _Optional[_Union[KafkaAuth, _Mapping]] = ..., topic_name: _Optional[str] = ..., parser: _Optional[_Union[_parsers_pb2.Parser, _Mapping]] = ..., topic_names: _Optional[_Iterable[str]] = ...) -> None: ...

class KafkaTarget(_message.Message):
    __slots__ = ("connection", "auth", "topic_settings", "serializer", "compression")
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    TOPIC_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SERIALIZER_FIELD_NUMBER: _ClassVar[int]
    COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    connection: KafkaConnectionOptions
    auth: KafkaAuth
    topic_settings: KafkaTargetTopicSettings
    serializer: _serializers_pb2.Serializer
    compression: KafkaCompressionEncoding
    def __init__(self, connection: _Optional[_Union[KafkaConnectionOptions, _Mapping]] = ..., auth: _Optional[_Union[KafkaAuth, _Mapping]] = ..., topic_settings: _Optional[_Union[KafkaTargetTopicSettings, _Mapping]] = ..., serializer: _Optional[_Union[_serializers_pb2.Serializer, _Mapping]] = ..., compression: _Optional[_Union[KafkaCompressionEncoding, str]] = ...) -> None: ...

class KafkaTargetTopicSettings(_message.Message):
    __slots__ = ("topic", "topic_prefix", "topic_config_entries")
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    TOPIC_PREFIX_FIELD_NUMBER: _ClassVar[int]
    TOPIC_CONFIG_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    topic: KafkaTargetTopic
    topic_prefix: str
    topic_config_entries: _containers.RepeatedCompositeFieldContainer[TopicConfigEntry]
    def __init__(self, topic: _Optional[_Union[KafkaTargetTopic, _Mapping]] = ..., topic_prefix: _Optional[str] = ..., topic_config_entries: _Optional[_Iterable[_Union[TopicConfigEntry, _Mapping]]] = ...) -> None: ...

class KafkaTargetTopic(_message.Message):
    __slots__ = ("topic_name", "save_tx_order")
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    SAVE_TX_ORDER_FIELD_NUMBER: _ClassVar[int]
    topic_name: str
    save_tx_order: bool
    def __init__(self, topic_name: _Optional[str] = ..., save_tx_order: bool = ...) -> None: ...

class TopicConfigEntry(_message.Message):
    __slots__ = ("config_name", "config_value")
    CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VALUE_FIELD_NUMBER: _ClassVar[int]
    config_name: str
    config_value: str
    def __init__(self, config_name: _Optional[str] = ..., config_value: _Optional[str] = ...) -> None: ...
