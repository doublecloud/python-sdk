from google.protobuf import duration_pb2 as _duration_pb2
from doublecloud.organizationmanager.v1 import group_mapping_pb2 as _group_mapping_pb2
from doublecloud.v1 import operation_pb2 as _operation_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetGroupMappingRequest(_message.Message):
    __slots__ = ("federation_id",)
    FEDERATION_ID_FIELD_NUMBER: _ClassVar[int]
    federation_id: str
    def __init__(self, federation_id: _Optional[str] = ...) -> None: ...

class GetGroupMappingResponse(_message.Message):
    __slots__ = ("group_mapping",)
    GROUP_MAPPING_FIELD_NUMBER: _ClassVar[int]
    group_mapping: _group_mapping_pb2.GroupMapping
    def __init__(self, group_mapping: _Optional[_Union[_group_mapping_pb2.GroupMapping, _Mapping]] = ...) -> None: ...

class CreateGroupMappingRequest(_message.Message):
    __slots__ = ("federation_id", "enabled")
    FEDERATION_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    federation_id: str
    enabled: bool
    def __init__(self, federation_id: _Optional[str] = ..., enabled: bool = ...) -> None: ...

class UpdateGroupMappingRequest(_message.Message):
    __slots__ = ("federation_id", "enabled")
    FEDERATION_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    federation_id: str
    enabled: bool
    def __init__(self, federation_id: _Optional[str] = ..., enabled: bool = ...) -> None: ...

class DeleteGroupMappingRequest(_message.Message):
    __slots__ = ("federation_id",)
    FEDERATION_ID_FIELD_NUMBER: _ClassVar[int]
    federation_id: str
    def __init__(self, federation_id: _Optional[str] = ...) -> None: ...

class UpdateGroupMappingItemsRequest(_message.Message):
    __slots__ = ("federation_id", "group_mapping_item_deltas")
    FEDERATION_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_MAPPING_ITEM_DELTAS_FIELD_NUMBER: _ClassVar[int]
    federation_id: str
    group_mapping_item_deltas: _containers.RepeatedCompositeFieldContainer[GroupMappingItemDelta]
    def __init__(self, federation_id: _Optional[str] = ..., group_mapping_item_deltas: _Optional[_Iterable[_Union[GroupMappingItemDelta, _Mapping]]] = ...) -> None: ...

class GroupMappingItemDelta(_message.Message):
    __slots__ = ("item", "action")
    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_UNSPECIFIED: _ClassVar[GroupMappingItemDelta.Action]
        ADD: _ClassVar[GroupMappingItemDelta.Action]
        REMOVE: _ClassVar[GroupMappingItemDelta.Action]
    ACTION_UNSPECIFIED: GroupMappingItemDelta.Action
    ADD: GroupMappingItemDelta.Action
    REMOVE: GroupMappingItemDelta.Action
    ITEM_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    item: _group_mapping_pb2.GroupMappingItem
    action: GroupMappingItemDelta.Action
    def __init__(self, item: _Optional[_Union[_group_mapping_pb2.GroupMappingItem, _Mapping]] = ..., action: _Optional[_Union[GroupMappingItemDelta.Action, str]] = ...) -> None: ...

class UpdateGroupMappingItemsResponse(_message.Message):
    __slots__ = ("group_mapping_item_deltas",)
    GROUP_MAPPING_ITEM_DELTAS_FIELD_NUMBER: _ClassVar[int]
    group_mapping_item_deltas: _containers.RepeatedCompositeFieldContainer[GroupMappingItemDelta]
    def __init__(self, group_mapping_item_deltas: _Optional[_Iterable[_Union[GroupMappingItemDelta, _Mapping]]] = ...) -> None: ...

class ListGroupMappingItemsRequest(_message.Message):
    __slots__ = ("federation_id", "page_size", "page_token", "filter")
    FEDERATION_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    federation_id: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, federation_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListGroupMappingItemsResponse(_message.Message):
    __slots__ = ("group_mapping_items", "next_page_token")
    GROUP_MAPPING_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    group_mapping_items: _containers.RepeatedCompositeFieldContainer[_group_mapping_pb2.GroupMappingItem]
    next_page_token: str
    def __init__(self, group_mapping_items: _Optional[_Iterable[_Union[_group_mapping_pb2.GroupMappingItem, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
