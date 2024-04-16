from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InstagramSource(_message.Message):
    __slots__ = ("start_date", "access_token")
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    start_date: str
    access_token: str
    def __init__(self, start_date: _Optional[str] = ..., access_token: _Optional[str] = ...) -> None: ...
