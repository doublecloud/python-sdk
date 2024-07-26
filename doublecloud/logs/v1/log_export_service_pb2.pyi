from doublecloud.v1 import operation_pb2 as _operation_pb2
from doublecloud.v1 import paging_pb2 as _paging_pb2
from doublecloud.logs.v1 import log_export_pb2 as _log_export_pb2
from doublecloud.logs.v1 import log_source_pb2 as _log_source_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListExportRequest(_message.Message):
    __slots__ = ("project_id", "paging")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    paging: _paging_pb2.Paging
    def __init__(self, project_id: _Optional[str] = ..., paging: _Optional[_Union[_paging_pb2.Paging, _Mapping]] = ...) -> None: ...

class ListExportResponse(_message.Message):
    __slots__ = ("exports", "next_page")
    EXPORTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    exports: _containers.RepeatedCompositeFieldContainer[_log_export_pb2.LogsExport]
    next_page: _paging_pb2.NextPage
    def __init__(self, exports: _Optional[_Iterable[_Union[_log_export_pb2.LogsExport, _Mapping]]] = ..., next_page: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ...) -> None: ...

class GetExportRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CreateExportRequest(_message.Message):
    __slots__ = ("project_id", "name", "description", "sources", "target")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    name: str
    description: str
    sources: _containers.RepeatedCompositeFieldContainer[_log_source_pb2.LogSource]
    target: _log_export_pb2.LogsTarget
    def __init__(self, project_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., sources: _Optional[_Iterable[_Union[_log_source_pb2.LogSource, _Mapping]]] = ..., target: _Optional[_Union[_log_export_pb2.LogsTarget, _Mapping]] = ...) -> None: ...

class UpdateExportRequest(_message.Message):
    __slots__ = ("id", "name", "description", "sources", "target")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    sources: _containers.RepeatedCompositeFieldContainer[_log_source_pb2.LogSource]
    target: _log_export_pb2.LogsTarget
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., sources: _Optional[_Iterable[_Union[_log_source_pb2.LogSource, _Mapping]]] = ..., target: _Optional[_Union[_log_export_pb2.LogsTarget, _Mapping]] = ...) -> None: ...

class DeleteExportRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...
