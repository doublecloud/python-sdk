from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Backup(_message.Message):
    __slots__ = ("id", "project_id", "name", "create_time", "start_time", "source_cluster_id", "size", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_INVALID: _ClassVar[Backup.Type]
        TYPE_AUTOMATED: _ClassVar[Backup.Type]
        TYPE_MANUAL: _ClassVar[Backup.Type]
    TYPE_INVALID: Backup.Type
    TYPE_AUTOMATED: Backup.Type
    TYPE_MANUAL: Backup.Type
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    name: str
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    source_cluster_id: str
    size: int
    type: Backup.Type
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., name: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., source_cluster_id: _Optional[str] = ..., size: _Optional[int] = ..., type: _Optional[_Union[Backup.Type, str]] = ...) -> None: ...
