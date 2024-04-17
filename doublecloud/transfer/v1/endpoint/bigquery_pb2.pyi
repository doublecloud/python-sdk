from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BigQueryTarget(_message.Message):
    __slots__ = ("project_id", "dataset_id", "credentials_json")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_JSON_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    credentials_json: str
    def __init__(self, project_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., credentials_json: _Optional[str] = ...) -> None: ...
