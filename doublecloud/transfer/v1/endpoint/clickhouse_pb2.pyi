from google.protobuf import empty_pb2 as _empty_pb2
from doublecloud.transfer.v1.endpoint import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClickhouseCleanupPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLICKHOUSE_CLEANUP_POLICY_UNSPECIFIED: _ClassVar[ClickhouseCleanupPolicy]
    CLICKHOUSE_CLEANUP_POLICY_DISABLED: _ClassVar[ClickhouseCleanupPolicy]
    CLICKHOUSE_CLEANUP_POLICY_DROP: _ClassVar[ClickhouseCleanupPolicy]
    CLICKHOUSE_CLEANUP_POLICY_TRUNCATE: _ClassVar[ClickhouseCleanupPolicy]
CLICKHOUSE_CLEANUP_POLICY_UNSPECIFIED: ClickhouseCleanupPolicy
CLICKHOUSE_CLEANUP_POLICY_DISABLED: ClickhouseCleanupPolicy
CLICKHOUSE_CLEANUP_POLICY_DROP: ClickhouseCleanupPolicy
CLICKHOUSE_CLEANUP_POLICY_TRUNCATE: ClickhouseCleanupPolicy

class ClickhouseShard(_message.Message):
    __slots__ = ("name", "hosts")
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    hosts: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., hosts: _Optional[_Iterable[str]] = ...) -> None: ...

class OnPremiseClickhouse(_message.Message):
    __slots__ = ("shards", "http_port", "native_port", "tls_mode")
    SHARDS_FIELD_NUMBER: _ClassVar[int]
    HTTP_PORT_FIELD_NUMBER: _ClassVar[int]
    NATIVE_PORT_FIELD_NUMBER: _ClassVar[int]
    TLS_MODE_FIELD_NUMBER: _ClassVar[int]
    shards: _containers.RepeatedCompositeFieldContainer[ClickhouseShard]
    http_port: int
    native_port: int
    tls_mode: _common_pb2.TLSMode
    def __init__(self, shards: _Optional[_Iterable[_Union[ClickhouseShard, _Mapping]]] = ..., http_port: _Optional[int] = ..., native_port: _Optional[int] = ..., tls_mode: _Optional[_Union[_common_pb2.TLSMode, _Mapping]] = ...) -> None: ...

class ClickhouseConnectionOptions(_message.Message):
    __slots__ = ("on_premise", "mdb_cluster_id", "user", "password", "database")
    ON_PREMISE_FIELD_NUMBER: _ClassVar[int]
    MDB_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    on_premise: OnPremiseClickhouse
    mdb_cluster_id: str
    user: str
    password: _common_pb2.Secret
    database: str
    def __init__(self, on_premise: _Optional[_Union[OnPremiseClickhouse, _Mapping]] = ..., mdb_cluster_id: _Optional[str] = ..., user: _Optional[str] = ..., password: _Optional[_Union[_common_pb2.Secret, _Mapping]] = ..., database: _Optional[str] = ...) -> None: ...

class ClickhouseConnection(_message.Message):
    __slots__ = ("connection_options",)
    CONNECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    connection_options: ClickhouseConnectionOptions
    def __init__(self, connection_options: _Optional[_Union[ClickhouseConnectionOptions, _Mapping]] = ...) -> None: ...

