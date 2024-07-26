from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from doublecloud.clickhouse.v1 import config_pb2 as _config_pb2
from doublecloud.v1 import cluster_pb2 as _cluster_pb2
from doublecloud.v1 import maintenance_pb2 as _maintenance_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Cluster(_message.Message):
    __slots__ = ("id", "project_id", "cloud_type", "region_id", "create_time", "name", "description", "status", "version", "resources", "connection_info", "access", "private_connection_info", "encryption", "network_id", "clickhouse_config", "maintenance_window", "maintenance_operation", "metrics_exporter_connection_info", "custom_certificate")
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
    PRIVATE_CONNECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    CLICKHOUSE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_OPERATION_FIELD_NUMBER: _ClassVar[int]
    METRICS_EXPORTER_CONNECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
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
    private_connection_info: PrivateConnectionInfo
    encryption: _cluster_pb2.DataEncryption
    network_id: str
    clickhouse_config: _config_pb2.ClickhouseConfig
    maintenance_window: _maintenance_pb2.MaintenanceWindow
    maintenance_operation: _maintenance_pb2.MaintenanceOperation
    metrics_exporter_connection_info: MetricsExporterConnectionInfo
    custom_certificate: CustomCertificate
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., cloud_type: _Optional[str] = ..., region_id: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[_Union[_cluster_pb2.ClusterStatus, str]] = ..., version: _Optional[str] = ..., resources: _Optional[_Union[ClusterResources, _Mapping]] = ..., connection_info: _Optional[_Union[ConnectionInfo, _Mapping]] = ..., access: _Optional[_Union[_cluster_pb2.Access, _Mapping]] = ..., private_connection_info: _Optional[_Union[PrivateConnectionInfo, _Mapping]] = ..., encryption: _Optional[_Union[_cluster_pb2.DataEncryption, _Mapping]] = ..., network_id: _Optional[str] = ..., clickhouse_config: _Optional[_Union[_config_pb2.ClickhouseConfig, _Mapping]] = ..., maintenance_window: _Optional[_Union[_maintenance_pb2.MaintenanceWindow, _Mapping]] = ..., maintenance_operation: _Optional[_Union[_maintenance_pb2.MaintenanceOperation, _Mapping]] = ..., metrics_exporter_connection_info: _Optional[_Union[MetricsExporterConnectionInfo, _Mapping]] = ..., custom_certificate: _Optional[_Union[CustomCertificate, _Mapping]] = ...) -> None: ...

