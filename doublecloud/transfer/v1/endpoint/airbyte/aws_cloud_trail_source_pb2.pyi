from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AWSCloudTrailSource(_message.Message):
    __slots__ = ("aws_key_id", "aws_secret_key", "aws_region_name", "start_date")
    AWS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    AWS_REGION_NAME_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    aws_key_id: str
    aws_secret_key: str
    aws_region_name: str
    start_date: str
    def __init__(self, aws_key_id: _Optional[str] = ..., aws_secret_key: _Optional[str] = ..., aws_region_name: _Optional[str] = ..., start_date: _Optional[str] = ...) -> None: ...
