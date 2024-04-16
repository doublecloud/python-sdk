from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Operation(_message.Message):
    __slots__ = ("id", "project_id", "description", "created_by", "metadata", "create_time", "start_time", "finish_time", "status", "error", "resource_id")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_INVALID: _ClassVar[Operation.Status]
        STATUS_PENDING: _ClassVar[Operation.Status]
        STATUS_RUNNING: _ClassVar[Operation.Status]
        STATUS_DONE: _ClassVar[Operation.Status]
    STATUS_INVALID: Operation.Status
    STATUS_PENDING: Operation.Status
    STATUS_RUNNING: Operation.Status
    STATUS_DONE: Operation.Status
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    description: str
    created_by: str
    metadata: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    finish_time: _timestamp_pb2.Timestamp
    status: Operation.Status
    error: _status_pb2.Status
    resource_id: str
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., description: _Optional[str] = ..., created_by: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., finish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[Operation.Status, str]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ..., resource_id: _Optional[str] = ...) -> None: ...
