from doublecloud.transfer.v1.endpoint import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProtoMessagePackageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PROTO_MESSAGE_PACKAGE_TYPE_UNSPECIFIED: _ClassVar[ProtoMessagePackageType]
    PROTOSEQ: _ClassVar[ProtoMessagePackageType]
    REPEATED: _ClassVar[ProtoMessagePackageType]
    SINGLE_MESSAGE: _ClassVar[ProtoMessagePackageType]
PROTO_MESSAGE_PACKAGE_TYPE_UNSPECIFIED: ProtoMessagePackageType
PROTOSEQ: ProtoMessagePackageType
REPEATED: ProtoMessagePackageType
SINGLE_MESSAGE: ProtoMessagePackageType

class Parser(_message.Message):
    __slots__ = ("json_parser", "debezium_cdc_parser", "tskv_parser", "confluent_schema_registry_parser", "blank_parser", "raw_table")
    JSON_PARSER_FIELD_NUMBER: _ClassVar[int]
    DEBEZIUM_CDC_PARSER_FIELD_NUMBER: _ClassVar[int]
    TSKV_PARSER_FIELD_NUMBER: _ClassVar[int]
    CONFLUENT_SCHEMA_REGISTRY_PARSER_FIELD_NUMBER: _ClassVar[int]
    BLANK_PARSER_FIELD_NUMBER: _ClassVar[int]
    RAW_TABLE_FIELD_NUMBER: _ClassVar[int]
    json_parser: GenericParserCommon
    debezium_cdc_parser: DebeziumCDCParser
    tskv_parser: GenericParserCommon
    confluent_schema_registry_parser: ConfluentSchemaRegistryParser
    blank_parser: BlankParser
    raw_table: RawTable
    def __init__(self, json_parser: _Optional[_Union[GenericParserCommon, _Mapping]] = ..., debezium_cdc_parser: _Optional[_Union[DebeziumCDCParser, _Mapping]] = ..., tskv_parser: _Optional[_Union[GenericParserCommon, _Mapping]] = ..., confluent_schema_registry_parser: _Optional[_Union[ConfluentSchemaRegistryParser, _Mapping]] = ..., blank_parser: _Optional[_Union[BlankParser, _Mapping]] = ..., raw_table: _Optional[_Union[RawTable, _Mapping]] = ...) -> None: ...

class GenericParserCommon(_message.Message):
    __slots__ = ("data_schema", "null_keys_allowed", "add_rest_column")
    DATA_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    NULL_KEYS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    ADD_REST_COLUMN_FIELD_NUMBER: _ClassVar[int]
    data_schema: _common_pb2.DataSchema
    null_keys_allowed: bool
    add_rest_column: bool
    def __init__(self, data_schema: _Optional[_Union[_common_pb2.DataSchema, _Mapping]] = ..., null_keys_allowed: bool = ..., add_rest_column: bool = ...) -> None: ...

class DebeziumCDCParser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfluentSchemaRegistryConnection(_message.Message):
    __slots__ = ("schema_registry_url", "tls_mode", "auth")
    SCHEMA_REGISTRY_URL_FIELD_NUMBER: _ClassVar[int]
    TLS_MODE_FIELD_NUMBER: _ClassVar[int]
    AUTH_FIELD_NUMBER: _ClassVar[int]
    schema_registry_url: str
    tls_mode: _common_pb2.TLSMode
    auth: ConfluentSchemaRegistryAuth
    def __init__(self, schema_registry_url: _Optional[str] = ..., tls_mode: _Optional[_Union[_common_pb2.TLSMode, _Mapping]] = ..., auth: _Optional[_Union[ConfluentSchemaRegistryAuth, _Mapping]] = ...) -> None: ...

class ConfluentSchemaRegistryParser(_message.Message):
    __slots__ = ("connection",)
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    connection: ConfluentSchemaRegistryConnection
    def __init__(self, connection: _Optional[_Union[ConfluentSchemaRegistryConnection, _Mapping]] = ...) -> None: ...

