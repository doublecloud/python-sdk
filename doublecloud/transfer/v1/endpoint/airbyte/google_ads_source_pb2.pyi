from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GoogleAdsSource(_message.Message):
    __slots__ = ("customer_id", "start_date", "end_date", "custom_queries", "login_customer_id", "conversion_window_days", "credentials")
    class Credentials(_message.Message):
        __slots__ = ("developer_token", "client_id", "client_secret", "access_token", "refresh_token")
        DEVELOPER_TOKEN_FIELD_NUMBER: _ClassVar[int]
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
        ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
        developer_token: str
        client_id: str
        client_secret: str
        access_token: str
        refresh_token: str
        def __init__(self, developer_token: _Optional[str] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ...) -> None: ...
    class CustomQuery(_message.Message):
        __slots__ = ("query", "table_name")
        QUERY_FIELD_NUMBER: _ClassVar[int]
        TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
        query: str
        table_name: str
        def __init__(self, query: _Optional[str] = ..., table_name: _Optional[str] = ...) -> None: ...
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_QUERIES_FIELD_NUMBER: _ClassVar[int]
    LOGIN_CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_WINDOW_DAYS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    start_date: str
    end_date: str
    custom_queries: _containers.RepeatedCompositeFieldContainer[GoogleAdsSource.CustomQuery]
    login_customer_id: str
    conversion_window_days: float
    credentials: GoogleAdsSource.Credentials
    def __init__(self, customer_id: _Optional[str] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ..., custom_queries: _Optional[_Iterable[_Union[GoogleAdsSource.CustomQuery, _Mapping]]] = ..., login_customer_id: _Optional[str] = ..., conversion_window_days: _Optional[float] = ..., credentials: _Optional[_Union[GoogleAdsSource.Credentials, _Mapping]] = ...) -> None: ...
