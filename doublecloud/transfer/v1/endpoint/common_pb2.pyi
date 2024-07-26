from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectTransferStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OBJECT_TRANSFER_STAGE_UNSPECIFIED: _ClassVar[ObjectTransferStage]
    BEFORE_DATA: _ClassVar[ObjectTransferStage]
    AFTER_DATA: _ClassVar[ObjectTransferStage]
    NEVER: _ClassVar[ObjectTransferStage]

class CleanupPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLEANUP_POLICY_UNSPECIFIED: _ClassVar[CleanupPolicy]
    DISABLED: _ClassVar[CleanupPolicy]
    DROP: _ClassVar[CleanupPolicy]
    TRUNCATE: _ClassVar[CleanupPolicy]

class ColumnType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLUMN_TYPE_UNSPECIFIED: _ClassVar[ColumnType]
    INT32: _ClassVar[ColumnType]
    INT16: _ClassVar[ColumnType]
    INT8: _ClassVar[ColumnType]
    UINT64: _ClassVar[ColumnType]
    UINT32: _ClassVar[ColumnType]
    UINT16: _ClassVar[ColumnType]
    UINT8: _ClassVar[ColumnType]
    DOUBLE: _ClassVar[ColumnType]
    BOOLEAN: _ClassVar[ColumnType]
    STRING: _ClassVar[ColumnType]
    UTF8: _ClassVar[ColumnType]
    ANY: _ClassVar[ColumnType]
    DATETIME: _ClassVar[ColumnType]
    INT64: _ClassVar[ColumnType]
OBJECT_TRANSFER_STAGE_UNSPECIFIED: ObjectTransferStage
BEFORE_DATA: ObjectTransferStage
AFTER_DATA: ObjectTransferStage
NEVER: ObjectTransferStage
CLEANUP_POLICY_UNSPECIFIED: CleanupPolicy
DISABLED: CleanupPolicy
DROP: CleanupPolicy
TRUNCATE: CleanupPolicy
COLUMN_TYPE_UNSPECIFIED: ColumnType
INT32: ColumnType
INT16: ColumnType
INT8: ColumnType
UINT64: ColumnType
UINT32: ColumnType
UINT16: ColumnType
UINT8: ColumnType
DOUBLE: ColumnType
BOOLEAN: ColumnType
STRING: ColumnType
UTF8: ColumnType
ANY: ColumnType
DATETIME: ColumnType
INT64: ColumnType

class AltName(_message.Message):
    __slots__ = ("from_name", "to_name")
    FROM_NAME_FIELD_NUMBER: _ClassVar[int]
    TO_NAME_FIELD_NUMBER: _ClassVar[int]
    from_name: str
    to_name: str
    def __init__(self, from_name: _Optional[str] = ..., to_name: _Optional[str] = ...) -> None: ...

class Secret(_message.Message):
    __slots__ = ("raw",)
    RAW_FIELD_NUMBER: _ClassVar[int]
    raw: str
    def __init__(self, raw: _Optional[str] = ...) -> None: ...

class ColSchema(_message.Message):
    __slots__ = ("name", "type", "key", "required", "path")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: ColumnType
    key: bool
    required: bool
    path: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[ColumnType, str]] = ..., key: bool = ..., required: bool = ..., path: _Optional[str] = ...) -> None: ...

class TLSMode(_message.Message):
    __slots__ = ("disabled", "enabled")
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    disabled: _empty_pb2.Empty
    enabled: TLSConfig
    def __init__(self, disabled: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., enabled: _Optional[_Union[TLSConfig, _Mapping]] = ...) -> None: ...

class TLSConfig(_message.Message):
    __slots__ = ("ca_certificate",)
    CA_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    ca_certificate: str
    def __init__(self, ca_certificate: _Optional[str] = ...) -> None: ...

class ColumnValue(_message.Message):
    __slots__ = ("string_value",)
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    def __init__(self, string_value: _Optional[str] = ...) -> None: ...

class HeaderValue(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class DataTransformationOptions(_message.Message):
    __slots__ = ("cloud_function", "number_of_retries", "buffer_size", "buffer_flush_interval", "invocation_timeout", "cloud_function_url", "headers")
    CLOUD_FUNCTION_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_RETRIES_FIELD_NUMBER: _ClassVar[int]
    BUFFER_SIZE_FIELD_NUMBER: _ClassVar[int]
    BUFFER_FLUSH_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_FUNCTION_URL_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    cloud_function: str
    number_of_retries: int
    buffer_size: str
    buffer_flush_interval: str
    invocation_timeout: str
    cloud_function_url: str
    headers: _containers.RepeatedCompositeFieldContainer[HeaderValue]
    def __init__(self, cloud_function: _Optional[str] = ..., number_of_retries: _Optional[int] = ..., buffer_size: _Optional[str] = ..., buffer_flush_interval: _Optional[str] = ..., invocation_timeout: _Optional[str] = ..., cloud_function_url: _Optional[str] = ..., headers: _Optional[_Iterable[_Union[HeaderValue, _Mapping]]] = ...) -> None: ...

class FieldList(_message.Message):
    __slots__ = ("fields",)
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[ColSchema]
    def __init__(self, fields: _Optional[_Iterable[_Union[ColSchema, _Mapping]]] = ...) -> None: ...

class DataSchema(_message.Message):
    __slots__ = ("json_fields", "fields")
    JSON_FIELDS_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    json_fields: str
    fields: FieldList
    def __init__(self, json_fields: _Optional[str] = ..., fields: _Optional[_Union[FieldList, _Mapping]] = ...) -> None: ...

class NoAuth(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
