from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HubspotSource(_message.Message):
    __slots__ = ("start_date", "credentials", "enable_experimental_streams")
    class Credentials(_message.Message):
        __slots__ = ("private_app",)
        class PrivateApp(_message.Message):
            __slots__ = ("access_token",)
            ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
            access_token: str
            def __init__(self, access_token: _Optional[str] = ...) -> None: ...
        PRIVATE_APP_FIELD_NUMBER: _ClassVar[int]
        private_app: HubspotSource.Credentials.PrivateApp
        def __init__(self, private_app: _Optional[_Union[HubspotSource.Credentials.PrivateApp, _Mapping]] = ...) -> None: ...
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_EXPERIMENTAL_STREAMS_FIELD_NUMBER: _ClassVar[int]
    start_date: str
    credentials: HubspotSource.Credentials
    enable_experimental_streams: bool
    def __init__(self, start_date: _Optional[str] = ..., credentials: _Optional[_Union[HubspotSource.Credentials, _Mapping]] = ..., enable_experimental_streams: bool = ...) -> None: ...
