from doublecloud.v1 import operation_pb2 as _operation_pb2
from doublecloud.v1 import paging_pb2 as _paging_pb2
from doublecloud.kafka.v1 import connector_pb2 as _connector_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetConnectorRequest(_message.Message):
    __slots__ = ("cluster_id", "connector_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    connector_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., connector_name: _Optional[str] = ...) -> None: ...

class ListConnectorsRequest(_message.Message):
    __slots__ = ("cluster_id", "paging")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    paging: _paging_pb2.Paging
    def __init__(self, cluster_id: _Optional[str] = ..., paging: _Optional[_Union[_paging_pb2.Paging, _Mapping]] = ...) -> None: ...

class ListConnectorsResponse(_message.Message):
    __slots__ = ("connectors", "next_page")
    CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    connectors: _containers.RepeatedCompositeFieldContainer[_connector_pb2.Connector]
    next_page: _paging_pb2.NextPage
    def __init__(self, connectors: _Optional[_Iterable[_Union[_connector_pb2.Connector, _Mapping]]] = ..., next_page: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ...) -> None: ...

class CreateConnectorRequest(_message.Message):
    __slots__ = ("cluster_id", "connector_spec")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_SPEC_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    connector_spec: _connector_pb2.ConnectorSpec
    def __init__(self, cluster_id: _Optional[str] = ..., connector_spec: _Optional[_Union[_connector_pb2.ConnectorSpec, _Mapping]] = ...) -> None: ...

class CreateConnectorMetadata(_message.Message):
    __slots__ = ("cluster_id", "connector_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    connector_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., connector_name: _Optional[str] = ...) -> None: ...

class UpdateConnectorRequest(_message.Message):
    __slots__ = ("cluster_id", "connector_name", "connector_spec")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_SPEC_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    connector_name: str
    connector_spec: _connector_pb2.UpdateConnectorSpec
    def __init__(self, cluster_id: _Optional[str] = ..., connector_name: _Optional[str] = ..., connector_spec: _Optional[_Union[_connector_pb2.UpdateConnectorSpec, _Mapping]] = ...) -> None: ...

class UpdateConnectorMetadata(_message.Message):
    __slots__ = ("cluster_id", "connector_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    connector_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., connector_name: _Optional[str] = ...) -> None: ...

class DeleteConnectorRequest(_message.Message):
    __slots__ = ("cluster_id", "connector_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    connector_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., connector_name: _Optional[str] = ...) -> None: ...

class DeleteConnectorMetadata(_message.Message):
    __slots__ = ("cluster_id", "connector_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    connector_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., connector_name: _Optional[str] = ...) -> None: ...

class ResumeConnectorRequest(_message.Message):
    __slots__ = ("cluster_id", "connector_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    connector_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., connector_name: _Optional[str] = ...) -> None: ...

class ResumeConnectorMetadata(_message.Message):
    __slots__ = ("cluster_id", "connector_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    connector_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., connector_name: _Optional[str] = ...) -> None: ...

class PauseConnectorRequest(_message.Message):
    __slots__ = ("cluster_id", "connector_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    connector_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., connector_name: _Optional[str] = ...) -> None: ...

class PauseConnectorMetadata(_message.Message):
    __slots__ = ("cluster_id", "connector_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    connector_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., connector_name: _Optional[str] = ...) -> None: ...
