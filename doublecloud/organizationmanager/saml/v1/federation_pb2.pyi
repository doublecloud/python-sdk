from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BindingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BINDING_TYPE_UNSPECIFIED: _ClassVar[BindingType]
    POST: _ClassVar[BindingType]
    REDIRECT: _ClassVar[BindingType]
    ARTIFACT: _ClassVar[BindingType]
BINDING_TYPE_UNSPECIFIED: BindingType
POST: BindingType
REDIRECT: BindingType
ARTIFACT: BindingType

class Federation(_message.Message):
    __slots__ = ("id", "organization_id", "name", "description", "created_at", "cookie_max_age", "auto_create_account_on_login", "issuer", "sso_binding", "sso_url", "security_settings", "case_insensitive_name_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    COOKIE_MAX_AGE_FIELD_NUMBER: _ClassVar[int]
    AUTO_CREATE_ACCOUNT_ON_LOGIN_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    SSO_BINDING_FIELD_NUMBER: _ClassVar[int]
    SSO_URL_FIELD_NUMBER: _ClassVar[int]
    SECURITY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CASE_INSENSITIVE_NAME_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    organization_id: str
    name: str
    description: str
    created_at: _timestamp_pb2.Timestamp
    cookie_max_age: _duration_pb2.Duration
    auto_create_account_on_login: bool
    issuer: str
    sso_binding: BindingType
    sso_url: str
    security_settings: FederationSecuritySettings
    case_insensitive_name_ids: bool
    def __init__(self, id: _Optional[str] = ..., organization_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cookie_max_age: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., auto_create_account_on_login: bool = ..., issuer: _Optional[str] = ..., sso_binding: _Optional[_Union[BindingType, str]] = ..., sso_url: _Optional[str] = ..., security_settings: _Optional[_Union[FederationSecuritySettings, _Mapping]] = ..., case_insensitive_name_ids: bool = ...) -> None: ...

class FederationSecuritySettings(_message.Message):
    __slots__ = ("encrypted_assertions",)
    ENCRYPTED_ASSERTIONS_FIELD_NUMBER: _ClassVar[int]
    encrypted_assertions: bool
    def __init__(self, encrypted_assertions: bool = ...) -> None: ...
