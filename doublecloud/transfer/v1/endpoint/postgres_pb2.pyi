from doublecloud.transfer.v1.endpoint import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostgresObjectTransferSettings(_message.Message):
    __slots__ = ("sequence", "sequence_owned_by", "table", "primary_key", "fk_constraint", "default_values", "constraint", "index", "view", "function", "trigger", "type", "rule", "collation", "policy", "cast", "materialized_view", "sequence_set")
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_OWNED_BY_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    FK_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUES_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    COLLATION_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    CAST_FIELD_NUMBER: _ClassVar[int]
    MATERIALIZED_VIEW_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_SET_FIELD_NUMBER: _ClassVar[int]
    sequence: _common_pb2.ObjectTransferStage
    sequence_owned_by: _common_pb2.ObjectTransferStage
    table: _common_pb2.ObjectTransferStage
    primary_key: _common_pb2.ObjectTransferStage
    fk_constraint: _common_pb2.ObjectTransferStage
    default_values: _common_pb2.ObjectTransferStage
    constraint: _common_pb2.ObjectTransferStage
    index: _common_pb2.ObjectTransferStage
    view: _common_pb2.ObjectTransferStage
    function: _common_pb2.ObjectTransferStage
    trigger: _common_pb2.ObjectTransferStage
    type: _common_pb2.ObjectTransferStage
    rule: _common_pb2.ObjectTransferStage
    collation: _common_pb2.ObjectTransferStage
    policy: _common_pb2.ObjectTransferStage
    cast: _common_pb2.ObjectTransferStage
    materialized_view: _common_pb2.ObjectTransferStage
    sequence_set: _common_pb2.ObjectTransferStage
    def __init__(self, sequence: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., sequence_owned_by: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., table: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., primary_key: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., fk_constraint: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., default_values: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., constraint: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., index: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., view: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., function: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., trigger: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., type: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., rule: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., collation: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., policy: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., cast: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., materialized_view: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., sequence_set: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ...) -> None: ...

class OnPremisePostgres(_message.Message):
    __slots__ = ("port", "hosts", "tls_mode")
    PORT_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    TLS_MODE_FIELD_NUMBER: _ClassVar[int]
    port: int
    hosts: _containers.RepeatedScalarFieldContainer[str]
    tls_mode: _common_pb2.TLSMode
    def __init__(self, port: _Optional[int] = ..., hosts: _Optional[_Iterable[str]] = ..., tls_mode: _Optional[_Union[_common_pb2.TLSMode, _Mapping]] = ...) -> None: ...

class PostgresConnection(_message.Message):
    __slots__ = ("on_premise",)
    ON_PREMISE_FIELD_NUMBER: _ClassVar[int]
    on_premise: OnPremisePostgres
    def __init__(self, on_premise: _Optional[_Union[OnPremisePostgres, _Mapping]] = ...) -> None: ...

class PostgresSource(_message.Message):
    __slots__ = ("connection", "database", "user", "password", "include_tables", "exclude_tables", "slot_byte_lag_limit", "service_schema", "object_transfer_settings")
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TABLES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_TABLES_FIELD_NUMBER: _ClassVar[int]
    SLOT_BYTE_LAG_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TRANSFER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    connection: PostgresConnection
    database: str
    user: str
    password: _common_pb2.Secret
    include_tables: _containers.RepeatedScalarFieldContainer[str]
    exclude_tables: _containers.RepeatedScalarFieldContainer[str]
    slot_byte_lag_limit: int
    service_schema: str
    object_transfer_settings: PostgresObjectTransferSettings
    def __init__(self, connection: _Optional[_Union[PostgresConnection, _Mapping]] = ..., database: _Optional[str] = ..., user: _Optional[str] = ..., password: _Optional[_Union[_common_pb2.Secret, _Mapping]] = ..., include_tables: _Optional[_Iterable[str]] = ..., exclude_tables: _Optional[_Iterable[str]] = ..., slot_byte_lag_limit: _Optional[int] = ..., service_schema: _Optional[str] = ..., object_transfer_settings: _Optional[_Union[PostgresObjectTransferSettings, _Mapping]] = ...) -> None: ...

class PostgresTarget(_message.Message):
    __slots__ = ("connection", "database", "user", "password", "cleanup_policy", "security_groups")
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_POLICY_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUPS_FIELD_NUMBER: _ClassVar[int]
    connection: PostgresConnection
    database: str
    user: str
    password: _common_pb2.Secret
    cleanup_policy: _common_pb2.CleanupPolicy
    security_groups: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, connection: _Optional[_Union[PostgresConnection, _Mapping]] = ..., database: _Optional[str] = ..., user: _Optional[str] = ..., password: _Optional[_Union[_common_pb2.Secret, _Mapping]] = ..., cleanup_policy: _Optional[_Union[_common_pb2.CleanupPolicy, str]] = ..., security_groups: _Optional[_Iterable[str]] = ...) -> None: ...
