from google.protobuf import wrappers_pb2 as _wrappers_pb2
from doublecloud.v1 import operation_pb2 as _operation_pb2
from doublecloud.visualization.v1 import workbook_pb2 as _workbook_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetWorkbookRequest(_message.Message):
    __slots__ = ("workbook_id",)
    WORKBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    workbook_id: str
    def __init__(self, workbook_id: _Optional[str] = ...) -> None: ...

class GetWorkbookResponse(_message.Message):
    __slots__ = ("workbook", "id", "title", "project_id")
    WORKBOOK_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    workbook: _workbook_pb2.Workbook
    id: str
    title: str
    project_id: str
    def __init__(self, workbook: _Optional[_Union[_workbook_pb2.Workbook, _Mapping]] = ..., id: _Optional[str] = ..., title: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class CreateWorkbookRequest(_message.Message):
    __slots__ = ("project_id", "workbook_title")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    WORKBOOK_TITLE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    workbook_title: str
    def __init__(self, project_id: _Optional[str] = ..., workbook_title: _Optional[str] = ...) -> None: ...

class UpdateWorkbookRequest(_message.Message):
    __slots__ = ("workbook_id", "workbook", "force_rewrite")
    WORKBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    WORKBOOK_FIELD_NUMBER: _ClassVar[int]
    FORCE_REWRITE_FIELD_NUMBER: _ClassVar[int]
    workbook_id: str
    workbook: _workbook_pb2.Workbook
    force_rewrite: _wrappers_pb2.BoolValue
    def __init__(self, workbook_id: _Optional[str] = ..., workbook: _Optional[_Union[_workbook_pb2.Workbook, _Mapping]] = ..., force_rewrite: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class DeleteWorkbookRequest(_message.Message):
    __slots__ = ("workbook_id",)
    WORKBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    workbook_id: str
    def __init__(self, workbook_id: _Optional[str] = ...) -> None: ...

class GetWorkbookConnectionRequest(_message.Message):
    __slots__ = ("workbook_id", "connection_name")
    WORKBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    workbook_id: str
    connection_name: str
    def __init__(self, workbook_id: _Optional[str] = ..., connection_name: _Optional[str] = ...) -> None: ...

class GetWorkbookConnectionResponse(_message.Message):
    __slots__ = ("connection",)
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    connection: _workbook_pb2.Connection
    def __init__(self, connection: _Optional[_Union[_workbook_pb2.Connection, _Mapping]] = ...) -> None: ...

class CreateWorkbookConnectionRequest(_message.Message):
    __slots__ = ("workbook_id", "connection_name", "connection", "secret")
    WORKBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    workbook_id: str
    connection_name: str
    connection: _workbook_pb2.Connection
    secret: _workbook_pb2.Secret
    def __init__(self, workbook_id: _Optional[str] = ..., connection_name: _Optional[str] = ..., connection: _Optional[_Union[_workbook_pb2.Connection, _Mapping]] = ..., secret: _Optional[_Union[_workbook_pb2.Secret, _Mapping]] = ...) -> None: ...

class UpdateWorkbookConnectionRequest(_message.Message):
    __slots__ = ("workbook_id", "connection_name", "connection", "secret")
    WORKBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    workbook_id: str
    connection_name: str
    connection: _workbook_pb2.Connection
    secret: _workbook_pb2.Secret
    def __init__(self, workbook_id: _Optional[str] = ..., connection_name: _Optional[str] = ..., connection: _Optional[_Union[_workbook_pb2.Connection, _Mapping]] = ..., secret: _Optional[_Union[_workbook_pb2.Secret, _Mapping]] = ...) -> None: ...

class DeleteWorkbookConnectionRequest(_message.Message):
    __slots__ = ("workbook_id", "connection_name")
    WORKBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    workbook_id: str
    connection_name: str
    def __init__(self, workbook_id: _Optional[str] = ..., connection_name: _Optional[str] = ...) -> None: ...

class AdviseDatasetFieldsRequest(_message.Message):
    __slots__ = ("workbook_id", "connection_name", "partial_dataset")
    WORKBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_DATASET_FIELD_NUMBER: _ClassVar[int]
    workbook_id: str
    connection_name: str
    partial_dataset: _workbook_pb2.Dataset
    def __init__(self, workbook_id: _Optional[str] = ..., connection_name: _Optional[str] = ..., partial_dataset: _Optional[_Union[_workbook_pb2.Dataset, _Mapping]] = ...) -> None: ...

class AdviseDatasetFieldsResponse(_message.Message):
    __slots__ = ("dataset",)
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: _workbook_pb2.Dataset
    def __init__(self, dataset: _Optional[_Union[_workbook_pb2.Dataset, _Mapping]] = ...) -> None: ...

class ListWorkbooksRequest(_message.Message):
    __slots__ = ("project_id",)
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class ListWorkbooksResponse(_message.Message):
    __slots__ = ("workbooks",)
    WORKBOOKS_FIELD_NUMBER: _ClassVar[int]
    workbooks: _containers.RepeatedCompositeFieldContainer[_workbook_pb2.WorkbooksIndexItem]
    def __init__(self, workbooks: _Optional[_Iterable[_Union[_workbook_pb2.WorkbooksIndexItem, _Mapping]]] = ...) -> None: ...

class ErrorDetailsRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ErrorDetailsResponse(_message.Message):
    __slots__ = ("id", "format", "details")
    ID_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    id: str
    format: str
    details: str
    def __init__(self, id: _Optional[str] = ..., format: _Optional[str] = ..., details: _Optional[str] = ...) -> None: ...
