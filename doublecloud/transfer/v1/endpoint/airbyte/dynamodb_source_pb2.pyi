from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DynamodbSource(_message.Message):
    __slots__ = ("region", "aws_access_key_id", "aws_secret_access_key", "reserved_attribute_names", "ignore_missing_read_permissions_tables")
    REGION_FIELD_NUMBER: _ClassVar[int]
    AWS_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    RESERVED_ATTRIBUTE_NAMES_FIELD_NUMBER: _ClassVar[int]
    IGNORE_MISSING_READ_PERMISSIONS_TABLES_FIELD_NUMBER: _ClassVar[int]
    region: str
    aws_access_key_id: str
    aws_secret_access_key: str
    reserved_attribute_names: _containers.RepeatedScalarFieldContainer[str]
    ignore_missing_read_permissions_tables: bool
    def __init__(self, region: _Optional[str] = ..., aws_access_key_id: _Optional[str] = ..., aws_secret_access_key: _Optional[str] = ..., reserved_attribute_names: _Optional[_Iterable[str]] = ..., ignore_missing_read_permissions_tables: bool = ...) -> None: ...
