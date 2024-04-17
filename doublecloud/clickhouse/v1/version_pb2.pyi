from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Version(_message.Message):
    __slots__ = ("id", "name", "deprecated", "updatable_to")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    UPDATABLE_TO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    deprecated: bool
    updatable_to: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., deprecated: bool = ..., updatable_to: _Optional[_Iterable[str]] = ...) -> None: ...
