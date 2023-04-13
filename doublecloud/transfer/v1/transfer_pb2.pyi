from doublecloud.transfer.v1 import endpoint_pb2 as _endpoint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransferType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TRANSFER_TYPE_UNSPECIFIED: _ClassVar[TransferType]
    SNAPSHOT_AND_INCREMENT: _ClassVar[TransferType]
    SNAPSHOT_ONLY: _ClassVar[TransferType]
    INCREMENT_ONLY: _ClassVar[TransferType]

class TransferStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TRANSFER_STATUS_UNSPECIFIED: _ClassVar[TransferStatus]
    CREATING: _ClassVar[TransferStatus]
    CREATED: _ClassVar[TransferStatus]
    RUNNING: _ClassVar[TransferStatus]
    STOPPING: _ClassVar[TransferStatus]
    STOPPED: _ClassVar[TransferStatus]
    ERROR: _ClassVar[TransferStatus]
    SNAPSHOTTING: _ClassVar[TransferStatus]
    DONE: _ClassVar[TransferStatus]
TRANSFER_TYPE_UNSPECIFIED: TransferType
SNAPSHOT_AND_INCREMENT: TransferType
SNAPSHOT_ONLY: TransferType
INCREMENT_ONLY: TransferType
TRANSFER_STATUS_UNSPECIFIED: TransferStatus
CREATING: TransferStatus
CREATED: TransferStatus
RUNNING: TransferStatus
STOPPING: TransferStatus
STOPPED: TransferStatus
ERROR: TransferStatus
SNAPSHOTTING: TransferStatus
DONE: TransferStatus

class Transfer(_message.Message):
    __slots__ = ["id", "project_id", "name", "description", "labels", "source", "target", "status", "type", "warning"]
    class LabelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    name: str
    description: str
    labels: _containers.ScalarMap[str, str]
    source: _endpoint_pb2.Endpoint
    target: _endpoint_pb2.Endpoint
    status: TransferStatus
    type: TransferType
    warning: str
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., source: _Optional[_Union[_endpoint_pb2.Endpoint, _Mapping]] = ..., target: _Optional[_Union[_endpoint_pb2.Endpoint, _Mapping]] = ..., status: _Optional[_Union[TransferStatus, str]] = ..., type: _Optional[_Union[TransferType, str]] = ..., warning: _Optional[str] = ...) -> None: ...
