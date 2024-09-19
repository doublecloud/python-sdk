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

from doublecloud.v1 import cluster_pb2 as _cluster_pb2
from doublecloud.v1 import maintenance_pb2 as _maintenance_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Cluster(_message.Message):
    __slots__ = ("id", "project_id", "cloud_type", "region_id", "create_time", "name", "description", "status", "resources", "connection_info", "access", "config", "network_id", "maintenance_window", "cr_connection_info", "managed_image_status")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TYPE_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    CR_CONNECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    MANAGED_IMAGE_STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    cloud_type: str
    region_id: str
    create_time: _timestamp_pb2.Timestamp
    name: str
    description: str
    status: _cluster_pb2.ClusterStatus
    resources: ClusterResources
    connection_info: ConnectionInfo
    access: _cluster_pb2.Access
    config: AirflowConfig
    network_id: str
    maintenance_window: _maintenance_pb2.MaintenanceWindow
    cr_connection_info: CrConnectionInfo
    managed_image_status: ManagedImageStatus
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., cloud_type: _Optional[str] = ..., region_id: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[_Union[_cluster_pb2.ClusterStatus, str]] = ..., resources: _Optional[_Union[ClusterResources, _Mapping]] = ..., connection_info: _Optional[_Union[ConnectionInfo, _Mapping]] = ..., access: _Optional[_Union[_cluster_pb2.Access, _Mapping]] = ..., config: _Optional[_Union[AirflowConfig, _Mapping]] = ..., network_id: _Optional[str] = ..., maintenance_window: _Optional[_Union[_maintenance_pb2.MaintenanceWindow, _Mapping]] = ..., cr_connection_info: _Optional[_Union[CrConnectionInfo, _Mapping]] = ..., managed_image_status: _Optional[_Union[ManagedImageStatus, _Mapping]] = ...) -> None: ...

class AirflowEnvVariable(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ManagedImageStatus(_message.Message):
    __slots__ = ("build_errors", "applied_requirements_txt")
    BUILD_ERRORS_FIELD_NUMBER: _ClassVar[int]
    APPLIED_REQUIREMENTS_TXT_FIELD_NUMBER: _ClassVar[int]
    build_errors: str
    applied_requirements_txt: str
    def __init__(self, build_errors: _Optional[str] = ..., applied_requirements_txt: _Optional[str] = ...) -> None: ...

class ClusterResources(_message.Message):
    __slots__ = ("airflow",)
    class Airflow(_message.Message):
        __slots__ = ("max_worker_count", "environment_flavor", "min_worker_count", "worker_concurrency", "worker_disk_size", "worker_preset")
        MAX_WORKER_COUNT_FIELD_NUMBER: _ClassVar[int]
        ENVIRONMENT_FLAVOR_FIELD_NUMBER: _ClassVar[int]
        MIN_WORKER_COUNT_FIELD_NUMBER: _ClassVar[int]
        WORKER_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
        WORKER_DISK_SIZE_FIELD_NUMBER: _ClassVar[int]
        WORKER_PRESET_FIELD_NUMBER: _ClassVar[int]
        max_worker_count: _wrappers_pb2.Int64Value
        environment_flavor: str
        min_worker_count: _wrappers_pb2.Int64Value
        worker_concurrency: _wrappers_pb2.Int64Value
        worker_disk_size: _wrappers_pb2.Int64Value
        worker_preset: str
        def __init__(self, max_worker_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., environment_flavor: _Optional[str] = ..., min_worker_count: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., worker_concurrency: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., worker_disk_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., worker_preset: _Optional[str] = ...) -> None: ...
    AIRFLOW_FIELD_NUMBER: _ClassVar[int]
    airflow: ClusterResources.Airflow
    def __init__(self, airflow: _Optional[_Union[ClusterResources.Airflow, _Mapping]] = ...) -> None: ...

class ConnectionInfo(_message.Message):
    __slots__ = ("host", "user", "password")
    HOST_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    host: str
    user: str
    password: str
    def __init__(self, host: _Optional[str] = ..., user: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class CrConnectionInfo(_message.Message):
    __slots__ = ("remote_image_path", "user", "password")
    REMOTE_IMAGE_PATH_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    remote_image_path: str
    user: str
    password: str
    def __init__(self, remote_image_path: _Optional[str] = ..., user: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class SyncConfig(_message.Message):
    __slots__ = ("repo_url", "branch", "revision", "dags_path", "api_credentials")
    REPO_URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    DAGS_PATH_FIELD_NUMBER: _ClassVar[int]
    API_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    repo_url: str
    branch: str
    revision: str
    dags_path: str
    api_credentials: GitApiCredentials
    def __init__(self, repo_url: _Optional[str] = ..., branch: _Optional[str] = ..., revision: _Optional[str] = ..., dags_path: _Optional[str] = ..., api_credentials: _Optional[_Union[GitApiCredentials, _Mapping]] = ...) -> None: ...

class GitApiCredentials(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AirflowConfig(_message.Message):
    __slots__ = ("version_id", "git_sync", "custom_image_digest", "managed_requirements_txt", "user_service_account_id", "env_vars")
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    GIT_SYNC_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_IMAGE_DIGEST_FIELD_NUMBER: _ClassVar[int]
    MANAGED_REQUIREMENTS_TXT_FIELD_NUMBER: _ClassVar[int]
    USER_SERVICE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ENV_VARS_FIELD_NUMBER: _ClassVar[int]
    version_id: str
    git_sync: SyncConfig
    custom_image_digest: str
    managed_requirements_txt: str
    user_service_account_id: str
    env_vars: _containers.RepeatedCompositeFieldContainer[AirflowEnvVariable]
    def __init__(self, version_id: _Optional[str] = ..., git_sync: _Optional[_Union[SyncConfig, _Mapping]] = ..., custom_image_digest: _Optional[str] = ..., managed_requirements_txt: _Optional[str] = ..., user_service_account_id: _Optional[str] = ..., env_vars: _Optional[_Iterable[_Union[AirflowEnvVariable, _Mapping]]] = ...) -> None: ...
