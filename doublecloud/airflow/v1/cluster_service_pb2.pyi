from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from doublecloud.airflow.v1 import cluster_pb2 as _cluster_pb2_1
from doublecloud.v1 import cluster_pb2 as _cluster_pb2
from doublecloud.v1 import maintenance_pb2 as _maintenance_pb2
from doublecloud.v1 import operation_pb2 as _operation_pb2
from doublecloud.v1 import paging_pb2 as _paging_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_VIEW_INVALID: _ClassVar[ClusterView]
    CLUSTER_VIEW_BASIC: _ClassVar[ClusterView]
    CLUSTER_VIEW_FULL: _ClassVar[ClusterView]
CLUSTER_VIEW_INVALID: ClusterView
CLUSTER_VIEW_BASIC: ClusterView
CLUSTER_VIEW_FULL: ClusterView

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

class ListCustomImagesRequest(_message.Message):
    __slots__ = ("cluster_id",)
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    def __init__(self, cluster_id: _Optional[str] = ...) -> None: ...

class ListCustomImagesResponse(_message.Message):
    __slots__ = ("custom_images",)
    CUSTOM_IMAGES_FIELD_NUMBER: _ClassVar[int]
    custom_images: _containers.RepeatedCompositeFieldContainer[CustomImage]
    def __init__(self, custom_images: _Optional[_Iterable[_Union[CustomImage, _Mapping]]] = ...) -> None: ...

