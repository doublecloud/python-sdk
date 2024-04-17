from google.protobuf import timestamp_pb2 as _timestamp_pb2
from doublecloud.v1 import cluster_pb2 as _cluster_pb2
from doublecloud.v1 import maintenance_pb2 as _maintenance_pb2
from doublecloud.v1 import operation_pb2 as _operation_pb2
from doublecloud.v1 import paging_pb2 as _paging_pb2
from doublecloud.kafka.v1 import cluster_pb2 as _cluster_pb2_1
from doublecloud.kafka.v1 import config_pb2 as _config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_VIEW_INVALID: _ClassVar[ClusterView]
    CLUSTER_VIEW_BASIC: _ClassVar[ClusterView]
    CLUSTER_VIEW_FULL: _ClassVar[ClusterView]
CLUSTER_VIEW_INVALID: ClusterView
CLUSTER_VIEW_BASIC: ClusterView
CLUSTER_VIEW_FULL: ClusterView

class GetClusterRequest(_message.Message):
    __slots__ = ("cluster_id", "sensitive")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    sensitive: bool
    def __init__(self, cluster_id: _Optional[str] = ..., sensitive: bool = ...) -> None: ...

class ListClustersRequest(_message.Message):
    __slots__ = ("project_id", "paging", "view")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    paging: _paging_pb2.Paging
    view: ClusterView
    def __init__(self, project_id: _Optional[str] = ..., paging: _Optional[_Union[_paging_pb2.Paging, _Mapping]] = ..., view: _Optional[_Union[ClusterView, str]] = ...) -> None: ...

class ListClustersResponse(_message.Message):
    __slots__ = ("clusters", "next_page")
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[_cluster_pb2_1.Cluster]
    next_page: _paging_pb2.NextPage
    def __init__(self, clusters: _Optional[_Iterable[_Union[_cluster_pb2_1.Cluster, _Mapping]]] = ..., next_page: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ...) -> None: ...

class CreateClusterRequest(_message.Message):
    __slots__ = ("project_id", "cloud_type", "region_id", "name", "description", "version", "resources", "access", "encryption", "network_id", "maintenance_window", "kafka_config", "schema_registry_config", "rest_api_config")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TYPE_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    KAFKA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_REGISTRY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REST_API_CONFIG_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    cloud_type: str
    region_id: str
    name: str
    description: str
    version: str
    resources: _cluster_pb2_1.ClusterResources
    access: _cluster_pb2.Access
    encryption: _cluster_pb2.DataEncryption
    network_id: str
    maintenance_window: _maintenance_pb2.MaintenanceWindow
    kafka_config: _config_pb2.KafkaConfig
    schema_registry_config: _config_pb2.SchemaRegistryConfig
    rest_api_config: _config_pb2.RestAPIConfig
    def __init__(self, project_id: _Optional[str] = ..., cloud_type: _Optional[str] = ..., region_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., version: _Optional[str] = ..., resources: _Optional[_Union[_cluster_pb2_1.ClusterResources, _Mapping]] = ..., access: _Optional[_Union[_cluster_pb2.Access, _Mapping]] = ..., encryption: _Optional[_Union[_cluster_pb2.DataEncryption, _Mapping]] = ..., network_id: _Optional[str] = ..., maintenance_window: _Optional[_Union[_maintenance_pb2.MaintenanceWindow, _Mapping]] = ..., kafka_config: _Optional[_Union[_config_pb2.KafkaConfig, _Mapping]] = ..., schema_registry_config: _Optional[_Union[_config_pb2.SchemaRegistryConfig, _Mapping]] = ..., rest_api_config: _Optional[_Union[_config_pb2.RestAPIConfig, _Mapping]] = ...) -> None: ...

class UpdateClusterRequest(_message.Message):
    __slots__ = ("cluster_id", "name", "description", "version", "resources", "access", "maintenance_window", "kafka_config", "schema_registry_config", "rest_api_config")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    KAFKA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_REGISTRY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REST_API_CONFIG_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    name: str
    description: str
    version: str
    resources: _cluster_pb2_1.ClusterResources
    access: _cluster_pb2.Access
    maintenance_window: _maintenance_pb2.MaintenanceWindow
    kafka_config: _config_pb2.KafkaConfig
    schema_registry_config: _config_pb2.SchemaRegistryConfig
    rest_api_config: _config_pb2.RestAPIConfig
    def __init__(self, cluster_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., version: _Optional[str] = ..., resources: _Optional[_Union[_cluster_pb2_1.ClusterResources, _Mapping]] = ..., access: _Optional[_Union[_cluster_pb2.Access, _Mapping]] = ..., maintenance_window: _Optional[_Union[_maintenance_pb2.MaintenanceWindow, _Mapping]] = ..., kafka_config: _Optional[_Union[_config_pb2.KafkaConfig, _Mapping]] = ..., schema_registry_config: _Optional[_Union[_config_pb2.SchemaRegistryConfig, _Mapping]] = ..., rest_api_config: _Optional[_Union[_config_pb2.RestAPIConfig, _Mapping]] = ...) -> None: ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ("cluster_id",)
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    def __init__(self, cluster_id: _Optional[str] = ...) -> None: ...

class ResetClusterCredentialsRequest(_message.Message):
    __slots__ = ("cluster_id",)
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    def __init__(self, cluster_id: _Optional[str] = ...) -> None: ...

class ListClusterHostsRequest(_message.Message):
    __slots__ = ("cluster_id", "paging")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    paging: _paging_pb2.Paging
    def __init__(self, cluster_id: _Optional[str] = ..., paging: _Optional[_Union[_paging_pb2.Paging, _Mapping]] = ...) -> None: ...

class ListClusterHostsResponse(_message.Message):
    __slots__ = ("hosts", "next_page")
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    hosts: _containers.RepeatedCompositeFieldContainer[_cluster_pb2_1.Host]
    next_page: _paging_pb2.NextPage
    def __init__(self, hosts: _Optional[_Iterable[_Union[_cluster_pb2_1.Host, _Mapping]]] = ..., next_page: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ...) -> None: ...

class StartClusterRequest(_message.Message):
    __slots__ = ("cluster_id",)
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    def __init__(self, cluster_id: _Optional[str] = ...) -> None: ...

class StopClusterRequest(_message.Message):
    __slots__ = ("cluster_id",)
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    def __init__(self, cluster_id: _Optional[str] = ...) -> None: ...

class RescheduleMaintenanceRequest(_message.Message):
    __slots__ = ("cluster_id", "reschedule_type", "delayed_until_time")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RESCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELAYED_UNTIL_TIME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    reschedule_type: _maintenance_pb2.RescheduleType
    delayed_until_time: _timestamp_pb2.Timestamp
    def __init__(self, cluster_id: _Optional[str] = ..., reschedule_type: _Optional[_Union[_maintenance_pb2.RescheduleType, str]] = ..., delayed_until_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListClusterOperationsRequest(_message.Message):
    __slots__ = ("cluster_id", "paging")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    paging: _paging_pb2.Paging
    def __init__(self, cluster_id: _Optional[str] = ..., paging: _Optional[_Union[_paging_pb2.Paging, _Mapping]] = ...) -> None: ...

class ListClusterOperationsResponse(_message.Message):
    __slots__ = ("operations", "next_page")
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[_operation_pb2.Operation]
    next_page: _paging_pb2.NextPage
    def __init__(self, operations: _Optional[_Iterable[_Union[_operation_pb2.Operation, _Mapping]]] = ..., next_page: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ...) -> None: ...
