from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GroupMappingItem(_message.Message):
    __slots__ = ("external_group_id", "internal_group_id")
    EXTERNAL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    external_group_id: str
    internal_group_id: str
    def __init__(self, external_group_id: _Optional[str] = ..., internal_group_id: _Optional[str] = ...) -> None: ...

class GroupMapping(_message.Message):
    __slots__ = ("federation_id", "enabled")
    FEDERATION_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    federation_id: str
    enabled: bool
    def __init__(self, federation_id: _Optional[str] = ..., enabled: bool = ...) -> None: ...