class CustomImage(_message.Message):
    __slots__ = ("digest", "airflow_version", "tags", "created_time")
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    AIRFLOW_VERSION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_FIELD_NUMBER: _ClassVar[int]
    digest: str
    airflow_version: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    created_time: _timestamp_pb2.Timestamp
    def __init__(self, digest: _Optional[str] = ..., airflow_version: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., created_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("project_id", "cloud_type", "region_id", "name", "description", "resources", "access", "config", "network_id", "maintenance_window")
    class AirflowConfig(_message.Message):
        __slots__ = ("version_id", "git_sync", "requirements_txt", "user_service_account_id", "env_vars")
        VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        GIT_SYNC_FIELD_NUMBER: _ClassVar[int]
        REQUIREMENTS_TXT_FIELD_NUMBER: _ClassVar[int]
        USER_SERVICE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        ENV_VARS_FIELD_NUMBER: _ClassVar[int]
        version_id: str
        git_sync: _cluster_pb2_1.SyncConfig
        requirements_txt: str
        user_service_account_id: str
        env_vars: _containers.RepeatedCompositeFieldContainer[_cluster_pb2_1.AirflowEnvVariable]
        def __init__(self, version_id: _Optional[str] = ..., git_sync: _Optional[_Union[_cluster_pb2_1.SyncConfig, _Mapping]] = ..., requirements_txt: _Optional[str] = ..., user_service_account_id: _Optional[str] = ..., env_vars: _Optional[_Iterable[_Union[_cluster_pb2_1.AirflowEnvVariable, _Mapping]]] = ...) -> None: ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TYPE_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    cloud_type: str
    region_id: str
    name: str
    description: str
    resources: _cluster_pb2_1.ClusterResources
    access: _cluster_pb2.Access
    config: CreateClusterRequest.AirflowConfig
    network_id: str
    maintenance_window: _maintenance_pb2.MaintenanceWindow
    def __init__(self, project_id: _Optional[str] = ..., cloud_type: _Optional[str] = ..., region_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., resources: _Optional[_Union[_cluster_pb2_1.ClusterResources, _Mapping]] = ..., access: _Optional[_Union[_cluster_pb2.Access, _Mapping]] = ..., config: _Optional[_Union[CreateClusterRequest.AirflowConfig, _Mapping]] = ..., network_id: _Optional[str] = ..., maintenance_window: _Optional[_Union[_maintenance_pb2.MaintenanceWindow, _Mapping]] = ...) -> None: ...

class CreateClusterMetadata(_message.Message):
    __slots__ = ("cluster_id",)
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    def __init__(self, cluster_id: _Optional[str] = ...) -> None: ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ("cluster_id",)
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    def __init__(self, cluster_id: _Optional[str] = ...) -> None: ...

class DeleteClusterMetadata(_message.Message):
    __slots__ = ("cluster_id",)
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    def __init__(self, cluster_id: _Optional[str] = ...) -> None: ...

class UpdateClusterRequest(_message.Message):
    __slots__ = ("cluster_id", "description", "resources", "access", "maintenance_window", "config", "name")
    class UpdateClusterResources(_message.Message):
        __slots__ = ("airflow",)
        class Airflow(_message.Message):
            __slots__ = ("max_worker_count", "min_worker_count", "worker_concurrency", "worker_disk_size", "worker_preset")
            MAX_WORKER_COUNT_FIELD_NUMBER: _ClassVar[int]
            MIN_WORKER_COUNT_FIELD_NUMBER: _ClassVar[int]
            WORKER_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
            WORKER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
            WORKER_PRESET_FIELD_NUMBER: _ClassVar[int]
            max_worker_count: _wrappers_pb2.Int64Value
            min_worker_count: _wrappers_pb2.Int64Value
            worker_concurrency: _wrappers_pb2.Int64Value
            worker_disk_size: _wrappers_pb2.Int64Value
            worker_preset: _wrappers_pb2.StringValue
            def __init__(self, max_worker_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., min_worker_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., worker_concurrency: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., worker_disk_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., worker_preset: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
        AIRFLOW_FIELD_NUMBER: _ClassVar[int]
        airflow: UpdateClusterRequest.UpdateClusterResources.Airflow
        def __init__(self, airflow: _Optional[_Union[UpdateClusterRequest.UpdateClusterResources.Airflow, _Mapping]] = ...) -> None: ...
    class UpdateAirflowConfig(_message.Message):
        __slots__ = ("git_sync", "custom_image_digest", "requirements_txt", "user_service_account_id", "env_vars")
        class UpdateGitSyncConfig(_message.Message):
            __slots__ = ("git_sync",)
            GIT_SYNC_FIELD_NUMBER: _ClassVar[int]
            git_sync: _cluster_pb2_1.SyncConfig
            def __init__(self, git_sync: _Optional[_Union[_cluster_pb2_1.SyncConfig, _Mapping]] = ...) -> None: ...
        GIT_SYNC_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_IMAGE_DIGEST_FIELD_NUMBER: _ClassVar[int]
        REQUIREMENTS_TXT_FIELD_NUMBER: _ClassVar[int]
        USER_SERVICE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        ENV_VARS_FIELD_NUMBER: _ClassVar[int]
        git_sync: UpdateClusterRequest.UpdateAirflowConfig.UpdateGitSyncConfig
        custom_image_digest: _wrappers_pb2.StringValue
        requirements_txt: _wrappers_pb2.StringValue
        user_service_account_id: _wrappers_pb2.StringValue
        env_vars: _containers.RepeatedCompositeFieldContainer[_cluster_pb2_1.AirflowEnvVariable]
        def __init__(self, git_sync: _Optional[_Union[UpdateClusterRequest.UpdateAirflowConfig.UpdateGitSyncConfig, _Mapping]] = ..., custom_image_digest: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., requirements_txt: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., user_service_account_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., env_vars: _Optional[_Iterable[_Union[_cluster_pb2_1.AirflowEnvVariable, _Mapping]]] = ...) -> None: ...
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    description: _wrappers_pb2.StringValue
    resources: UpdateClusterRequest.UpdateClusterResources
    access: _cluster_pb2.Access
    maintenance_window: _maintenance_pb2.MaintenanceWindow
    config: UpdateClusterRequest.UpdateAirflowConfig
    name: _wrappers_pb2.StringValue
    def __init__(self, cluster_id: _Optional[str] = ..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., resources: _Optional[_Union[UpdateClusterRequest.UpdateClusterResources, _Mapping]] = ..., access: _Optional[_Union[_cluster_pb2.Access, _Mapping]] = ..., maintenance_window: _Optional[_Union[_maintenance_pb2.MaintenanceWindow, _Mapping]] = ..., config: _Optional[_Union[UpdateClusterRequest.UpdateAirflowConfig, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class RescheduleMaintenanceRequest(_message.Message):
    __slots__ = ("cluster_id", "reschedule_type", "delayed_until_time")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    RESCHEDULE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DELAYED_UNTIL_TIME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    reschedule_type: _maintenance_pb2.RescheduleType
    delayed_until_time: _timestamp_pb2.Timestamp
    def __init__(self, cluster_id: _Optional[str] = ..., reschedule_type: _Optional[_Union[_maintenance_pb2.RescheduleType, str]] = ..., delayed_until_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RescheduleMaintenanceMetadata(_message.Message):
    __slots__ = ("cluster_id", "delayed_until_time")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    DELAYED_UNTIL_TIME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    delayed_until_time: _timestamp_pb2.Timestamp
    def __init__(self, cluster_id: _Optional[str] = ..., delayed_until_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