class ConfluentSchemaRegistryAuth(_message.Message):
    __slots__ = ("no_auth", "basic")
    NO_AUTH_FIELD_NUMBER: _ClassVar[int]
    BASIC_FIELD_NUMBER: _ClassVar[int]
    no_auth: _common_pb2.NoAuth
    basic: BasicAuthSR
    def __init__(self, no_auth: _Optional[_Union[_common_pb2.NoAuth, _Mapping]] = ..., basic: _Optional[_Union[BasicAuthSR, _Mapping]] = ...) -> None: ...

class BasicAuthSR(_message.Message):
    __slots__ = ("user", "password")
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    password: _common_pb2.Secret
    def __init__(self, user: _Optional[str] = ..., password: _Optional[_Union[_common_pb2.Secret, _Mapping]] = ...) -> None: ...

class ProtoParser(_message.Message):
    __slots__ = ("proto_desc", "msg_package_type", "msg_name", "primary_keys", "included_fields", "null_keys_allowed")
    PROTO_DESC_FIELD_NUMBER: _ClassVar[int]
    MSG_PACKAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MSG_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEYS_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    NULL_KEYS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    proto_desc: ProtoDesc
    msg_package_type: ProtoMessagePackageType
    msg_name: str
    primary_keys: _containers.RepeatedScalarFieldContainer[str]
    included_fields: ProtoDataSchema
    null_keys_allowed: bool
    def __init__(self, proto_desc: _Optional[_Union[ProtoDesc, _Mapping]] = ..., msg_package_type: _Optional[_Union[ProtoMessagePackageType, str]] = ..., msg_name: _Optional[str] = ..., primary_keys: _Optional[_Iterable[str]] = ..., included_fields: _Optional[_Union[ProtoDataSchema, _Mapping]] = ..., null_keys_allowed: bool = ...) -> None: ...

class ProtoDesc(_message.Message):
    __slots__ = ("desc_file",)
    DESC_FILE_FIELD_NUMBER: _ClassVar[int]
    desc_file: bytes
    def __init__(self, desc_file: _Optional[bytes] = ...) -> None: ...

class ProtoDataSchema(_message.Message):
    __slots__ = ("col_params_list",)
    COL_PARAMS_LIST_FIELD_NUMBER: _ClassVar[int]
    col_params_list: ColumnParamsList
    def __init__(self, col_params_list: _Optional[_Union[ColumnParamsList, _Mapping]] = ...) -> None: ...

class ColumnParamsList(_message.Message):
    __slots__ = ("col_params",)
    COL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    col_params: _containers.RepeatedCompositeFieldContainer[ColumnParams]
    def __init__(self, col_params: _Optional[_Iterable[_Union[ColumnParams, _Mapping]]] = ...) -> None: ...

class ColumnParams(_message.Message):
    __slots__ = ("name", "required")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    name: str
    required: bool
    def __init__(self, name: _Optional[str] = ..., required: bool = ...) -> None: ...

class BlankParser(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RawTable(_message.Message):
    __slots__ = ("value_as_bytes", "keys_as_bytes", "add_timestamp", "add_headers", "add_key")
    VALUE_AS_BYTES_FIELD_NUMBER: _ClassVar[int]
    KEYS_AS_BYTES_FIELD_NUMBER: _ClassVar[int]
    ADD_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ADD_HEADERS_FIELD_NUMBER: _ClassVar[int]
    ADD_KEY_FIELD_NUMBER: _ClassVar[int]
    value_as_bytes: bool
    keys_as_bytes: bool
    add_timestamp: bool
    add_headers: bool
    add_key: bool
    def __init__(self, value_as_bytes: bool = ..., keys_as_bytes: bool = ..., add_timestamp: bool = ..., add_headers: bool = ..., add_key: bool = ...) -> None: ...
