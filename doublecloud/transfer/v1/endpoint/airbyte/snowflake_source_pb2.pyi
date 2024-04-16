from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnowflakeSource(_message.Message):
    __slots__ = ("host", "role", "warehouse", "database", "schema", "jdbc_url_params", "credentials")
    class Credentials(_message.Message):
        __slots__ = ("oauth", "basic_auth")
        class OAuth(_message.Message):
            __slots__ = ("client_id", "client_secret", "access_token", "refresh_token")
            CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
            CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
            ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
            REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
            client_id: str
            client_secret: str
            access_token: str
            refresh_token: str
            def __init__(self, client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ...) -> None: ...
        class BasicAuth(_message.Message):
            __slots__ = ("username", "password")
            USERNAME_FIELD_NUMBER: _ClassVar[int]
            PASSWORD_FIELD_NUMBER: _ClassVar[int]
            username: str
            password: str
            def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...
        OAUTH_FIELD_NUMBER: _ClassVar[int]
        BASIC_AUTH_FIELD_NUMBER: _ClassVar[int]
        oauth: SnowflakeSource.Credentials.OAuth
        basic_auth: SnowflakeSource.Credentials.BasicAuth
        def __init__(self, oauth: _Optional[_Union[SnowflakeSource.Credentials.OAuth, _Mapping]] = ..., basic_auth: _Optional[_Union[SnowflakeSource.Credentials.BasicAuth, _Mapping]] = ...) -> None: ...
    HOST_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    JDBC_URL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    host: str
    role: str
    warehouse: str
    database: str
    schema: str
    jdbc_url_params: str
    credentials: SnowflakeSource.Credentials
    def __init__(self, host: _Optional[str] = ..., role: _Optional[str] = ..., warehouse: _Optional[str] = ..., database: _Optional[str] = ..., schema: _Optional[str] = ..., jdbc_url_params: _Optional[str] = ..., credentials: _Optional[_Union[SnowflakeSource.Credentials, _Mapping]] = ...) -> None: ...
