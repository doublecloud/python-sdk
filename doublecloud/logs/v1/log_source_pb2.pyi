from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LogSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG_SOURCE_TYPE_INVALID: _ClassVar[LogSourceType]
    LOG_SOURCE_TYPE_CLICKHOUSE: _ClassVar[LogSourceType]
    LOG_SOURCE_TYPE_KAFKA: _ClassVar[LogSourceType]
    LOG_SOURCE_TYPE_TRANSFER: _ClassVar[LogSourceType]
LOG_SOURCE_TYPE_INVALID: LogSourceType
LOG_SOURCE_TYPE_CLICKHOUSE: LogSourceType
LOG_SOURCE_TYPE_KAFKA: LogSourceType
LOG_SOURCE_TYPE_TRANSFER: LogSourceType

class LogSource(_message.Message):
    __slots__ = ("type", "id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    type: LogSourceType
    id: str
    def __init__(self, type: _Optional[_Union[LogSourceType, str]] = ..., id: _Optional[str] = ...) -> None: ...
