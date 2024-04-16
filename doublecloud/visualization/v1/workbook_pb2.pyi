from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlainSecret(_message.Message):
    __slots__ = ("secret",)
    SECRET_FIELD_NUMBER: _ClassVar[int]
    secret: str
    def __init__(self, secret: _Optional[str] = ...) -> None: ...

class Secret(_message.Message):
    __slots__ = ("plain_secret",)
    PLAIN_SECRET_FIELD_NUMBER: _ClassVar[int]
    plain_secret: PlainSecret
    def __init__(self, plain_secret: _Optional[_Union[PlainSecret, _Mapping]] = ...) -> None: ...

class Workbook(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _struct_pb2.Value
    def __init__(self, config: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class Dataset(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _struct_pb2.Value
    def __init__(self, config: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class Connection(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _struct_pb2.Value
    def __init__(self, config: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...

class WorkbooksIndexItem(_message.Message):
    __slots__ = ("id", "title")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...
