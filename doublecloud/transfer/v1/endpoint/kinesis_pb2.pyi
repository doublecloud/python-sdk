from doublecloud.transfer.v1.endpoint import parsers_pb2 as _parsers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KinesisSource(_message.Message):
    __slots__ = ("region", "stream_name", "aws_access_key_id", "aws_secret_access_key", "parser")
    REGION_FIELD_NUMBER: _ClassVar[int]
    STREAM_NAME_FIELD_NUMBER: _ClassVar[int]
    AWS_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    PARSER_FIELD_NUMBER: _ClassVar[int]
    region: str
    stream_name: str
    aws_access_key_id: str
    aws_secret_access_key: str
    parser: _parsers_pb2.Parser
    def __init__(self, region: _Optional[str] = ..., stream_name: _Optional[str] = ..., aws_access_key_id: _Optional[str] = ..., aws_secret_access_key: _Optional[str] = ..., parser: _Optional[_Union[_parsers_pb2.Parser, _Mapping]] = ...) -> None: ...
