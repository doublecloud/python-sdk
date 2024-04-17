from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from doublecloud.v1 import cluster_pb2 as _cluster_pb2
from doublecloud.v1 import maintenance_pb2 as _maintenance_pb2
from doublecloud.kafka.v1 import config_pb2 as _config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Cluster(_message.Message):
    __slots__ = ("id", "project_id", "cloud_type", "region_id", "create_time", "name", "description", "status", "version", "resources", "connection_info", "access", "encryption", "network_id", "private_connection_info", "maintenance_window", "planned_operation", "kafka_config", "metrics_exporter_connection_info", "schema_registry_config", "rest_api_config")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TYPE_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CONNECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    PLANNED_OPERATION_FIELD_NUMBER: _ClassVar[int]
    KAFKA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    METRICS_EXPORTER_CONNECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_REGISTRY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REST_API_CONFIG_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    cloud_type: str
    region_id: str
    create_time: _timestamp_pb2.Timestamp
    name: str
    description: str
    status: _cluster_pb2.ClusterStatus
    version: str
    resources: ClusterResources
    connection_info: ConnectionInfo
    access: _cluster_pb2.Access
    encryption: _cluster_pb2.DataEncryption
    network_id: str
    private_connection_info: PrivateConnectionInfo
    maintenance_window: _maintenance_pb2.MaintenanceWindow
    planned_operation: _maintenance_pb2.MaintenanceOperation
    kafka_config: _config_pb2.KafkaConfig
    metrics_exporter_connection_info: MetricsExporterConnectionInfo
    schema_registry_config: _config_pb2.SchemaRegistryConfig
    rest_api_config: _config_pb2.RestAPIConfig
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., cloud_type: _Optional[str] = ..., region_id: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[_Union[_cluster_pb2.ClusterStatus, str]] = ..., version: _Optional[str] = ..., resources: _Optional[_Union[ClusterResources, _Mapping]] = ..., connection_info: _Optional[_Union[ConnectionInfo, _Mapping]] = ..., access: _Optional[_Union[_cluster_pb2.Access, _Mapping]] = ..., encryption: _Optional[_Union[_cluster_pb2.DataEncryption, _Mapping]] = ..., network_id: _Optional[str] = ..., private_connection_info: _Optional[_Union[PrivateConnectionInfo, _Mapping]] = ..., maintenance_window: _Optional[_Union[_maintenance_pb2.MaintenanceWindow, _Mapping]] = ..., planned_operation: _Optional[_Union[_maintenance_pb2.MaintenanceOperation, _Mapping]] = ..., kafka_config: _Optional[_Union[_config_pb2.KafkaConfig, _Mapping]] = ..., metrics_exporter_connection_info: _Optional[_Union[MetricsExporterConnectionInfo, _Mapping]] = ..., schema_registry_config: _Optional[_Union[_config_pb2.SchemaRegistryConfig, _Mapping]] = ..., rest_api_config: _Optional[_Union[_config_pb2.RestAPIConfig, _Mapping]] = ...) -> None: ...

class ClusterResources(_message.Message):
    __slots__ = ("kafka",)
    class Kafka(_message.Message):
        __slots__ = ("resource_preset_id", "disk_size", "broker_count", "zone_count", "max_disk_size", "min_resource_preset_id", "max_resource_preset_id")
        RESOURCE_PRESET_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        BROKER_COUNT_FIELD_NUMBER: _ClassVar[int]
        ZONE_COUNT_FIELD_NUMBER: _ClassVar[int]
        MAX_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        MIN_RESOURCE_PRESET_ID_FIELD_NUMBER: _ClassVar[int]
        MAX_RESOURCE_PRESET_ID_FIELD_NUMBER: _ClassVar[int]
        resource_preset_id: str
        disk_size: _wrappers_pb2.Int64Value
        broker_count: _wrappers_pb2.Int64Value
        zone_count: _wrappers_pb2.Int64Value
        max_disk_size: _wrappers_pb2.Int64Value
        min_resource_preset_id: _wrappers_pb2.StringValue
        max_resource_preset_id: _wrappers_pb2.StringValue
        def __init__(self, resource_preset_id: _Optional[str] = ..., disk_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., broker_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., zone_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_disk_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., min_resource_preset_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., max_resource_preset_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
    KAFKA_FIELD_NUMBER: _ClassVar[int]
    kafka: ClusterResources.Kafka
    def __init__(self, kafka: _Optional[_Union[ClusterResources.Kafka, _Mapping]] = ...) -> None: ...

class ConnectionInfo(_message.Message):
    __slots__ = ("connection_string", "user", "password")
    CONNECTION_STRING_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    connection_string: str
    user: str
    password: str
    def __init__(self, connection_string: _Optional[str] = ..., user: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class PrivateConnectionInfo(_message.Message):
    __slots__ = ("connection_string", "user", "password")
    CONNECTION_STRING_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    connection_string: str
    user: str
    password: str
    def __init__(self, connection_string: _Optional[str] = ..., user: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class MetricsExporterConnectionInfo(_message.Message):
    __slots__ = ("user", "password")
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    password: str
    def __init__(self, user: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class Host(_message.Message):
    __slots__ = ("name", "cluster_id", "status")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    cluster_id: str
    status: _cluster_pb2.HostStatus
    def __init__(self, name: _Optional[str] = ..., cluster_id: _Optional[str] = ..., status: _Optional[_Union[_cluster_pb2.HostStatus, str]] = ...) -> None: ...
