from doublecloud.transfer.v1.endpoint import common_pb2 as _common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Parser(_message.Message):
    __slots__ = ["json_parser", "tskv_parser"]
    JSON_PARSER_FIELD_NUMBER: _ClassVar[int]
    TSKV_PARSER_FIELD_NUMBER: _ClassVar[int]
    json_parser: GenericParserCommon
    tskv_parser: GenericParserCommon
    def __init__(self, json_parser: _Optional[_Union[GenericParserCommon, _Mapping]] = ..., tskv_parser: _Optional[_Union[GenericParserCommon, _Mapping]] = ...) -> None: ...

class GenericParserCommon(_message.Message):
    __slots__ = ["data_schema", "null_keys_allowed", "add_rest_column"]
    DATA_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    NULL_KEYS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    ADD_REST_COLUMN_FIELD_NUMBER: _ClassVar[int]
    data_schema: _common_pb2.DataSchema
    null_keys_allowed: bool
    add_rest_column: bool
    def __init__(self, data_schema: _Optional[_Union[_common_pb2.DataSchema, _Mapping]] = ..., null_keys_allowed: bool = ..., add_rest_column: bool = ...) -> None: ...
