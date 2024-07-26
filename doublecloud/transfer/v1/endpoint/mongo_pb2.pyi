from doublecloud.transfer.v1.endpoint import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SrvMongo(_message.Message):
    __slots__ = ("hostname", "replica_set", "tls_mode")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    REPLICA_SET_FIELD_NUMBER: _ClassVar[int]
    TLS_MODE_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    replica_set: str
    tls_mode: _common_pb2.TLSMode
    def __init__(self, hostname: _Optional[str] = ..., replica_set: _Optional[str] = ..., tls_mode: _Optional[_Union[_common_pb2.TLSMode, _Mapping]] = ...) -> None: ...

class OnPremiseMongo(_message.Message):
    __slots__ = ("hosts", "port", "replica_set", "tls_mode")
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    REPLICA_SET_FIELD_NUMBER: _ClassVar[int]
    TLS_MODE_FIELD_NUMBER: _ClassVar[int]
    hosts: _containers.RepeatedScalarFieldContainer[str]
    port: int
    replica_set: str
    tls_mode: _common_pb2.TLSMode
    def __init__(self, hosts: _Optional[_Iterable[str]] = ..., port: _Optional[int] = ..., replica_set: _Optional[str] = ..., tls_mode: _Optional[_Union[_common_pb2.TLSMode, _Mapping]] = ...) -> None: ...

class MongoConnectionOptions(_message.Message):
    __slots__ = ("on_premise", "srv", "user", "password", "auth_source")
    ON_PREMISE_FIELD_NUMBER: _ClassVar[int]
    SRV_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    AUTH_SOURCE_FIELD_NUMBER: _ClassVar[int]
    on_premise: OnPremiseMongo
    srv: SrvMongo
    user: str
    password: _common_pb2.Secret
    auth_source: str
    def __init__(self, on_premise: _Optional[_Union[OnPremiseMongo, _Mapping]] = ..., srv: _Optional[_Union[SrvMongo, _Mapping]] = ..., user: _Optional[str] = ..., password: _Optional[_Union[_common_pb2.Secret, _Mapping]] = ..., auth_source: _Optional[str] = ...) -> None: ...

class MongoConnection(_message.Message):
    __slots__ = ("connection_options",)
    CONNECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    connection_options: MongoConnectionOptions
    def __init__(self, connection_options: _Optional[_Union[MongoConnectionOptions, _Mapping]] = ...) -> None: ...

class MongoCollection(_message.Message):
    __slots__ = ("database_name", "collection_name")
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    database_name: str
    collection_name: str
    def __init__(self, database_name: _Optional[str] = ..., collection_name: _Optional[str] = ...) -> None: ...

class MongoSource(_message.Message):
    __slots__ = ("connection", "collections", "excluded_collections", "secondary_preferred_mode")
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_PREFERRED_MODE_FIELD_NUMBER: _ClassVar[int]
    connection: MongoConnection
    collections: _containers.RepeatedCompositeFieldContainer[MongoCollection]
    excluded_collections: _containers.RepeatedCompositeFieldContainer[MongoCollection]
    secondary_preferred_mode: bool
    def __init__(self, connection: _Optional[_Union[MongoConnection, _Mapping]] = ..., collections: _Optional[_Iterable[_Union[MongoCollection, _Mapping]]] = ..., excluded_collections: _Optional[_Iterable[_Union[MongoCollection, _Mapping]]] = ..., secondary_preferred_mode: bool = ...) -> None: ...

class MongoTarget(_message.Message):
    __slots__ = ("connection", "database", "cleanup_policy")
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_POLICY_FIELD_NUMBER: _ClassVar[int]
    connection: MongoConnection
    database: str
    cleanup_policy: _common_pb2.CleanupPolicy
    def __init__(self, connection: _Optional[_Union[MongoConnection, _Mapping]] = ..., database: _Optional[str] = ..., cleanup_policy: _Optional[_Union[_common_pb2.CleanupPolicy, str]] = ...) -> None: ...
