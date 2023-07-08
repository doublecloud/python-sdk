from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KafkaConfig(_message.Message):
    __slots__ = ["message_max_bytes", "replica_fetch_max_bytes"]
    MESSAGE_MAX_BYTES_FIELD_NUMBER: _ClassVar[int]
    REPLICA_FETCH_MAX_BYTES_FIELD_NUMBER: _ClassVar[int]
    message_max_bytes: _wrappers_pb2.Int64Value
    replica_fetch_max_bytes: _wrappers_pb2.Int64Value
    def __init__(self, message_max_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., replica_fetch_max_bytes: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class SchemaRegistryConfig(_message.Message):
    __slots__ = ["enabled"]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class RestAPIConfig(_message.Message):
    __slots__ = ["enabled"]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...
