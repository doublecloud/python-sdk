from doublecloud.v1 import operation_pb2 as _operation_pb2
from doublecloud.v1 import paging_pb2 as _paging_pb2
from doublecloud.logs.v1 import log_pb2 as _log_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadLogsRequest(_message.Message):
    __slots__ = ("paging", "criteria")
    PAGING_FIELD_NUMBER: _ClassVar[int]
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    paging: _paging_pb2.NextPage
    criteria: _log_pb2.Criteria
    def __init__(self, paging: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ..., criteria: _Optional[_Union[_log_pb2.Criteria, _Mapping]] = ...) -> None: ...

class ReadLogRecord(_message.Message):
    __slots__ = ("record", "next_page")
    RECORD_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    record: _log_pb2.LogRecord
    next_page: _paging_pb2.NextPage
    def __init__(self, record: _Optional[_Union[_log_pb2.LogRecord, _Mapping]] = ..., next_page: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ...) -> None: ...
