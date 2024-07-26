from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessBindingAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACCESS_BINDING_ACTION_UNSPECIFIED: _ClassVar[AccessBindingAction]
    ADD: _ClassVar[AccessBindingAction]
    REMOVE: _ClassVar[AccessBindingAction]
ACCESS_BINDING_ACTION_UNSPECIFIED: AccessBindingAction
ADD: AccessBindingAction
REMOVE: AccessBindingAction

class Subject(_message.Message):
    __slots__ = ("id", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class AccessBinding(_message.Message):
    __slots__ = ("role_id", "subject")
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    subject: Subject
    def __init__(self, role_id: _Optional[str] = ..., subject: _Optional[_Union[Subject, _Mapping]] = ...) -> None: ...

class ListAccessBindingsRequest(_message.Message):
    __slots__ = ("resource_id", "page_size", "page_token")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    page_size: int
    page_token: str
    def __init__(self, resource_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListAccessBindingsResponse(_message.Message):
    __slots__ = ("access_bindings", "next_page_token")
    ACCESS_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_bindings: _containers.RepeatedCompositeFieldContainer[AccessBinding]
    next_page_token: str
    def __init__(self, access_bindings: _Optional[_Iterable[_Union[AccessBinding, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class SetAccessBindingsRequest(_message.Message):
    __slots__ = ("resource_id", "access_bindings")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    access_bindings: _containers.RepeatedCompositeFieldContainer[AccessBinding]
    def __init__(self, resource_id: _Optional[str] = ..., access_bindings: _Optional[_Iterable[_Union[AccessBinding, _Mapping]]] = ...) -> None: ...

class SetAccessBindingsMetadata(_message.Message):
    __slots__ = ("resource_id",)
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    def __init__(self, resource_id: _Optional[str] = ...) -> None: ...

class UpdateAccessBindingsRequest(_message.Message):
    __slots__ = ("resource_id", "access_binding_deltas")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_BINDING_DELTAS_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    access_binding_deltas: _containers.RepeatedCompositeFieldContainer[AccessBindingDelta]
    def __init__(self, resource_id: _Optional[str] = ..., access_binding_deltas: _Optional[_Iterable[_Union[AccessBindingDelta, _Mapping]]] = ...) -> None: ...

class UpdateAccessBindingsMetadata(_message.Message):
    __slots__ = ("resource_id",)
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    def __init__(self, resource_id: _Optional[str] = ...) -> None: ...

class AccessBindingDelta(_message.Message):
    __slots__ = ("action", "access_binding")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ACCESS_BINDING_FIELD_NUMBER: _ClassVar[int]
    action: AccessBindingAction
    access_binding: AccessBinding
    def __init__(self, action: _Optional[_Union[AccessBindingAction, str]] = ..., access_binding: _Optional[_Union[AccessBinding, _Mapping]] = ...) -> None: ...

class AccessBindingsOperationResult(_message.Message):
    __slots__ = ("effective_deltas",)
    EFFECTIVE_DELTAS_FIELD_NUMBER: _ClassVar[int]
    effective_deltas: _containers.RepeatedCompositeFieldContainer[AccessBindingDelta]
    def __init__(self, effective_deltas: _Optional[_Iterable[_Union[AccessBindingDelta, _Mapping]]] = ...) -> None: ...
