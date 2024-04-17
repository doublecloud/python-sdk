from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LinkedinAdsSource(_message.Message):
    __slots__ = ("start_date", "account_ids", "credentials")
    class Credentials(_message.Message):
        __slots__ = ("oauth", "access_token")
        class OAuth(_message.Message):
            __slots__ = ("client_id", "client_secret", "refresh_token")
            CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
            CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
            REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
            client_id: str
            client_secret: str
            refresh_token: str
            def __init__(self, client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., refresh_token: _Optional[str] = ...) -> None: ...
        OAUTH_FIELD_NUMBER: _ClassVar[int]
        ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        oauth: LinkedinAdsSource.Credentials.OAuth
        access_token: str
        def __init__(self, oauth: _Optional[_Union[LinkedinAdsSource.Credentials.OAuth, _Mapping]] = ..., access_token: _Optional[str] = ...) -> None: ...
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    start_date: str
    account_ids: _containers.RepeatedScalarFieldContainer[int]
    credentials: LinkedinAdsSource.Credentials
    def __init__(self, start_date: _Optional[str] = ..., account_ids: _Optional[_Iterable[int]] = ..., credentials: _Optional[_Union[LinkedinAdsSource.Credentials, _Mapping]] = ...) -> None: ...
