from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MSSQLSource(_message.Message):
    __slots__ = ("host", "port", "database", "username", "password", "replication_method", "ssl_method")
    class MSSQLReplicationMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MSSQL_REPLICATION_METHOD_UNSPECIFIED: _ClassVar[MSSQLSource.MSSQLReplicationMethod]
        STANDARD: _ClassVar[MSSQLSource.MSSQLReplicationMethod]
        CDC: _ClassVar[MSSQLSource.MSSQLReplicationMethod]
    MSSQL_REPLICATION_METHOD_UNSPECIFIED: MSSQLSource.MSSQLReplicationMethod
    STANDARD: MSSQLSource.MSSQLReplicationMethod
    CDC: MSSQLSource.MSSQLReplicationMethod
    class SSLUnencrypted(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SSLEncryptedTrusted(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SSLEncryptedVerifyCert(_message.Message):
        __slots__ = ("host_name_in_certificate",)
        HOST_NAME_IN_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        host_name_in_certificate: str
        def __init__(self, host_name_in_certificate: _Optional[str] = ...) -> None: ...
    class SSLConfig(_message.Message):
        __slots__ = ("unencrypted", "encrypted_trust_server_certificate", "encrypted_verify_certificate")
        UNENCRYPTED_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_TRUST_SERVER_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_VERIFY_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
        unencrypted: MSSQLSource.SSLUnencrypted
        encrypted_trust_server_certificate: MSSQLSource.SSLEncryptedTrusted
        encrypted_verify_certificate: MSSQLSource.SSLEncryptedVerifyCert
        def __init__(self, unencrypted: _Optional[_Union[MSSQLSource.SSLUnencrypted, _Mapping]] = ..., encrypted_trust_server_certificate: _Optional[_Union[MSSQLSource.SSLEncryptedTrusted, _Mapping]] = ..., encrypted_verify_certificate: _Optional[_Union[MSSQLSource.SSLEncryptedVerifyCert, _Mapping]] = ...) -> None: ...
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    SSL_METHOD_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    database: str
    username: str
    password: str
    replication_method: MSSQLSource.MSSQLReplicationMethod
    ssl_method: MSSQLSource.SSLConfig
    def __init__(self, host: _Optional[str] = ..., port: _Optional[int] = ..., database: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., replication_method: _Optional[_Union[MSSQLSource.MSSQLReplicationMethod, str]] = ..., ssl_method: _Optional[_Union[MSSQLSource.SSLConfig, _Mapping]] = ...) -> None: ...