class ClickhouseSharding(_message.Message):
    __slots__ = ("column_value_hash", "custom_mapping", "transfer_id", "round_robin")
    class ColumnValueHash(_message.Message):
        __slots__ = ("column_name",)
        COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
        column_name: str
        def __init__(self, column_name: _Optional[str] = ...) -> None: ...
    class ColumnValueMapping(_message.Message):
        __slots__ = ("column_name", "mapping")
        class ValueToShard(_message.Message):
            __slots__ = ("column_value", "shard_name")
            COLUMN_VALUE_FIELD_NUMBER: _ClassVar[int]
            SHARD_NAME_FIELD_NUMBER: _ClassVar[int]
            column_value: _common_pb2.ColumnValue
            shard_name: str
            def __init__(self, column_value: _Optional[_Union[_common_pb2.ColumnValue, _Mapping]] = ..., shard_name: _Optional[str] = ...) -> None: ...
        COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
        MAPPING_FIELD_NUMBER: _ClassVar[int]
        column_name: str
        mapping: _containers.RepeatedCompositeFieldContainer[ClickhouseSharding.ColumnValueMapping.ValueToShard]
        def __init__(self, column_name: _Optional[str] = ..., mapping: _Optional[_Iterable[_Union[ClickhouseSharding.ColumnValueMapping.ValueToShard, _Mapping]]] = ...) -> None: ...
    COLUMN_VALUE_HASH_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_MAPPING_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_ID_FIELD_NUMBER: _ClassVar[int]
    ROUND_ROBIN_FIELD_NUMBER: _ClassVar[int]
    column_value_hash: ClickhouseSharding.ColumnValueHash
    custom_mapping: ClickhouseSharding.ColumnValueMapping
    transfer_id: _empty_pb2.Empty
    round_robin: _empty_pb2.Empty
    def __init__(self, column_value_hash: _Optional[_Union[ClickhouseSharding.ColumnValueHash, _Mapping]] = ..., custom_mapping: _Optional[_Union[ClickhouseSharding.ColumnValueMapping, _Mapping]] = ..., transfer_id: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., round_robin: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ...) -> None: ...

class ClickhouseMigrationOptions(_message.Message):
    __slots__ = ("add_new_columns",)
    ADD_NEW_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    add_new_columns: bool
    def __init__(self, add_new_columns: bool = ...) -> None: ...

class ClickhouseInsertOptions(_message.Message):
    __slots__ = ("materialized_views_ignore_errors",)
    MATERIALIZED_VIEWS_IGNORE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    materialized_views_ignore_errors: bool
    def __init__(self, materialized_views_ignore_errors: bool = ...) -> None: ...

class ClickhouseSource(_message.Message):
    __slots__ = ("connection", "include_tables", "exclude_tables")
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TABLES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_TABLES_FIELD_NUMBER: _ClassVar[int]
    connection: ClickhouseConnection
    include_tables: _containers.RepeatedScalarFieldContainer[str]
    exclude_tables: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, connection: _Optional[_Union[ClickhouseConnection, _Mapping]] = ..., include_tables: _Optional[_Iterable[str]] = ..., exclude_tables: _Optional[_Iterable[str]] = ...) -> None: ...

class ClickhouseTarget(_message.Message):
    __slots__ = ("connection", "alt_names", "migration_options", "cleanup_policy", "sharding", "insert_options", "clickhouse_cluster_name")
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    ALT_NAMES_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_POLICY_FIELD_NUMBER: _ClassVar[int]
    SHARDING_FIELD_NUMBER: _ClassVar[int]
    INSERT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CLICKHOUSE_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    connection: ClickhouseConnection
    alt_names: _containers.RepeatedCompositeFieldContainer[_common_pb2.AltName]
    migration_options: ClickhouseMigrationOptions
    cleanup_policy: ClickhouseCleanupPolicy
    sharding: ClickhouseSharding
    insert_options: ClickhouseInsertOptions
    clickhouse_cluster_name: str
    def __init__(self, connection: _Optional[_Union[ClickhouseConnection, _Mapping]] = ..., alt_names: _Optional[_Iterable[_Union[_common_pb2.AltName, _Mapping]]] = ..., migration_options: _Optional[_Union[ClickhouseMigrationOptions, _Mapping]] = ..., cleanup_policy: _Optional[_Union[ClickhouseCleanupPolicy, str]] = ..., sharding: _Optional[_Union[ClickhouseSharding, _Mapping]] = ..., insert_options: _Optional[_Union[ClickhouseInsertOptions, _Mapping]] = ..., clickhouse_cluster_name: _Optional[str] = ...) -> None: ...
