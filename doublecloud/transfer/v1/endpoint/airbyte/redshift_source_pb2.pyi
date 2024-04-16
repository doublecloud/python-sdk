from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RedshiftSource(_message.Message):
    __slots__ = ("host", "port", "database", "schemas", "username", "password")
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    database: str
    schemas: _containers.RepeatedScalarFieldContainer[str]
    username: str
    password: str
    def __init__(self, host: _Optional[str] = ..., port: _Optional[int] = ..., database: _Optional[str] = ..., schemas: _Optional[_Iterable[str]] = ..., username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...
