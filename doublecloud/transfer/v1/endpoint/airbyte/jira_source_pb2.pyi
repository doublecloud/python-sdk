from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JiraSource(_message.Message):
    __slots__ = ("api_token", "domain", "email", "projects", "start_date", "issues_stream_expand_with", "enable_experimental_streams")
    class Expand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXPAND_UNSPECIFIED: _ClassVar[JiraSource.Expand]
        RENDERED_FIELDS: _ClassVar[JiraSource.Expand]
        TRANSITIONS: _ClassVar[JiraSource.Expand]
        CHANGELOG: _ClassVar[JiraSource.Expand]
    EXPAND_UNSPECIFIED: JiraSource.Expand
    RENDERED_FIELDS: JiraSource.Expand
    TRANSITIONS: JiraSource.Expand
    CHANGELOG: JiraSource.Expand
    API_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    ISSUES_STREAM_EXPAND_WITH_FIELD_NUMBER: _ClassVar[int]
    ENABLE_EXPERIMENTAL_STREAMS_FIELD_NUMBER: _ClassVar[int]
    api_token: str
    domain: str
    email: str
    projects: _containers.RepeatedScalarFieldContainer[str]
    start_date: str
    issues_stream_expand_with: _containers.RepeatedScalarFieldContainer[JiraSource.Expand]
    enable_experimental_streams: bool
    def __init__(self, api_token: _Optional[str] = ..., domain: _Optional[str] = ..., email: _Optional[str] = ..., projects: _Optional[_Iterable[str]] = ..., start_date: _Optional[str] = ..., issues_stream_expand_with: _Optional[_Iterable[_Union[JiraSource.Expand, str]]] = ..., enable_experimental_streams: bool = ...) -> None: ...
