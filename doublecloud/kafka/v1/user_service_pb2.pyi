from doublecloud.v1 import operation_pb2 as _operation_pb2
from doublecloud.v1 import paging_pb2 as _paging_pb2
from doublecloud.kafka.v1 import user_pb2 as _user_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
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
    __slots__ = ("cluster_id", "user_spec")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_SPEC_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    user_spec: _user_pb2.UserSpec
    def __init__(self, cluster_id: _Optional[str] = ..., user_spec: _Optional[_Union[_user_pb2.UserSpec, _Mapping]] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("cluster_id", "user_name", "update_spec")
    class UpdateSpec(_message.Message):
        __slots__ = ("password", "permissions")
        class UpdatePermissions(_message.Message):
            __slots__ = ("permissions",)
            PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
            permissions: _containers.RepeatedCompositeFieldContainer[_user_pb2.Permission]
            def __init__(self, permissions: _Optional[_Iterable[_Union[_user_pb2.Permission, _Mapping]]] = ...) -> None: ...
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        password: _wrappers_pb2.StringValue
        permissions: UpdateUserRequest.UpdateSpec.UpdatePermissions
        def __init__(self, password: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., permissions: _Optional[_Union[UpdateUserRequest.UpdateSpec.UpdatePermissions, _Mapping]] = ...) -> None: ...
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_SPEC_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    user_name: str
    update_spec: UpdateUserRequest.UpdateSpec
    def __init__(self, cluster_id: _Optional[str] = ..., user_name: _Optional[str] = ..., update_spec: _Optional[_Union[UpdateUserRequest.UpdateSpec, _Mapping]] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("cluster_id", "user_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    user_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., user_name: _Optional[str] = ...) -> None: ...

class GrantUserPermissionRequest(_message.Message):
    __slots__ = ("cluster_id", "user_name", "permission")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    user_name: str
    permission: _user_pb2.Permission
    def __init__(self, cluster_id: _Optional[str] = ..., user_name: _Optional[str] = ..., permission: _Optional[_Union[_user_pb2.Permission, _Mapping]] = ...) -> None: ...

class RevokeUserPermissionRequest(_message.Message):
    __slots__ = ("cluster_id", "user_name", "permission")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    user_name: str
    permission: _user_pb2.Permission
    def __init__(self, cluster_id: _Optional[str] = ..., user_name: _Optional[str] = ..., permission: _Optional[_Union[_user_pb2.Permission, _Mapping]] = ...) -> None: ...
