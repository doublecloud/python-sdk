from google.protobuf import duration_pb2 as _duration_pb2
from doublecloud.organizationmanager.v1 import group_pb2 as _group_pb2
from doublecloud.access.v1 import access_pb2 as _access_pb2
from doublecloud.v1 import operation_pb2 as _operation_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetGroupRequest(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class ListGroupsRequest(_message.Message):
    __slots__ = ("organization_id", "page_size", "page_token", "filter")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    page_size: int
    page_token: str
    filter: str
    def __init__(self, organization_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[str] = ...) -> None: ...

class ListGroupsResponse(_message.Message):
    __slots__ = ("groups", "next_page_token")
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[_group_pb2.Group]
    next_page_token: str
    def __init__(self, groups: _Optional[_Iterable[_Union[_group_pb2.Group, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreateGroupRequest(_message.Message):
    __slots__ = ("organization_id", "name", "description")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    name: str
    description: str
    def __init__(self, organization_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateGroupRequest(_message.Message):
    __slots__ = ("group_id", "name", "description")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    name: str
    description: str
    def __init__(self, group_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class DeleteGroupRequest(_message.Message):
    __slots__ = ("group_id",)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class ListGroupOperationsRequest(_message.Message):
    __slots__ = ("group_id", "page_size", "page_token")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    page_size: int
    page_token: str
    def __init__(self, group_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListGroupOperationsResponse(_message.Message):
    __slots__ = ("operations", "next_page_token")
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[_operation_pb2.Operation]
    next_page_token: str
    def __init__(self, operations: _Optional[_Iterable[_Union[_operation_pb2.Operation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ListGroupMembersRequest(_message.Message):
    __slots__ = ("group_id", "page_size", "page_token")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    page_size: int
    page_token: str
    def __init__(self, group_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListGroupMembersResponse(_message.Message):
    __slots__ = ("members", "next_page_token")
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[GroupMember]
    next_page_token: str
    def __init__(self, members: _Optional[_Iterable[_Union[GroupMember, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GroupMember(_message.Message):
    __slots__ = ("subject_id", "subject_type")
    SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    subject_id: str
    subject_type: str
    def __init__(self, subject_id: _Optional[str] = ..., subject_type: _Optional[str] = ...) -> None: ...

class UpdateGroupMembersRequest(_message.Message):
    __slots__ = ("group_id", "member_deltas")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_DELTAS_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    member_deltas: _containers.RepeatedCompositeFieldContainer[MemberDelta]
    def __init__(self, group_id: _Optional[str] = ..., member_deltas: _Optional[_Iterable[_Union[MemberDelta, _Mapping]]] = ...) -> None: ...

class MemberDelta(_message.Message):
    __slots__ = ("action", "subject_id")
    class MemberAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MEMBER_ACTION_UNSPECIFIED: _ClassVar[MemberDelta.MemberAction]
        ADD: _ClassVar[MemberDelta.MemberAction]
        REMOVE: _ClassVar[MemberDelta.MemberAction]
    MEMBER_ACTION_UNSPECIFIED: MemberDelta.MemberAction
    ADD: MemberDelta.MemberAction
    REMOVE: MemberDelta.MemberAction
    ACTION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    action: MemberDelta.MemberAction
    subject_id: str
    def __init__(self, action: _Optional[_Union[MemberDelta.MemberAction, str]] = ..., subject_id: _Optional[str] = ...) -> None: ...