class ClusterResources(_message.Message):
    __slots__ = ("clickhouse", "dedicated_keeper")
    class Clickhouse(_message.Message):
        __slots__ = ("resource_preset_id", "disk_size", "replica_count", "shard_count", "max_disk_size", "min_resource_preset_id", "max_resource_preset_id")
        RESOURCE_PRESET_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
        SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
        MAX_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        MIN_RESOURCE_PRESET_ID_FIELD_NUMBER: _ClassVar[int]
        MAX_RESOURCE_PRESET_ID_FIELD_NUMBER: _ClassVar[int]
        resource_preset_id: str
        disk_size: _wrappers_pb2.Int64Value
        replica_count: _wrappers_pb2.Int64Value
        shard_count: _wrappers_pb2.Int64Value
        max_disk_size: _wrappers_pb2.Int64Value
        min_resource_preset_id: _wrappers_pb2.StringValue
        max_resource_preset_id: _wrappers_pb2.StringValue
        def __init__(self, resource_preset_id: _Optional[str] = ..., disk_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., replica_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., shard_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_disk_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., min_resource_preset_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., max_resource_preset_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
    class Keeper(_message.Message):
        __slots__ = ("resource_preset_id", "disk_size", "replica_count", "max_disk_size", "min_resource_preset_id", "max_resource_preset_id")
        RESOURCE_PRESET_ID_FIELD_NUMBER: _ClassVar[int]
        DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
        MAX_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        MIN_RESOURCE_PRESET_ID_FIELD_NUMBER: _ClassVar[int]
        MAX_RESOURCE_PRESET_ID_FIELD_NUMBER: _ClassVar[int]
        resource_preset_id: str
        disk_size: _wrappers_pb2.Int64Value
        replica_count: _wrappers_pb2.Int64Value
        max_disk_size: _wrappers_pb2.Int64Value
        min_resource_preset_id: _wrappers_pb2.StringValue
        max_resource_preset_id: _wrappers_pb2.StringValue
        def __init__(self, resource_preset_id: _Optional[str] = ..., disk_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., replica_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max_disk_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., min_resource_preset_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., max_resource_preset_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
    CLICKHOUSE_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_KEEPER_FIELD_NUMBER: _ClassVar[int]
    clickhouse: ClusterResources.Clickhouse
    dedicated_keeper: ClusterResources.Keeper
    def __init__(self, clickhouse: _Optional[_Union[ClusterResources.Clickhouse, _Mapping]] = ..., dedicated_keeper: _Optional[_Union[ClusterResources.Keeper, _Mapping]] = ...) -> None: ...

class ConnectionInfo(_message.Message):
    __slots__ = ("host", "user", "password", "https_port", "tcp_port_secure", "native_protocol", "https_uri", "jdbc_uri", "odbc_uri")
    HOST_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    HTTPS_PORT_FIELD_NUMBER: _ClassVar[int]
    TCP_PORT_SECURE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    HTTPS_URI_FIELD_NUMBER: _ClassVar[int]
    JDBC_URI_FIELD_NUMBER: _ClassVar[int]
    ODBC_URI_FIELD_NUMBER: _ClassVar[int]
    host: str
    user: str
    password: str
    https_port: _wrappers_pb2.Int64Value
    tcp_port_secure: _wrappers_pb2.Int64Value
    native_protocol: str
    https_uri: str
    jdbc_uri: str
    odbc_uri: str
    def __init__(self, host: _Optional[str] = ..., user: _Optional[str] = ..., password: _Optional[str] = ..., https_port: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., tcp_port_secure: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., native_protocol: _Optional[str] = ..., https_uri: _Optional[str] = ..., jdbc_uri: _Optional[str] = ..., odbc_uri: _Optional[str] = ...) -> None: ...

class PrivateConnectionInfo(_message.Message):
    __slots__ = ("host", "user", "password", "https_port", "tcp_port_secure", "native_protocol", "https_uri", "jdbc_uri", "odbc_uri")
    HOST_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    HTTPS_PORT_FIELD_NUMBER: _ClassVar[int]
    TCP_PORT_SECURE_FIELD_NUMBER: _ClassVar[int]
    NATIVE_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    HTTPS_URI_FIELD_NUMBER: _ClassVar[int]
    JDBC_URI_FIELD_NUMBER: _ClassVar[int]
    ODBC_URI_FIELD_NUMBER: _ClassVar[int]
    host: str
    user: str
    password: str
    https_port: _wrappers_pb2.Int64Value
    tcp_port_secure: _wrappers_pb2.Int64Value
    native_protocol: str
    https_uri: str
    jdbc_uri: str
    odbc_uri: str
    def __init__(self, host: _Optional[str] = ..., user: _Optional[str] = ..., password: _Optional[str] = ..., https_port: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., tcp_port_secure: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., native_protocol: _Optional[str] = ..., https_uri: _Optional[str] = ..., jdbc_uri: _Optional[str] = ..., odbc_uri: _Optional[str] = ...) -> None: ...

class MetricsExporterConnectionInfo(_message.Message):
    __slots__ = ("user", "password")
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    password: str
    def __init__(self, user: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class Host(_message.Message):
    __slots__ = ("name", "cluster_id", "shard_name", "private_name", "status")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    SHARD_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    cluster_id: str
    shard_name: str
    private_name: str
    status: _cluster_pb2.HostStatus
    def __init__(self, name: _Optional[str] = ..., cluster_id: _Optional[str] = ..., shard_name: _Optional[str] = ..., private_name: _Optional[str] = ..., status: _Optional[_Union[_cluster_pb2.HostStatus, str]] = ...) -> None: ...

class CustomCertificate(_message.Message):
    __slots__ = ("enabled", "certificate", "key", "root_ca")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ROOT_CA_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    certificate: _wrappers_pb2.BytesValue
    key: _wrappers_pb2.BytesValue
    root_ca: _wrappers_pb2.BytesValue
    def __init__(self, enabled: bool = ..., certificate: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., key: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., root_ca: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...
