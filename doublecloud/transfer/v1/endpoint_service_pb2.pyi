from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from doublecloud.transfer.v1 import endpoint_pb2 as _endpoint_pb2
from doublecloud.v1 import operation_pb2 as _operation_pb2
from doublecloud.v1 import paging_pb2 as _paging_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetEndpointRequest(_message.Message):
    __slots__ = ("endpoint_id",)
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    endpoint_id: str
    def __init__(self, endpoint_id: _Optional[str] = ...) -> None: ...

class ListEndpointsRequest(_message.Message):
    __slots__ = ("project_id", "page")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    page: _paging_pb2.Paging
    def __init__(self, project_id: _Optional[str] = ..., page: _Optional[_Union[_paging_pb2.Paging, _Mapping]] = ...) -> None: ...

class ListEndpointsResponse(_message.Message):
    __slots__ = ("endpoints", "next_page")
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    endpoints: _containers.RepeatedCompositeFieldContainer[_endpoint_pb2.Endpoint]
    next_page: _paging_pb2.NextPage
    def __init__(self, endpoints: _Optional[_Iterable[_Union[_endpoint_pb2.Endpoint, _Mapping]]] = ..., next_page: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ...) -> None: ...

class CreateEndpointRequest(_message.Message):
    __slots__ = ("project_id", "name", "description", "labels", "settings")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    name: str
    description: str
    labels: _containers.ScalarMap[str, str]
    settings: _endpoint_pb2.EndpointSettings
    def __init__(self, project_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., settings: _Optional[_Union[_endpoint_pb2.EndpointSettings, _Mapping]] = ...) -> None: ...

class UpdateEndpointRequest(_message.Message):
    __slots__ = ("endpoint_id", "name", "description", "labels", "settings")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    endpoint_id: str
    name: str
    description: str
    labels: _containers.ScalarMap[str, str]
    settings: _endpoint_pb2.EndpointSettings
    def __init__(self, endpoint_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., settings: _Optional[_Union[_endpoint_pb2.EndpointSettings, _Mapping]] = ...) -> None: ...

class DeleteEndpointRequest(_message.Message):
    __slots__ = ("endpoint_id",)
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    endpoint_id: str
    def __init__(self, endpoint_id: _Optional[str] = ...) -> None: ...
