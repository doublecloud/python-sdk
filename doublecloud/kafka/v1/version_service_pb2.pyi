from doublecloud.v1 import paging_pb2 as _paging_pb2
from doublecloud.kafka.v1 import version_pb2 as _version_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListVersionsRequest(_message.Message):
    __slots__ = ("paging",)
    PAGING_FIELD_NUMBER: _ClassVar[int]
    paging: _paging_pb2.Paging
    def __init__(self, paging: _Optional[_Union[_paging_pb2.Paging, _Mapping]] = ...) -> None: ...

class ListVersionsResponse(_message.Message):
    __slots__ = ("versions", "next_page")
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    versions: _containers.RepeatedCompositeFieldContainer[_version_pb2.Version]
    next_page: _paging_pb2.NextPage
    def __init__(self, versions: _Optional[_Iterable[_Union[_version_pb2.Version, _Mapping]]] = ..., next_page: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ...) -> None: ...
