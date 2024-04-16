from google.protobuf import empty_pb2 as _empty_pb2
from doublecloud.transfer.v1.endpoint import common_pb2 as _common_pb2
from doublecloud.transfer.v1.endpoint import parsers_pb2 as _parsers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectStorageCodec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OBJECT_STORAGE_CODEC_UNSPECIFIED: _ClassVar[ObjectStorageCodec]
    UNCOMPRESSED: _ClassVar[ObjectStorageCodec]
    GZIP: _ClassVar[ObjectStorageCodec]

class ObjectStorageSerializationFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OBJECT_STORAGE_SERIALIZATION_FORMAT_UNSPECIFIED: _ClassVar[ObjectStorageSerializationFormat]
    OBJECT_STORAGE_SERIALIZATION_FORMAT_JSON: _ClassVar[ObjectStorageSerializationFormat]
    OBJECT_STORAGE_SERIALIZATION_FORMAT_CSV: _ClassVar[ObjectStorageSerializationFormat]
    OBJECT_STORAGE_SERIALIZATION_FORMAT_RAW: _ClassVar[ObjectStorageSerializationFormat]
    OBJECT_STORAGE_SERIALIZATION_FORMAT_PARQUET: _ClassVar[ObjectStorageSerializationFormat]

class ObjectStorageUnparsed(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OBJECT_STORAGE_UNPARSED_UNSPECIFIED: _ClassVar[ObjectStorageUnparsed]
    OBJECT_STORAGE_UNPARSED_RETRY: _ClassVar[ObjectStorageUnparsed]
    OBJECT_STORAGE_UNPARSED_FAIL: _ClassVar[ObjectStorageUnparsed]
    OBJECT_STORAGE_UNPARSED_CONTINUE: _ClassVar[ObjectStorageUnparsed]
OBJECT_STORAGE_CODEC_UNSPECIFIED: ObjectStorageCodec
UNCOMPRESSED: ObjectStorageCodec
GZIP: ObjectStorageCodec
OBJECT_STORAGE_SERIALIZATION_FORMAT_UNSPECIFIED: ObjectStorageSerializationFormat
OBJECT_STORAGE_SERIALIZATION_FORMAT_JSON: ObjectStorageSerializationFormat
OBJECT_STORAGE_SERIALIZATION_FORMAT_CSV: ObjectStorageSerializationFormat
OBJECT_STORAGE_SERIALIZATION_FORMAT_RAW: ObjectStorageSerializationFormat
OBJECT_STORAGE_SERIALIZATION_FORMAT_PARQUET: ObjectStorageSerializationFormat
OBJECT_STORAGE_UNPARSED_UNSPECIFIED: ObjectStorageUnparsed
OBJECT_STORAGE_UNPARSED_RETRY: ObjectStorageUnparsed
OBJECT_STORAGE_UNPARSED_FAIL: ObjectStorageUnparsed
OBJECT_STORAGE_UNPARSED_CONTINUE: ObjectStorageUnparsed

class ObjectStorageConnection(_message.Message):
    __slots__ = ("aws_access_key_id", "aws_secret_access_key", "region", "endpoint", "use_ssl", "verify_ssl_cert")
    AWS_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    USE_SSL_FIELD_NUMBER: _ClassVar[int]
    VERIFY_SSL_CERT_FIELD_NUMBER: _ClassVar[int]
    aws_access_key_id: str
    aws_secret_access_key: str
    region: str
    endpoint: str
    use_ssl: bool
    verify_ssl_cert: bool
    def __init__(self, aws_access_key_id: _Optional[str] = ..., aws_secret_access_key: _Optional[str] = ..., region: _Optional[str] = ..., endpoint: _Optional[str] = ..., use_ssl: bool = ..., verify_ssl_cert: bool = ...) -> None: ...

class ObjectStorageSerializerConfig(_message.Message):
    __slots__ = ("any_as_string",)
    ANY_AS_STRING_FIELD_NUMBER: _ClassVar[int]
    any_as_string: bool
    def __init__(self, any_as_string: bool = ...) -> None: ...

class ObjectStorageTarget(_message.Message):
    __slots__ = ("bucket", "output_format", "bucket_layout", "buffer_size", "buffer_interval", "service_account_id", "output_encoding", "connection", "bucket_layout_timezone", "bucket_layout_column", "serializer_config")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    BUCKET_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    BUFFER_SIZE_FIELD_NUMBER: _ClassVar[int]
    BUFFER_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_ENCODING_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    BUCKET_LAYOUT_TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    BUCKET_LAYOUT_COLUMN_FIELD_NUMBER: _ClassVar[int]
    SERIALIZER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    output_format: ObjectStorageSerializationFormat
    bucket_layout: str
    buffer_size: str
    buffer_interval: str
    service_account_id: str
    output_encoding: ObjectStorageCodec
    connection: ObjectStorageConnection
    bucket_layout_timezone: str
    bucket_layout_column: str
    serializer_config: ObjectStorageSerializerConfig
    def __init__(self, bucket: _Optional[str] = ..., output_format: _Optional[_Union[ObjectStorageSerializationFormat, str]] = ..., bucket_layout: _Optional[str] = ..., buffer_size: _Optional[str] = ..., buffer_interval: _Optional[str] = ..., service_account_id: _Optional[str] = ..., output_encoding: _Optional[_Union[ObjectStorageCodec, str]] = ..., connection: _Optional[_Union[ObjectStorageConnection, _Mapping]] = ..., bucket_layout_timezone: _Optional[str] = ..., bucket_layout_column: _Optional[str] = ..., serializer_config: _Optional[_Union[ObjectStorageSerializerConfig, _Mapping]] = ...) -> None: ...

class ObjectStorageProvider(_message.Message):
    __slots__ = ("bucket", "aws_access_key_id", "aws_secret_access_key", "path_prefix", "endpoint", "use_ssl", "verify_ssl_cert", "region")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    AWS_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    USE_SSL_FIELD_NUMBER: _ClassVar[int]
    VERIFY_SSL_CERT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    aws_access_key_id: str
    aws_secret_access_key: str
    path_prefix: str
    endpoint: str
    use_ssl: bool
    verify_ssl_cert: bool
    region: str
    def __init__(self, bucket: _Optional[str] = ..., aws_access_key_id: _Optional[str] = ..., aws_secret_access_key: _Optional[str] = ..., path_prefix: _Optional[str] = ..., endpoint: _Optional[str] = ..., use_ssl: bool = ..., verify_ssl_cert: bool = ..., region: _Optional[str] = ...) -> None: ...

class ObjectStorageReaderFormat(_message.Message):
    __slots__ = ("csv", "parquet", "avro", "jsonl", "proto")
    class Jsonl(_message.Message):
        __slots__ = ("newlines_in_values", "unexpected_field_behavior", "block_size")
        class UnexpectedFieldBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNEXPECTED_FIELD_BEHAVIOR_UNSPECIFIED: _ClassVar[ObjectStorageReaderFormat.Jsonl.UnexpectedFieldBehavior]
            UNEXPECTED_FIELD_BEHAVIOR_IGNORE: _ClassVar[ObjectStorageReaderFormat.Jsonl.UnexpectedFieldBehavior]
            UNEXPECTED_FIELD_BEHAVIOR_INFER: _ClassVar[ObjectStorageReaderFormat.Jsonl.UnexpectedFieldBehavior]
            UNEXPECTED_FIELD_BEHAVIOR_ERROR: _ClassVar[ObjectStorageReaderFormat.Jsonl.UnexpectedFieldBehavior]
        UNEXPECTED_FIELD_BEHAVIOR_UNSPECIFIED: ObjectStorageReaderFormat.Jsonl.UnexpectedFieldBehavior
        UNEXPECTED_FIELD_BEHAVIOR_IGNORE: ObjectStorageReaderFormat.Jsonl.UnexpectedFieldBehavior
        UNEXPECTED_FIELD_BEHAVIOR_INFER: ObjectStorageReaderFormat.Jsonl.UnexpectedFieldBehavior
        UNEXPECTED_FIELD_BEHAVIOR_ERROR: ObjectStorageReaderFormat.Jsonl.UnexpectedFieldBehavior
        NEWLINES_IN_VALUES_FIELD_NUMBER: _ClassVar[int]
        UNEXPECTED_FIELD_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
        newlines_in_values: bool
        unexpected_field_behavior: ObjectStorageReaderFormat.Jsonl.UnexpectedFieldBehavior
        block_size: int
        def __init__(self, newlines_in_values: bool = ..., unexpected_field_behavior: _Optional[_Union[ObjectStorageReaderFormat.Jsonl.UnexpectedFieldBehavior, str]] = ..., block_size: _Optional[int] = ...) -> None: ...
    class Csv(_message.Message):
        __slots__ = ("delimiter", "quote_char", "escape_char", "encoding", "double_quote", "newlines_in_values", "block_size", "advanced_options", "additional_options")
        class AdvancedOptions(_message.Message):
            __slots__ = ("skip_rows", "skip_rows_after_names", "autogenerate_column_names", "column_names")
            SKIP_ROWS_FIELD_NUMBER: _ClassVar[int]
            SKIP_ROWS_AFTER_NAMES_FIELD_NUMBER: _ClassVar[int]
            AUTOGENERATE_COLUMN_NAMES_FIELD_NUMBER: _ClassVar[int]
            COLUMN_NAMES_FIELD_NUMBER: _ClassVar[int]
            skip_rows: int
            skip_rows_after_names: int
            autogenerate_column_names: bool
            column_names: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, skip_rows: _Optional[int] = ..., skip_rows_after_names: _Optional[int] = ..., autogenerate_column_names: bool = ..., column_names: _Optional[_Iterable[str]] = ...) -> None: ...
        class AdditionalReaderOptions(_message.Message):
            __slots__ = ("null_values", "true_values", "false_values", "decimal_point", "strings_can_be_null", "quoted_strings_can_be_null", "include_columns", "include_missing_columns", "timestamp_parsers")
            NULL_VALUES_FIELD_NUMBER: _ClassVar[int]
            TRUE_VALUES_FIELD_NUMBER: _ClassVar[int]
            FALSE_VALUES_FIELD_NUMBER: _ClassVar[int]
            DECIMAL_POINT_FIELD_NUMBER: _ClassVar[int]
            STRINGS_CAN_BE_NULL_FIELD_NUMBER: _ClassVar[int]
            QUOTED_STRINGS_CAN_BE_NULL_FIELD_NUMBER: _ClassVar[int]
            INCLUDE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
            INCLUDE_MISSING_COLUMNS_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_PARSERS_FIELD_NUMBER: _ClassVar[int]
            null_values: _containers.RepeatedScalarFieldContainer[str]
            true_values: _containers.RepeatedScalarFieldContainer[str]
            false_values: _containers.RepeatedScalarFieldContainer[str]
            decimal_point: str
            strings_can_be_null: bool
            quoted_strings_can_be_null: bool
            include_columns: _containers.RepeatedScalarFieldContainer[str]
            include_missing_columns: bool
            timestamp_parsers: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, null_values: _Optional[_Iterable[str]] = ..., true_values: _Optional[_Iterable[str]] = ..., false_values: _Optional[_Iterable[str]] = ..., decimal_point: _Optional[str] = ..., strings_can_be_null: bool = ..., quoted_strings_can_be_null: bool = ..., include_columns: _Optional[_Iterable[str]] = ..., include_missing_columns: bool = ..., timestamp_parsers: _Optional[_Iterable[str]] = ...) -> None: ...
        DELIMITER_FIELD_NUMBER: _ClassVar[int]
        QUOTE_CHAR_FIELD_NUMBER: _ClassVar[int]
        ESCAPE_CHAR_FIELD_NUMBER: _ClassVar[int]
        ENCODING_FIELD_NUMBER: _ClassVar[int]
        DOUBLE_QUOTE_FIELD_NUMBER: _ClassVar[int]
        NEWLINES_IN_VALUES_FIELD_NUMBER: _ClassVar[int]
        BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
        ADVANCED_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        delimiter: str
        quote_char: str
        escape_char: str
        encoding: str
        double_quote: bool
        newlines_in_values: bool
        block_size: int
        advanced_options: ObjectStorageReaderFormat.Csv.AdvancedOptions
        additional_options: ObjectStorageReaderFormat.Csv.AdditionalReaderOptions
        def __init__(self, delimiter: _Optional[str] = ..., quote_char: _Optional[str] = ..., escape_char: _Optional[str] = ..., encoding: _Optional[str] = ..., double_quote: bool = ..., newlines_in_values: bool = ..., block_size: _Optional[int] = ..., advanced_options: _Optional[_Union[ObjectStorageReaderFormat.Csv.AdvancedOptions, _Mapping]] = ..., additional_options: _Optional[_Union[ObjectStorageReaderFormat.Csv.AdditionalReaderOptions, _Mapping]] = ...) -> None: ...
    class Avro(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Parquet(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    CSV_FIELD_NUMBER: _ClassVar[int]
    PARQUET_FIELD_NUMBER: _ClassVar[int]
    AVRO_FIELD_NUMBER: _ClassVar[int]
    JSONL_FIELD_NUMBER: _ClassVar[int]
    PROTO_FIELD_NUMBER: _ClassVar[int]
    csv: ObjectStorageReaderFormat.Csv
    parquet: ObjectStorageReaderFormat.Parquet
    avro: ObjectStorageReaderFormat.Avro
    jsonl: ObjectStorageReaderFormat.Jsonl
    proto: _parsers_pb2.ProtoParser
    def __init__(self, csv: _Optional[_Union[ObjectStorageReaderFormat.Csv, _Mapping]] = ..., parquet: _Optional[_Union[ObjectStorageReaderFormat.Parquet, _Mapping]] = ..., avro: _Optional[_Union[ObjectStorageReaderFormat.Avro, _Mapping]] = ..., jsonl: _Optional[_Union[ObjectStorageReaderFormat.Jsonl, _Mapping]] = ..., proto: _Optional[_Union[_parsers_pb2.ProtoParser, _Mapping]] = ...) -> None: ...

class ObjectStorageDataSchema(_message.Message):
    __slots__ = ("infer", "data_schema")
    INFER_FIELD_NUMBER: _ClassVar[int]
    DATA_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    infer: _empty_pb2.Empty
    data_schema: _common_pb2.DataSchema
    def __init__(self, infer: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., data_schema: _Optional[_Union[_common_pb2.DataSchema, _Mapping]] = ...) -> None: ...

class ObjectStorageResultTable(_message.Message):
    __slots__ = ("table_namespace", "table_name", "add_system_cols")
    TABLE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    ADD_SYSTEM_COLS_FIELD_NUMBER: _ClassVar[int]
    table_namespace: str
    table_name: str
    add_system_cols: bool
    def __init__(self, table_namespace: _Optional[str] = ..., table_name: _Optional[str] = ..., add_system_cols: bool = ...) -> None: ...

class ObjectStorageSourceAdvancedSettings(_message.Message):
    __slots__ = ("unparsed_mode",)
    UNPARSED_MODE_FIELD_NUMBER: _ClassVar[int]
    unparsed_mode: ObjectStorageUnparsed
    def __init__(self, unparsed_mode: _Optional[_Union[ObjectStorageUnparsed, str]] = ...) -> None: ...

class ObjectStorageEventSource(_message.Message):
    __slots__ = ("sqs", "sns", "pub_sub")
    class SQS(_message.Message):
        __slots__ = ("queue_name", "owner_id", "aws_access_key_id", "aws_secret_access_key", "endpoint", "region", "use_ssl", "verify_ssl_cert")
        QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
        OWNER_ID_FIELD_NUMBER: _ClassVar[int]
        AWS_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        AWS_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        REGION_FIELD_NUMBER: _ClassVar[int]
        USE_SSL_FIELD_NUMBER: _ClassVar[int]
        VERIFY_SSL_CERT_FIELD_NUMBER: _ClassVar[int]
        queue_name: str
        owner_id: str
        aws_access_key_id: str
        aws_secret_access_key: str
        endpoint: str
        region: str
        use_ssl: bool
        verify_ssl_cert: bool
        def __init__(self, queue_name: _Optional[str] = ..., owner_id: _Optional[str] = ..., aws_access_key_id: _Optional[str] = ..., aws_secret_access_key: _Optional[str] = ..., endpoint: _Optional[str] = ..., region: _Optional[str] = ..., use_ssl: bool = ..., verify_ssl_cert: bool = ...) -> None: ...
    class SNS(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class PubSub(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    SQS_FIELD_NUMBER: _ClassVar[int]
    SNS_FIELD_NUMBER: _ClassVar[int]
    PUB_SUB_FIELD_NUMBER: _ClassVar[int]
    sqs: ObjectStorageEventSource.SQS
    sns: ObjectStorageEventSource.SNS
    pub_sub: ObjectStorageEventSource.PubSub
    def __init__(self, sqs: _Optional[_Union[ObjectStorageEventSource.SQS, _Mapping]] = ..., sns: _Optional[_Union[ObjectStorageEventSource.SNS, _Mapping]] = ..., pub_sub: _Optional[_Union[ObjectStorageEventSource.PubSub, _Mapping]] = ...) -> None: ...

class ObjectStorageSource(_message.Message):
    __slots__ = ("provider", "format", "path_pattern", "result_table", "result_schema", "event_source", "advanced_settings")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    PATH_PATTERN_FIELD_NUMBER: _ClassVar[int]
    RESULT_TABLE_FIELD_NUMBER: _ClassVar[int]
    RESULT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    EVENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    provider: ObjectStorageProvider
    format: ObjectStorageReaderFormat
    path_pattern: str
    result_table: ObjectStorageResultTable
    result_schema: ObjectStorageDataSchema
    event_source: ObjectStorageEventSource
    advanced_settings: ObjectStorageSourceAdvancedSettings
    def __init__(self, provider: _Optional[_Union[ObjectStorageProvider, _Mapping]] = ..., format: _Optional[_Union[ObjectStorageReaderFormat, _Mapping]] = ..., path_pattern: _Optional[str] = ..., result_table: _Optional[_Union[ObjectStorageResultTable, _Mapping]] = ..., result_schema: _Optional[_Union[ObjectStorageDataSchema, _Mapping]] = ..., event_source: _Optional[_Union[ObjectStorageEventSource, _Mapping]] = ..., advanced_settings: _Optional[_Union[ObjectStorageSourceAdvancedSettings, _Mapping]] = ...) -> None: ...
