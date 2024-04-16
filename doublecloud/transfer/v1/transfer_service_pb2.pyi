from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from doublecloud.transfer.v1 import transfer_pb2 as _transfer_pb2
from doublecloud.v1 import operation_pb2 as _operation_pb2
from doublecloud.v1 import paging_pb2 as _paging_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTransferRequest(_message.Message):
    __slots__ = ("source_id", "target_id", "description", "project_id", "runtime", "type", "name", "labels", "regular_snapshot", "transformation", "data_objects")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    REGULAR_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATION_FIELD_NUMBER: _ClassVar[int]
    DATA_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    source_id: str
    target_id: str
    description: str
    project_id: str
    runtime: _transfer_pb2.Runtime
    type: _transfer_pb2.TransferType
    name: str
    labels: _containers.ScalarMap[str, str]
    regular_snapshot: _transfer_pb2.RegularSnapshot
    transformation: _transfer_pb2.Transformation
    data_objects: _transfer_pb2.DataObjects
    def __init__(self, source_id: _Optional[str] = ..., target_id: _Optional[str] = ..., description: _Optional[str] = ..., project_id: _Optional[str] = ..., runtime: _Optional[_Union[_transfer_pb2.Runtime, _Mapping]] = ..., type: _Optional[_Union[_transfer_pb2.TransferType, str]] = ..., name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., regular_snapshot: _Optional[_Union[_transfer_pb2.RegularSnapshot, _Mapping]] = ..., transformation: _Optional[_Union[_transfer_pb2.Transformation, _Mapping]] = ..., data_objects: _Optional[_Union[_transfer_pb2.DataObjects, _Mapping]] = ...) -> None: ...

class UpdateTransferRequest(_message.Message):
    __slots__ = ("transfer_id", "description", "runtime", "name", "labels", "regular_snapshot", "transformation", "data_objects")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    REGULAR_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATION_FIELD_NUMBER: _ClassVar[int]
    DATA_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    transfer_id: str
    description: str
    runtime: _transfer_pb2.Runtime
    name: str
    labels: _containers.ScalarMap[str, str]
    regular_snapshot: _transfer_pb2.RegularSnapshot
    transformation: _transfer_pb2.Transformation
    data_objects: _transfer_pb2.DataObjects
    def __init__(self, transfer_id: _Optional[str] = ..., description: _Optional[str] = ..., runtime: _Optional[_Union[_transfer_pb2.Runtime, _Mapping]] = ..., name: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., regular_snapshot: _Optional[_Union[_transfer_pb2.RegularSnapshot, _Mapping]] = ..., transformation: _Optional[_Union[_transfer_pb2.Transformation, _Mapping]] = ..., data_objects: _Optional[_Union[_transfer_pb2.DataObjects, _Mapping]] = ...) -> None: ...

class DeleteTransferRequest(_message.Message):
    __slots__ = ("transfer_id",)
    TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
    transfer_id: str
    def __init__(self, transfer_id: _Optional[str] = ...) -> None: ...

class ListTransfersRequest(_message.Message):
    __slots__ = ("project_id", "page")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    page: _paging_pb2.Paging
    def __init__(self, project_id: _Optional[str] = ..., page: _Optional[_Union[_paging_pb2.Paging, _Mapping]] = ...) -> None: ...

class ListTransfersResponse(_message.Message):
    __slots__ = ("transfers", "next_page_token")
    TRANSFERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    transfers: _containers.RepeatedCompositeFieldContainer[_transfer_pb2.Transfer]
    next_page_token: str
    def __init__(self, transfers: _Optional[_Iterable[_Union[_transfer_pb2.Transfer, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetTransferRequest(_message.Message):
    __slots__ = ("transfer_id",)
    TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
    transfer_id: str
    def __init__(self, transfer_id: _Optional[str] = ...) -> None: ...

class DeactivateTransferRequest(_message.Message):
    __slots__ = ("transfer_id",)
    TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
    transfer_id: str
    def __init__(self, transfer_id: _Optional[str] = ...) -> None: ...

class ActivateTransferRequest(_message.Message):
    __slots__ = ("transfer_id",)
    TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
    transfer_id: str
    def __init__(self, transfer_id: _Optional[str] = ...) -> None: ...

class GetMetricsRequest(_message.Message):
    __slots__ = ("transfer_id",)
    TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
    transfer_id: str
    def __init__(self, transfer_id: _Optional[str] = ...) -> None: ...

class TransferMetrics(_message.Message):
    __slots__ = ("metrics",)
    class Metric(_message.Message):
        __slots__ = ("help", "type", "value")
        HELP_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        help: str
        type: str
        value: str
        def __init__(self, help: _Optional[str] = ..., type: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    METRICS_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.RepeatedCompositeFieldContainer[TransferMetrics.Metric]
    def __init__(self, metrics: _Optional[_Iterable[_Union[TransferMetrics.Metric, _Mapping]]] = ...) -> None: ...

class MetricExporterConnectionInfoRequest(_message.Message):
    __slots__ = ("transfer_id",)
    TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
    transfer_id: str
    def __init__(self, transfer_id: _Optional[str] = ...) -> None: ...

class MetricExporterConnectionInfoMetadata(_message.Message):
    __slots__ = ("connection_string", "user", "password")
    CONNECTION_STRING_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    connection_string: str
    user: str
    password: str
    def __init__(self, connection_string: _Optional[str] = ..., user: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class DeleteExporterConnectionInfoRequest(_message.Message):
    __slots__ = ("transfer_id",)
    TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
    transfer_id: str
    def __init__(self, transfer_id: _Optional[str] = ...) -> None: ...

class DeleteExporterConnectionInfoMetadata(_message.Message):
    __slots__ = ("transfer_id",)
    TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
    transfer_id: str
    def __init__(self, transfer_id: _Optional[str] = ...) -> None: ...
