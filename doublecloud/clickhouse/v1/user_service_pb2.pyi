from doublecloud.v1 import operation_pb2 as _operation_pb2
from doublecloud.v1 import paging_pb2 as _paging_pb2
from doublecloud.clickhouse.v1 import user_pb2 as _user_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUserRequest(_message.Message):
    __slots__ = ("cluster_id", "user_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    user_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., user_name: _Optional[str] = ...) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = ("cluster_id", "paging")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    paging: _paging_pb2.Paging
    def __init__(self, cluster_id: _Optional[str] = ..., paging: _Optional[_Union[_paging_pb2.Paging, _Mapping]] = ...) -> None: ...

class ListUsersResponse(_message.Message):
    __slots__ = ("users", "next_page")
    USERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    next_page: _paging_pb2.NextPage
    def __init__(self, users: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ..., next_page: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("cluster_id", "user_name", "authentication", "default_roles", "grantees", "privileges", "settings", "quota_names", "assigned_roles")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ROLES_FIELD_NUMBER: _ClassVar[int]
    GRANTEES_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    QUOTA_NAMES_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_ROLES_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    user_name: str
    authentication: _user_pb2.Authentication
    default_roles: _user_pb2.DefaultRoles
    grantees: _user_pb2.Grantees
    privileges: _user_pb2.Privileges
    settings: _user_pb2.Settings
    quota_names: _user_pb2.QuotaNames
    assigned_roles: _user_pb2.AssignedRoles
    def __init__(self, cluster_id: _Optional[str] = ..., user_name: _Optional[str] = ..., authentication: _Optional[_Union[_user_pb2.Authentication, _Mapping]] = ..., default_roles: _Optional[_Union[_user_pb2.DefaultRoles, _Mapping]] = ..., grantees: _Optional[_Union[_user_pb2.Grantees, _Mapping]] = ..., privileges: _Optional[_Union[_user_pb2.Privileges, _Mapping]] = ..., settings: _Optional[_Union[_user_pb2.Settings, _Mapping]] = ..., quota_names: _Optional[_Union[_user_pb2.QuotaNames, _Mapping]] = ..., assigned_roles: _Optional[_Union[_user_pb2.AssignedRoles, _Mapping]] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("cluster_id", "user_name", "authentication", "default_roles", "grantees", "privileges", "settings", "quota_names", "assigned_roles")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ROLES_FIELD_NUMBER: _ClassVar[int]
    GRANTEES_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    QUOTA_NAMES_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_ROLES_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    user_name: str
    authentication: _user_pb2.Authentication
    default_roles: _user_pb2.DefaultRoles
    grantees: _user_pb2.Grantees
    privileges: _user_pb2.Privileges
    settings: _user_pb2.Settings
    quota_names: _user_pb2.QuotaNames
    assigned_roles: _user_pb2.AssignedRoles
    def __init__(self, cluster_id: _Optional[str] = ..., user_name: _Optional[str] = ..., authentication: _Optional[_Union[_user_pb2.Authentication, _Mapping]] = ..., default_roles: _Optional[_Union[_user_pb2.DefaultRoles, _Mapping]] = ..., grantees: _Optional[_Union[_user_pb2.Grantees, _Mapping]] = ..., privileges: _Optional[_Union[_user_pb2.Privileges, _Mapping]] = ..., settings: _Optional[_Union[_user_pb2.Settings, _Mapping]] = ..., quota_names: _Optional[_Union[_user_pb2.QuotaNames, _Mapping]] = ..., assigned_roles: _Optional[_Union[_user_pb2.AssignedRoles, _Mapping]] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("cluster_id", "user_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    user_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., user_name: _Optional[str] = ...) -> None: ...

class GetRoleRequest(_message.Message):
    __slots__ = ("cluster_id", "role_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    role_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., role_name: _Optional[str] = ...) -> None: ...

class ListRolesRequest(_message.Message):
    __slots__ = ("cluster_id", "paging")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    paging: _paging_pb2.Paging
    def __init__(self, cluster_id: _Optional[str] = ..., paging: _Optional[_Union[_paging_pb2.Paging, _Mapping]] = ...) -> None: ...

class ListRolesResponse(_message.Message):
    __slots__ = ("roles", "next_page")
    ROLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[_user_pb2.Role]
    next_page: _paging_pb2.NextPage
    def __init__(self, roles: _Optional[_Iterable[_Union[_user_pb2.Role, _Mapping]]] = ..., next_page: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ...) -> None: ...

class CreateRoleRequest(_message.Message):
    __slots__ = ("cluster_id", "role_name", "privileges", "settings", "quota_names")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    QUOTA_NAMES_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    role_name: str
    privileges: _user_pb2.Privileges
    settings: _user_pb2.Settings
    quota_names: _user_pb2.QuotaNames
    def __init__(self, cluster_id: _Optional[str] = ..., role_name: _Optional[str] = ..., privileges: _Optional[_Union[_user_pb2.Privileges, _Mapping]] = ..., settings: _Optional[_Union[_user_pb2.Settings, _Mapping]] = ..., quota_names: _Optional[_Union[_user_pb2.QuotaNames, _Mapping]] = ...) -> None: ...

class UpdateRoleRequest(_message.Message):
    __slots__ = ("cluster_id", "role_name", "privileges", "settings", "quota_names")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    QUOTA_NAMES_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    role_name: str
    privileges: _user_pb2.Privileges
    settings: _user_pb2.Settings
    quota_names: _user_pb2.QuotaNames
    def __init__(self, cluster_id: _Optional[str] = ..., role_name: _Optional[str] = ..., privileges: _Optional[_Union[_user_pb2.Privileges, _Mapping]] = ..., settings: _Optional[_Union[_user_pb2.Settings, _Mapping]] = ..., quota_names: _Optional[_Union[_user_pb2.QuotaNames, _Mapping]] = ...) -> None: ...

class DeleteRoleRequest(_message.Message):
    __slots__ = ("cluster_id", "role_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    role_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., role_name: _Optional[str] = ...) -> None: ...
