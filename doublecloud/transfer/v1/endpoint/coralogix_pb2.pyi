from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CoralogixSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CORALOGIX_SEVERITY_UNSPECIFIED: _ClassVar[CoralogixSeverity]
    CORALOGIX_SEVERITY_DEBUG: _ClassVar[CoralogixSeverity]
    CORALOGIX_SEVERITY_VERBOSE: _ClassVar[CoralogixSeverity]
    CORALOGIX_SEVERITY_INFO: _ClassVar[CoralogixSeverity]
    CORALOGIX_SEVERITY_WARN: _ClassVar[CoralogixSeverity]
    CORALOGIX_SEVERITY_ERROR: _ClassVar[CoralogixSeverity]
    CORALOGIX_SEVERITY_CRITICAL: _ClassVar[CoralogixSeverity]
CORALOGIX_SEVERITY_UNSPECIFIED: CoralogixSeverity
CORALOGIX_SEVERITY_DEBUG: CoralogixSeverity
CORALOGIX_SEVERITY_VERBOSE: CoralogixSeverity
CORALOGIX_SEVERITY_INFO: CoralogixSeverity
CORALOGIX_SEVERITY_WARN: CoralogixSeverity
CORALOGIX_SEVERITY_ERROR: CoralogixSeverity
CORALOGIX_SEVERITY_CRITICAL: CoralogixSeverity

class CoralogixTarget(_message.Message):
    __slots__ = ("token", "domain", "application_name", "column_mapping")
    class SeverityMap(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: CoralogixSeverity
        def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[CoralogixSeverity, str]] = ...) -> None: ...
    class ColumnMapping(_message.Message):
        __slots__ = ("timestamp", "severity", "message_template", "class_name", "method_name", "thread_id", "category", "subsystem", "host", "known_severities")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        SEVERITY_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        CLASS_NAME_FIELD_NUMBER: _ClassVar[int]
        METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
        THREAD_ID_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        SUBSYSTEM_FIELD_NUMBER: _ClassVar[int]
        HOST_FIELD_NUMBER: _ClassVar[int]
        KNOWN_SEVERITIES_FIELD_NUMBER: _ClassVar[int]
        timestamp: str
        severity: str
        message_template: str
        class_name: str
        method_name: str
        thread_id: str
        category: str
        subsystem: str
        host: str
        known_severities: _containers.RepeatedCompositeFieldContainer[CoralogixTarget.SeverityMap]
        def __init__(self, timestamp: _Optional[str] = ..., severity: _Optional[str] = ..., message_template: _Optional[str] = ..., class_name: _Optional[str] = ..., method_name: _Optional[str] = ..., thread_id: _Optional[str] = ..., category: _Optional[str] = ..., subsystem: _Optional[str] = ..., host: _Optional[str] = ..., known_severities: _Optional[_Iterable[_Union[CoralogixTarget.SeverityMap, _Mapping]]] = ...) -> None: ...
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    COLUMN_MAPPING_FIELD_NUMBER: _ClassVar[int]
    token: str
    domain: str
    application_name: str
    column_mapping: CoralogixTarget.ColumnMapping
    def __init__(self, token: _Optional[str] = ..., domain: _Optional[str] = ..., application_name: _Optional[str] = ..., column_mapping: _Optional[_Union[CoralogixTarget.ColumnMapping, _Mapping]] = ...) -> None: ...
