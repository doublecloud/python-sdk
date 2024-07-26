from google.protobuf import duration_pb2 as _duration_pb2
from doublecloud.organizationmanager.saml.v1 import federation_pb2 as _federation_pb2
from doublecloud.v1 import operation_pb2 as _operation_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFederationRequest(_message.Message):
    __slots__ = ("federation_id",)
    FEDERATION_ID_FIELD_NUMBER: _ClassVar[int]
    federation_id: str
    def __init__(self, federation_id: _Optional[str] = ...) -> None: ...

class CreateFederationRequest(_message.Message):
    __slots__ = ("organization_id", "name", "description", "cookie_max_age", "auto_create_account_on_login", "issuer", "sso_binding", "sso_url", "security_settings", "case_insensitive_name_ids")
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COOKIE_MAX_AGE_FIELD_NUMBER: _ClassVar[int]
    AUTO_CREATE_ACCOUNT_ON_LOGIN_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    SSO_BINDING_FIELD_NUMBER: _ClassVar[int]
    SSO_URL_FIELD_NUMBER: _ClassVar[int]
    SECURITY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CASE_INSENSITIVE_NAME_IDS_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    name: str
    description: str
    cookie_max_age: _duration_pb2.Duration
    auto_create_account_on_login: bool
    issuer: str
    sso_binding: _federation_pb2.BindingType
    sso_url: str
    security_settings: _federation_pb2.FederationSecuritySettings
    case_insensitive_name_ids: bool
    def __init__(self, organization_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., cookie_max_age: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., auto_create_account_on_login: bool = ..., issuer: _Optional[str] = ..., sso_binding: _Optional[_Union[_federation_pb2.BindingType, str]] = ..., sso_url: _Optional[str] = ..., security_settings: _Optional[_Union[_federation_pb2.FederationSecuritySettings, _Mapping]] = ..., case_insensitive_name_ids: bool = ...) -> None: ...

class UpdateFederationRequest(_message.Message):
    __slots__ = ("federation_id", "name", "description", "cookie_max_age", "auto_create_account_on_login", "issuer", "sso_binding", "sso_url", "security_settings", "case_insensitive_name_ids")
    FEDERATION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COOKIE_MAX_AGE_FIELD_NUMBER: _ClassVar[int]
    AUTO_CREATE_ACCOUNT_ON_LOGIN_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    SSO_BINDING_FIELD_NUMBER: _ClassVar[int]
    SSO_URL_FIELD_NUMBER: _ClassVar[int]
    SECURITY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CASE_INSENSITIVE_NAME_IDS_FIELD_NUMBER: _ClassVar[int]
    federation_id: str
    name: str
    description: str
    cookie_max_age: _duration_pb2.Duration
    auto_create_account_on_login: bool
    issuer: str
    sso_binding: _federation_pb2.BindingType
    sso_url: str
    security_settings: _federation_pb2.FederationSecuritySettings
    case_insensitive_name_ids: bool
    def __init__(self, federation_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., cookie_max_age: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., auto_create_account_on_login: bool = ..., issuer: _Optional[str] = ..., sso_binding: _Optional[_Union[_federation_pb2.BindingType, str]] = ..., sso_url: _Optional[str] = ..., security_settings: _Optional[_Union[_federation_pb2.FederationSecuritySettings, _Mapping]] = ..., case_insensitive_name_ids: bool = ...) -> None: ...

class DeleteFederationRequest(_message.Message):
    __slots__ = ("federation_id",)
    FEDERATION_ID_FIELD_NUMBER: _ClassVar[int]
    federation_id: str
    def __init__(self, federation_id: _Optional[str] = ...) -> None: ...
