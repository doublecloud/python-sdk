from google.protobuf import timestamp_pb2 as _timestamp_pb2
from doublecloud.logs.v1 import log_source_pb2 as _log_source_pb2
from doublecloud.v1 import paging_pb2 as _paging_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LogExportStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG_EXPORT_STATUS_UNSPECIFIED: _ClassVar[LogExportStatus]
    LOG_EXPORT_STATUS_PENDING: _ClassVar[LogExportStatus]
    LOG_EXPORT_STATUS_RUNNING: _ClassVar[LogExportStatus]
    LOG_EXPORT_STATUS_STOPPED: _ClassVar[LogExportStatus]
    LOG_EXPORT_STATUS_FAILED: _ClassVar[LogExportStatus]
LOG_EXPORT_STATUS_UNSPECIFIED: LogExportStatus
LOG_EXPORT_STATUS_PENDING: LogExportStatus
LOG_EXPORT_STATUS_RUNNING: LogExportStatus
LOG_EXPORT_STATUS_STOPPED: LogExportStatus
LOG_EXPORT_STATUS_FAILED: LogExportStatus

class LogsExport(_message.Message):
    __slots__ = ("id", "project_id", "name", "description", "sources", "target", "status", "status_reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    name: str
    description: str
    sources: _containers.RepeatedCompositeFieldContainer[_log_source_pb2.LogSource]
    target: LogsTarget
    status: LogExportStatus
    status_reason: str
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., sources: _Optional[_Iterable[_Union[_log_source_pb2.LogSource, _Mapping]]] = ..., target: _Optional[_Union[LogsTarget, _Mapping]] = ..., status: _Optional[_Union[LogExportStatus, str]] = ..., status_reason: _Optional[str] = ...) -> None: ...

class LogsTargetS3(_message.Message):
    __slots__ = ("bucket", "bucket_layout", "aws_access_key_id", "aws_secret_access_key", "region", "endpoint", "disable_ssl", "skip_verify_ssl_cert")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    BUCKET_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    AWS_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    DISABLE_SSL_FIELD_NUMBER: _ClassVar[int]
    SKIP_VERIFY_SSL_CERT_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    bucket_layout: str
    aws_access_key_id: str
    aws_secret_access_key: str
    region: str
    endpoint: str
    disable_ssl: bool
    skip_verify_ssl_cert: bool
    def __init__(self, bucket: _Optional[str] = ..., bucket_layout: _Optional[str] = ..., aws_access_key_id: _Optional[str] = ..., aws_secret_access_key: _Optional[str] = ..., region: _Optional[str] = ..., endpoint: _Optional[str] = ..., disable_ssl: bool = ..., skip_verify_ssl_cert: bool = ...) -> None: ...

class LogsTargetDatadog(_message.Message):
    __slots__ = ("api_key", "datadog_host")
    class DatadogHost(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATADOG_HOST_UNSPECIFIED: _ClassVar[LogsTargetDatadog.DatadogHost]
        DATADOG_HOST_DATADOGHQ: _ClassVar[LogsTargetDatadog.DatadogHost]
        DATADOG_HOST_US3_DATADOGHQ: _ClassVar[LogsTargetDatadog.DatadogHost]
        DATADOG_HOST_US5_DATADOGHQ_COM: _ClassVar[LogsTargetDatadog.DatadogHost]
        DATADOG_HOST_AP1_DATADOGHQ_COM: _ClassVar[LogsTargetDatadog.DatadogHost]
        DATADOG_HOST_DATADOGHQ_EU: _ClassVar[LogsTargetDatadog.DatadogHost]
        DATADOG_HOST_DDOGGOV_COM: _ClassVar[LogsTargetDatadog.DatadogHost]
    DATADOG_HOST_UNSPECIFIED: LogsTargetDatadog.DatadogHost
    DATADOG_HOST_DATADOGHQ: LogsTargetDatadog.DatadogHost
    DATADOG_HOST_US3_DATADOGHQ: LogsTargetDatadog.DatadogHost
    DATADOG_HOST_US5_DATADOGHQ_COM: LogsTargetDatadog.DatadogHost
    DATADOG_HOST_AP1_DATADOGHQ_COM: LogsTargetDatadog.DatadogHost
    DATADOG_HOST_DATADOGHQ_EU: LogsTargetDatadog.DatadogHost
    DATADOG_HOST_DDOGGOV_COM: LogsTargetDatadog.DatadogHost
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    DATADOG_HOST_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    datadog_host: LogsTargetDatadog.DatadogHost
    def __init__(self, api_key: _Optional[str] = ..., datadog_host: _Optional[_Union[LogsTargetDatadog.DatadogHost, str]] = ...) -> None: ...

class LogsTargetCoralogix(_message.Message):
    __slots__ = ("domain", "token")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    domain: str
    token: str
    def __init__(self, domain: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class LogsTargetDatadogCompatible(_message.Message):
    __slots__ = ("api_key", "datadog_host")
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    DATADOG_HOST_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    datadog_host: str
    def __init__(self, api_key: _Optional[str] = ..., datadog_host: _Optional[str] = ...) -> None: ...

class LogsTarget(_message.Message):
    __slots__ = ("s3", "datadog", "coralogix", "datadog_compatible")
    S3_FIELD_NUMBER: _ClassVar[int]
    DATADOG_FIELD_NUMBER: _ClassVar[int]
    CORALOGIX_FIELD_NUMBER: _ClassVar[int]
    DATADOG_COMPATIBLE_FIELD_NUMBER: _ClassVar[int]
    s3: LogsTargetS3
    datadog: LogsTargetDatadog
    coralogix: LogsTargetCoralogix
    datadog_compatible: LogsTargetDatadogCompatible
    def __init__(self, s3: _Optional[_Union[LogsTargetS3, _Mapping]] = ..., datadog: _Optional[_Union[LogsTargetDatadog, _Mapping]] = ..., coralogix: _Optional[_Union[LogsTargetCoralogix, _Mapping]] = ..., datadog_compatible: _Optional[_Union[LogsTargetDatadogCompatible, _Mapping]] = ...) -> None: ...
