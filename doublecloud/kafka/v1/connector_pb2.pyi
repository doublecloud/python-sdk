from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectorSpec(_message.Message):
    __slots__ = ("name", "tasks_max", "properties", "connector_config_mirrormaker", "connector_config_s3_sink")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TASKS_MAX_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_CONFIG_MIRRORMAKER_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_CONFIG_S3_SINK_FIELD_NUMBER: _ClassVar[int]
    name: str
    tasks_max: _wrappers_pb2.Int64Value
    properties: _containers.ScalarMap[str, str]
    connector_config_mirrormaker: ConnectorConfigMirrorMakerSpec
    connector_config_s3_sink: ConnectorConfigS3SinkSpec
    def __init__(self, name: _Optional[str] = ..., tasks_max: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., properties: _Optional[_Mapping[str, str]] = ..., connector_config_mirrormaker: _Optional[_Union[ConnectorConfigMirrorMakerSpec, _Mapping]] = ..., connector_config_s3_sink: _Optional[_Union[ConnectorConfigS3SinkSpec, _Mapping]] = ...) -> None: ...

class UpdateConnectorSpec(_message.Message):
    __slots__ = ("tasks_max", "properties", "connector_config_mirrormaker", "connector_config_s3_sink")
    class UpdateProperties(_message.Message):
        __slots__ = ("properties",)
        class PropertiesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        properties: _containers.ScalarMap[str, str]
        def __init__(self, properties: _Optional[_Mapping[str, str]] = ...) -> None: ...
    TASKS_MAX_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_CONFIG_MIRRORMAKER_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_CONFIG_S3_SINK_FIELD_NUMBER: _ClassVar[int]
    tasks_max: _wrappers_pb2.Int64Value
    properties: UpdateConnectorSpec.UpdateProperties
    connector_config_mirrormaker: UpdateConnectorConfigMirrorMakerSpec
    connector_config_s3_sink: UpdateConnectorConfigS3SinkSpec
    def __init__(self, tasks_max: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., properties: _Optional[_Union[UpdateConnectorSpec.UpdateProperties, _Mapping]] = ..., connector_config_mirrormaker: _Optional[_Union[UpdateConnectorConfigMirrorMakerSpec, _Mapping]] = ..., connector_config_s3_sink: _Optional[_Union[UpdateConnectorConfigS3SinkSpec, _Mapping]] = ...) -> None: ...

