from doublecloud.transfer.v1.endpoint import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OnPremiseMysql(_message.Message):
    __slots__ = ("port", "hosts", "tls_mode")
    PORT_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    TLS_MODE_FIELD_NUMBER: _ClassVar[int]
    port: int
    hosts: _containers.RepeatedScalarFieldContainer[str]
    tls_mode: _common_pb2.TLSMode
    def __init__(self, port: _Optional[int] = ..., hosts: _Optional[_Iterable[str]] = ..., tls_mode: _Optional[_Union[_common_pb2.TLSMode, _Mapping]] = ...) -> None: ...

class MysqlConnection(_message.Message):
    __slots__ = ("on_premise",)
    ON_PREMISE_FIELD_NUMBER: _ClassVar[int]
    on_premise: OnPremiseMysql
    def __init__(self, on_premise: _Optional[_Union[OnPremiseMysql, _Mapping]] = ...) -> None: ...

class MysqlObjectTransferSettings(_message.Message):
    __slots__ = ("view", "routine", "trigger", "tables")
    VIEW_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    view: _common_pb2.ObjectTransferStage
    routine: _common_pb2.ObjectTransferStage
    trigger: _common_pb2.ObjectTransferStage
    tables: _common_pb2.ObjectTransferStage
    def __init__(self, view: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., routine: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., trigger: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ..., tables: _Optional[_Union[_common_pb2.ObjectTransferStage, str]] = ...) -> None: ...

class MysqlSource(_message.Message):
    __slots__ = ("connection", "database", "user", "password", "timezone", "object_transfer_settings", "include_tables_regex", "exclude_tables_regex", "service_database")
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TRANSFER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TABLES_REGEX_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_TABLES_REGEX_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DATABASE_FIELD_NUMBER: _ClassVar[int]
    connection: MysqlConnection
    database: str
    user: str
    password: _common_pb2.Secret
    timezone: str
    object_transfer_settings: MysqlObjectTransferSettings
    include_tables_regex: _containers.RepeatedScalarFieldContainer[str]
    exclude_tables_regex: _containers.RepeatedScalarFieldContainer[str]
    service_database: str
    def __init__(self, connection: _Optional[_Union[MysqlConnection, _Mapping]] = ..., database: _Optional[str] = ..., user: _Optional[str] = ..., password: _Optional[_Union[_common_pb2.Secret, _Mapping]] = ..., timezone: _Optional[str] = ..., object_transfer_settings: _Optional[_Union[MysqlObjectTransferSettings, _Mapping]] = ..., include_tables_regex: _Optional[_Iterable[str]] = ..., exclude_tables_regex: _Optional[_Iterable[str]] = ..., service_database: _Optional[str] = ...) -> None: ...

class MysqlTarget(_message.Message):
    __slots__ = ("connection", "database", "user", "password", "sql_mode", "skip_constraint_checks", "timezone", "cleanup_policy", "service_database", "security_groups")
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SQL_MODE_FIELD_NUMBER: _ClassVar[int]
    SKIP_CONSTRAINT_CHECKS_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_POLICY_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DATABASE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_GROUPS_FIELD_NUMBER: _ClassVar[int]
    connection: MysqlConnection
    database: str
    user: str
    password: _common_pb2.Secret
    sql_mode: str
    skip_constraint_checks: bool
    timezone: str
    cleanup_policy: _common_pb2.CleanupPolicy
    service_database: str
    security_groups: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, connection: _Optional[_Union[MysqlConnection, _Mapping]] = ..., database: _Optional[str] = ..., user: _Optional[str] = ..., password: _Optional[_Union[_common_pb2.Secret, _Mapping]] = ..., sql_mode: _Optional[str] = ..., skip_constraint_checks: bool = ..., timezone: _Optional[str] = ..., cleanup_policy: _Optional[_Union[_common_pb2.CleanupPolicy, str]] = ..., service_database: _Optional[str] = ..., security_groups: _Optional[_Iterable[str]] = ...) -> None: ...
