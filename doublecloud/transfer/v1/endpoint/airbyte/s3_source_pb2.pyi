from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class S3Source(_message.Message):
    __slots__ = ("dataset", "path_pattern", "schema", "format", "provider")
    class Format(_message.Message):
        __slots__ = ("csv", "parquet", "avro", "jsonl")
        CSV_FIELD_NUMBER: _ClassVar[int]
        PARQUET_FIELD_NUMBER: _ClassVar[int]
        AVRO_FIELD_NUMBER: _ClassVar[int]
        JSONL_FIELD_NUMBER: _ClassVar[int]
        csv: S3Source.Csv
        parquet: S3Source.Parquet
        avro: S3Source.Avro
        jsonl: S3Source.Jsonl
        def __init__(self, csv: _Optional[_Union[S3Source.Csv, _Mapping]] = ..., parquet: _Optional[_Union[S3Source.Parquet, _Mapping]] = ..., avro: _Optional[_Union[S3Source.Avro, _Mapping]] = ..., jsonl: _Optional[_Union[S3Source.Jsonl, _Mapping]] = ...) -> None: ...
    class Provider(_message.Message):
        __slots__ = ("bucket", "aws_access_key_id", "aws_secret_access_key", "path_prefix", "endpoint", "use_ssl", "verify_ssl_cert")
        BUCKET_FIELD_NUMBER: _ClassVar[int]
        AWS_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        AWS_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
        PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        USE_SSL_FIELD_NUMBER: _ClassVar[int]
        VERIFY_SSL_CERT_FIELD_NUMBER: _ClassVar[int]
        bucket: str
        aws_access_key_id: str
        aws_secret_access_key: str
        path_prefix: str
        endpoint: str
        use_ssl: bool
        verify_ssl_cert: bool
        def __init__(self, bucket: _Optional[str] = ..., aws_access_key_id: _Optional[str] = ..., aws_secret_access_key: _Optional[str] = ..., path_prefix: _Optional[str] = ..., endpoint: _Optional[str] = ..., use_ssl: bool = ..., verify_ssl_cert: bool = ...) -> None: ...
    class Csv(_message.Message):
        __slots__ = ("delimiter", "quote_char", "escape_char", "encoding", "double_quote", "newlines_in_values", "block_size", "additional_reader_options", "advanced_options")
        DELIMITER_FIELD_NUMBER: _ClassVar[int]
        QUOTE_CHAR_FIELD_NUMBER: _ClassVar[int]
        ESCAPE_CHAR_FIELD_NUMBER: _ClassVar[int]
        ENCODING_FIELD_NUMBER: _ClassVar[int]
        DOUBLE_QUOTE_FIELD_NUMBER: _ClassVar[int]
        NEWLINES_IN_VALUES_FIELD_NUMBER: _ClassVar[int]
        BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_READER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        ADVANCED_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        delimiter: str
        quote_char: str
        escape_char: str
        encoding: str
        double_quote: bool
        newlines_in_values: bool
        block_size: int
        additional_reader_options: str
        advanced_options: str
        def __init__(self, delimiter: _Optional[str] = ..., quote_char: _Optional[str] = ..., escape_char: _Optional[str] = ..., encoding: _Optional[str] = ..., double_quote: bool = ..., newlines_in_values: bool = ..., block_size: _Optional[int] = ..., additional_reader_options: _Optional[str] = ..., advanced_options: _Optional[str] = ...) -> None: ...
    class Avro(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Jsonl(_message.Message):
        __slots__ = ("newlines_in_values", "unexpected_field_behavior", "block_size")
        class UnexpectedFieldBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNEXPECTED_FIELD_BEHAVIOR_UNSPECIFIED: _ClassVar[S3Source.Jsonl.UnexpectedFieldBehavior]
            UNEXPECTED_FIELD_BEHAVIOR_IGNORE: _ClassVar[S3Source.Jsonl.UnexpectedFieldBehavior]
            UNEXPECTED_FIELD_BEHAVIOR_INFER: _ClassVar[S3Source.Jsonl.UnexpectedFieldBehavior]
            UNEXPECTED_FIELD_BEHAVIOR_ERROR: _ClassVar[S3Source.Jsonl.UnexpectedFieldBehavior]
        UNEXPECTED_FIELD_BEHAVIOR_UNSPECIFIED: S3Source.Jsonl.UnexpectedFieldBehavior
        UNEXPECTED_FIELD_BEHAVIOR_IGNORE: S3Source.Jsonl.UnexpectedFieldBehavior
        UNEXPECTED_FIELD_BEHAVIOR_INFER: S3Source.Jsonl.UnexpectedFieldBehavior
        UNEXPECTED_FIELD_BEHAVIOR_ERROR: S3Source.Jsonl.UnexpectedFieldBehavior
        NEWLINES_IN_VALUES_FIELD_NUMBER: _ClassVar[int]
        UNEXPECTED_FIELD_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
        newlines_in_values: bool
        unexpected_field_behavior: S3Source.Jsonl.UnexpectedFieldBehavior
        block_size: int
        def __init__(self, newlines_in_values: bool = ..., unexpected_field_behavior: _Optional[_Union[S3Source.Jsonl.UnexpectedFieldBehavior, str]] = ..., block_size: _Optional[int] = ...) -> None: ...
    class Parquet(_message.Message):
        __slots__ = ("buffer_size", "columns", "batch_size")
        BUFFER_SIZE_FIELD_NUMBER: _ClassVar[int]
        COLUMNS_FIELD_NUMBER: _ClassVar[int]
        BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
        buffer_size: int
        columns: _containers.RepeatedScalarFieldContainer[str]
        batch_size: int
        def __init__(self, buffer_size: _Optional[int] = ..., columns: _Optional[_Iterable[str]] = ..., batch_size: _Optional[int] = ...) -> None: ...
    DATASET_FIELD_NUMBER: _ClassVar[int]
    PATH_PATTERN_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    path_pattern: str
    schema: str
    format: S3Source.Format
    provider: S3Source.Provider
    def __init__(self, dataset: _Optional[str] = ..., path_pattern: _Optional[str] = ..., schema: _Optional[str] = ..., format: _Optional[_Union[S3Source.Format, _Mapping]] = ..., provider: _Optional[_Union[S3Source.Provider, _Mapping]] = ...) -> None: ...