class ConnectorConfigMirrorMakerSpec(_message.Message):
    __slots__ = ("source_cluster", "target_cluster", "topics", "replication_factor")
    SOURCE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    source_cluster: ClusterConnectionSpec
    target_cluster: ClusterConnectionSpec
    topics: str
    replication_factor: _wrappers_pb2.Int64Value
    def __init__(self, source_cluster: _Optional[_Union[ClusterConnectionSpec, _Mapping]] = ..., target_cluster: _Optional[_Union[ClusterConnectionSpec, _Mapping]] = ..., topics: _Optional[str] = ..., replication_factor: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class ClusterConnectionSpec(_message.Message):
    __slots__ = ("alias", "this_cluster", "external_cluster")
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    THIS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    alias: _wrappers_pb2.StringValue
    this_cluster: ThisCluster
    external_cluster: ExternalClusterConnectionSpec
    def __init__(self, alias: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., this_cluster: _Optional[_Union[ThisCluster, _Mapping]] = ..., external_cluster: _Optional[_Union[ExternalClusterConnectionSpec, _Mapping]] = ...) -> None: ...

class ExternalClusterConnectionSpec(_message.Message):
    __slots__ = ("bootstrap_servers", "sasl_username", "sasl_password", "sasl_mechanism", "security_protocol", "ssl_truststore_certificates")
    BOOTSTRAP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    SASL_USERNAME_FIELD_NUMBER: _ClassVar[int]
    SASL_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SASL_MECHANISM_FIELD_NUMBER: _ClassVar[int]
    SECURITY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    SSL_TRUSTSTORE_CERTIFICATES_FIELD_NUMBER: _ClassVar[int]
    bootstrap_servers: _wrappers_pb2.StringValue
    sasl_username: _wrappers_pb2.StringValue
    sasl_password: _wrappers_pb2.StringValue
    sasl_mechanism: _wrappers_pb2.StringValue
    security_protocol: _wrappers_pb2.StringValue
    ssl_truststore_certificates: _wrappers_pb2.StringValue
    def __init__(self, bootstrap_servers: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., sasl_username: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., sasl_password: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., sasl_mechanism: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., security_protocol: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., ssl_truststore_certificates: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ConnectorConfigS3SinkSpec(_message.Message):
    __slots__ = ("topics", "file_compression_type", "file_max_records", "s3_connection")
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    FILE_COMPRESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_MAX_RECORDS_FIELD_NUMBER: _ClassVar[int]
    S3_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    topics: str
    file_compression_type: str
    file_max_records: _wrappers_pb2.Int64Value
    s3_connection: S3ConnectionSpec
    def __init__(self, topics: _Optional[str] = ..., file_compression_type: _Optional[str] = ..., file_max_records: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., s3_connection: _Optional[_Union[S3ConnectionSpec, _Mapping]] = ...) -> None: ...

class UpdateConnectorConfigMirrorMakerSpec(_message.Message):
    __slots__ = ("source_cluster", "target_cluster", "topics", "replication_factor")
    SOURCE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    source_cluster: ClusterConnectionSpec
    target_cluster: ClusterConnectionSpec
    topics: _wrappers_pb2.StringValue
    replication_factor: _wrappers_pb2.Int64Value
    def __init__(self, source_cluster: _Optional[_Union[ClusterConnectionSpec, _Mapping]] = ..., target_cluster: _Optional[_Union[ClusterConnectionSpec, _Mapping]] = ..., topics: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., replication_factor: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class UpdateConnectorConfigS3SinkSpec(_message.Message):
    __slots__ = ("topics", "file_max_records", "s3_connection")
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    FILE_MAX_RECORDS_FIELD_NUMBER: _ClassVar[int]
    S3_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    topics: _wrappers_pb2.StringValue
    file_max_records: _wrappers_pb2.Int64Value
    s3_connection: S3ConnectionSpec
    def __init__(self, topics: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., file_max_records: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., s3_connection: _Optional[_Union[S3ConnectionSpec, _Mapping]] = ...) -> None: ...

class S3ConnectionSpec(_message.Message):
    __slots__ = ("bucket_name", "access_key_id", "secret_access_key", "endpoint", "region")
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    bucket_name: _wrappers_pb2.StringValue
    access_key_id: _wrappers_pb2.StringValue
    secret_access_key: _wrappers_pb2.StringValue
    endpoint: _wrappers_pb2.StringValue
    region: _wrappers_pb2.StringValue
    def __init__(self, bucket_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., access_key_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., secret_access_key: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., endpoint: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., region: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class Connector(_message.Message):
    __slots__ = ("name", "tasks_max", "properties", "health", "status", "cluster_id", "connector_config_mirrormaker", "connector_config_s3_sink")
    class Health(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HEALTH_INVALID: _ClassVar[Connector.Health]
        HEALTH_ALIVE: _ClassVar[Connector.Health]
        HEALTH_DEAD: _ClassVar[Connector.Health]
    HEALTH_INVALID: Connector.Health
    HEALTH_ALIVE: Connector.Health
    HEALTH_DEAD: Connector.Health
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_INVALID: _ClassVar[Connector.Status]
        STATUS_RUNNING: _ClassVar[Connector.Status]
        STATUS_ERROR: _ClassVar[Connector.Status]
        STATUS_PAUSED: _ClassVar[Connector.Status]
    STATUS_INVALID: Connector.Status
    STATUS_RUNNING: Connector.Status
    STATUS_ERROR: Connector.Status
    STATUS_PAUSED: Connector.Status
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TASKS_MAX_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_CONFIG_MIRRORMAKER_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_CONFIG_S3_SINK_FIELD_NUMBER: _ClassVar[int]
    name: str
    tasks_max: _wrappers_pb2.Int64Value
    properties: _containers.ScalarMap[str, str]
    health: Connector.Health
    status: Connector.Status
    cluster_id: str
    connector_config_mirrormaker: ConnectorConfigMirrorMaker
    connector_config_s3_sink: ConnectorConfigS3Sink
    def __init__(self, name: _Optional[str] = ..., tasks_max: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., properties: _Optional[_Mapping[str, str]] = ..., health: _Optional[_Union[Connector.Health, str]] = ..., status: _Optional[_Union[Connector.Status, str]] = ..., cluster_id: _Optional[str] = ..., connector_config_mirrormaker: _Optional[_Union[ConnectorConfigMirrorMaker, _Mapping]] = ..., connector_config_s3_sink: _Optional[_Union[ConnectorConfigS3Sink, _Mapping]] = ...) -> None: ...

class ConnectorConfigMirrorMaker(_message.Message):
    __slots__ = ("source_cluster", "target_cluster", "topics", "replication_factor")
    SOURCE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    source_cluster: ClusterConnection
    target_cluster: ClusterConnection
    topics: str
    replication_factor: _wrappers_pb2.Int64Value
    def __init__(self, source_cluster: _Optional[_Union[ClusterConnection, _Mapping]] = ..., target_cluster: _Optional[_Union[ClusterConnection, _Mapping]] = ..., topics: _Optional[str] = ..., replication_factor: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class ClusterConnection(_message.Message):
    __slots__ = ("alias", "this_cluster", "external_cluster")
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    THIS_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    alias: str
    this_cluster: ThisCluster
    external_cluster: ExternalClusterConnection
    def __init__(self, alias: _Optional[str] = ..., this_cluster: _Optional[_Union[ThisCluster, _Mapping]] = ..., external_cluster: _Optional[_Union[ExternalClusterConnection, _Mapping]] = ...) -> None: ...

class ThisCluster(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalClusterConnection(_message.Message):
    __slots__ = ("bootstrap_servers", "sasl_username", "sasl_mechanism", "security_protocol")
    BOOTSTRAP_SERVERS_FIELD_NUMBER: _ClassVar[int]
    SASL_USERNAME_FIELD_NUMBER: _ClassVar[int]
    SASL_MECHANISM_FIELD_NUMBER: _ClassVar[int]
    SECURITY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    bootstrap_servers: str
    sasl_username: str
    sasl_mechanism: str
    security_protocol: str
    def __init__(self, bootstrap_servers: _Optional[str] = ..., sasl_username: _Optional[str] = ..., sasl_mechanism: _Optional[str] = ..., security_protocol: _Optional[str] = ...) -> None: ...

class ConnectorConfigS3Sink(_message.Message):
    __slots__ = ("topics", "file_compression_type", "file_max_records", "s3_connection")
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    FILE_COMPRESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_MAX_RECORDS_FIELD_NUMBER: _ClassVar[int]
    S3_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    topics: str
    file_compression_type: str
    file_max_records: _wrappers_pb2.Int64Value
    s3_connection: S3Connection
    def __init__(self, topics: _Optional[str] = ..., file_compression_type: _Optional[str] = ..., file_max_records: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., s3_connection: _Optional[_Union[S3Connection, _Mapping]] = ...) -> None: ...

class S3Connection(_message.Message):
    __slots__ = ("bucket_name", "access_key_id", "endpoint", "region")
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    bucket_name: str
    access_key_id: str
    endpoint: str
    region: str
    def __init__(self, bucket_name: _Optional[str] = ..., access_key_id: _Optional[str] = ..., endpoint: _Optional[str] = ..., region: _Optional[str] = ...) -> None: ...
