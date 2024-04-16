from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("name", "cluster_id", "permissions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    cluster_id: str
    permissions: _containers.RepeatedCompositeFieldContainer[Permission]
    def __init__(self, name: _Optional[str] = ..., cluster_id: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[Permission, _Mapping]]] = ...) -> None: ...

class UserSpec(_message.Message):
    __slots__ = ("name", "password", "permissions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    password: str
    permissions: _containers.RepeatedCompositeFieldContainer[Permission]
    def __init__(self, name: _Optional[str] = ..., password: _Optional[str] = ..., permissions: _Optional[_Iterable[_Union[Permission, _Mapping]]] = ...) -> None: ...

class Permission(_message.Message):
    __slots__ = ("topic_name", "role")
    class AccessRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCESS_ROLE_INVALID: _ClassVar[Permission.AccessRole]
        ACCESS_ROLE_PRODUCER: _ClassVar[Permission.AccessRole]
        ACCESS_ROLE_CONSUMER: _ClassVar[Permission.AccessRole]
        ACCESS_ROLE_ADMIN: _ClassVar[Permission.AccessRole]
    ACCESS_ROLE_INVALID: Permission.AccessRole
    ACCESS_ROLE_PRODUCER: Permission.AccessRole
    ACCESS_ROLE_CONSUMER: Permission.AccessRole
    ACCESS_ROLE_ADMIN: Permission.AccessRole
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    topic_name: str
    role: Permission.AccessRole
    def __init__(self, topic_name: _Optional[str] = ..., role: _Optional[_Union[Permission.AccessRole, str]] = ...) -> None: ...
