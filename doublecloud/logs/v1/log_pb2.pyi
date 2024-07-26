from google.protobuf import timestamp_pb2 as _timestamp_pb2
from doublecloud.logs.v1 import log_source_pb2 as _log_source_pb2
from doublecloud.v1 import paging_pb2 as _paging_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SortOrder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SORT_ORDER_INVALID: _ClassVar[SortOrder]
    SORT_ORDER_ASCENDING: _ClassVar[SortOrder]
    SORT_ORDER_DESCENDING: _ClassVar[SortOrder]

class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG_LEVEL_DEFAULT: _ClassVar[LogLevel]
    LOG_LEVEL_DEBUG: _ClassVar[LogLevel]
    LOG_LEVEL_INFO: _ClassVar[LogLevel]
    LOG_LEVEL_WARN: _ClassVar[LogLevel]
    LOG_LEVEL_ERROR: _ClassVar[LogLevel]
    LOG_LEVEL_FATAL: _ClassVar[LogLevel]
SORT_ORDER_INVALID: SortOrder
SORT_ORDER_ASCENDING: SortOrder
SORT_ORDER_DESCENDING: SortOrder
LOG_LEVEL_DEFAULT: LogLevel
LOG_LEVEL_DEBUG: LogLevel
LOG_LEVEL_INFO: LogLevel
LOG_LEVEL_WARN: LogLevel
LOG_LEVEL_ERROR: LogLevel
LOG_LEVEL_FATAL: LogLevel

class Criteria(_message.Message):
    __slots__ = ("sources", "from_time", "to_time", "levels", "filter", "sort_order", "paging")
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    FROM_TIME_FIELD_NUMBER: _ClassVar[int]
    TO_TIME_FIELD_NUMBER: _ClassVar[int]
    LEVELS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[_log_source_pb2.LogSource]
    from_time: _timestamp_pb2.Timestamp
    to_time: _timestamp_pb2.Timestamp
    levels: _containers.RepeatedScalarFieldContainer[LogLevel]
    filter: str
    sort_order: SortOrder
    paging: _paging_pb2.NextPage
    def __init__(self, sources: _Optional[_Iterable[_Union[_log_source_pb2.LogSource, _Mapping]]] = ..., from_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., to_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., levels: _Optional[_Iterable[_Union[LogLevel, str]]] = ..., filter: _Optional[str] = ..., sort_order: _Optional[_Union[SortOrder, str]] = ..., paging: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ...) -> None: ...

class LogRecord(_message.Message):
    __slots__ = ("source", "instance", "record_time", "level", "message")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    RECORD_TIME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    source: _log_source_pb2.LogSource
    instance: str
    record_time: _timestamp_pb2.Timestamp
    level: LogLevel
    message: str
    def __init__(self, source: _Optional[_Union[_log_source_pb2.LogSource, _Mapping]] = ..., instance: _Optional[str] = ..., record_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., level: _Optional[_Union[LogLevel, str]] = ..., message: _Optional[str] = ...) -> None: ...
