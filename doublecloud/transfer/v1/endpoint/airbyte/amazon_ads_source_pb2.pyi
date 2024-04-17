from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AmazonAdsSource(_message.Message):
    __slots__ = ("client_id", "client_secret", "scope", "refresh_token", "start_date", "region", "profiles")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    PROFILES_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    client_secret: str
    scope: str
    refresh_token: str
    start_date: str
    region: str
    profiles: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., scope: _Optional[str] = ..., refresh_token: _Optional[str] = ..., start_date: _Optional[str] = ..., region: _Optional[str] = ..., profiles: _Optional[_Iterable[float]] = ...) -> None: ...
