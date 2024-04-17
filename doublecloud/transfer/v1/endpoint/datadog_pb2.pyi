from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DatadogTarget(_message.Message):
    __slots__ = ("client_api_key", "host", "column_mapping")
    class ColumnMapping(_message.Message):
        __slots__ = ("source", "tags", "host", "message_template", "service")
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        HOST_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        source: str
        tags: _containers.RepeatedScalarFieldContainer[str]
        host: str
        message_template: str
        service: str
        def __init__(self, source: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., host: _Optional[str] = ..., message_template: _Optional[str] = ..., service: _Optional[str] = ...) -> None: ...
    CLIENT_API_KEY_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    COLUMN_MAPPING_FIELD_NUMBER: _ClassVar[int]
    client_api_key: str
    host: str
    column_mapping: DatadogTarget.ColumnMapping
    def __init__(self, client_api_key: _Optional[str] = ..., host: _Optional[str] = ..., column_mapping: _Optional[_Union[DatadogTarget.ColumnMapping, _Mapping]] = ...) -> None: ...
