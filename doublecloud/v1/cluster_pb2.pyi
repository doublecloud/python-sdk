from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClusterStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_STATUS_INVALID: _ClassVar[ClusterStatus]
    CLUSTER_STATUS_ALIVE: _ClassVar[ClusterStatus]
    CLUSTER_STATUS_DEGRADED: _ClassVar[ClusterStatus]
    CLUSTER_STATUS_DEAD: _ClassVar[ClusterStatus]
    CLUSTER_STATUS_UNKNOWN: _ClassVar[ClusterStatus]
    CLUSTER_STATUS_CREATING: _ClassVar[ClusterStatus]
    CLUSTER_STATUS_UPDATING: _ClassVar[ClusterStatus]
    CLUSTER_STATUS_STOPPING: _ClassVar[ClusterStatus]
    CLUSTER_STATUS_STOPPED: _ClassVar[ClusterStatus]
    CLUSTER_STATUS_STARTING: _ClassVar[ClusterStatus]
    CLUSTER_STATUS_ERROR: _ClassVar[ClusterStatus]

class HostStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HOST_STATUS_INVALID: _ClassVar[HostStatus]
    HOST_STATUS_ALIVE: _ClassVar[HostStatus]
    HOST_STATUS_DEAD: _ClassVar[HostStatus]
    HOST_STATUS_DEGRADED: _ClassVar[HostStatus]
    HOST_STATUS_CREATING: _ClassVar[HostStatus]
    HOST_STATUS_STOPPING: _ClassVar[HostStatus]
    HOST_STATUS_STOPPED: _ClassVar[HostStatus]
    HOST_STATUS_STARTING: _ClassVar[HostStatus]
CLUSTER_STATUS_INVALID: ClusterStatus
CLUSTER_STATUS_ALIVE: ClusterStatus
CLUSTER_STATUS_DEGRADED: ClusterStatus
CLUSTER_STATUS_DEAD: ClusterStatus
CLUSTER_STATUS_UNKNOWN: ClusterStatus
CLUSTER_STATUS_CREATING: ClusterStatus
CLUSTER_STATUS_UPDATING: ClusterStatus
CLUSTER_STATUS_STOPPING: ClusterStatus
CLUSTER_STATUS_STOPPED: ClusterStatus
CLUSTER_STATUS_STARTING: ClusterStatus
CLUSTER_STATUS_ERROR: ClusterStatus
HOST_STATUS_INVALID: HostStatus
HOST_STATUS_ALIVE: HostStatus
HOST_STATUS_DEAD: HostStatus
HOST_STATUS_DEGRADED: HostStatus
HOST_STATUS_CREATING: HostStatus
HOST_STATUS_STOPPING: HostStatus
HOST_STATUS_STOPPED: HostStatus
HOST_STATUS_STARTING: HostStatus

class Access(_message.Message):
    __slots__ = ("ipv4_cidr_blocks", "ipv6_cidr_blocks", "data_services")
    class DataService(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_SERVICE_INVALID: _ClassVar[Access.DataService]
        DATA_SERVICE_VISUALIZATION: _ClassVar[Access.DataService]
        DATA_SERVICE_TRANSFER: _ClassVar[Access.DataService]
    DATA_SERVICE_INVALID: Access.DataService
    DATA_SERVICE_VISUALIZATION: Access.DataService
    DATA_SERVICE_TRANSFER: Access.DataService
    class CidrBlock(_message.Message):
        __slots__ = ("value", "description")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        value: str
        description: str
        def __init__(self, value: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    class CidrBlockList(_message.Message):
        __slots__ = ("values",)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedCompositeFieldContainer[Access.CidrBlock]
        def __init__(self, values: _Optional[_Iterable[_Union[Access.CidrBlock, _Mapping]]] = ...) -> None: ...
    class DataServiceList(_message.Message):
        __slots__ = ("values",)
        VALUES_FIELD_NUMBER: _ClassVar[int]
        values: _containers.RepeatedScalarFieldContainer[Access.DataService]
        def __init__(self, values: _Optional[_Iterable[_Union[Access.DataService, str]]] = ...) -> None: ...
    IPV4_CIDR_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    IPV6_CIDR_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    DATA_SERVICES_FIELD_NUMBER: _ClassVar[int]
    ipv4_cidr_blocks: Access.CidrBlockList
    ipv6_cidr_blocks: Access.CidrBlockList
    data_services: Access.DataServiceList
    def __init__(self, ipv4_cidr_blocks: _Optional[_Union[Access.CidrBlockList, _Mapping]] = ..., ipv6_cidr_blocks: _Optional[_Union[Access.CidrBlockList, _Mapping]] = ..., data_services: _Optional[_Union[Access.DataServiceList, _Mapping]] = ...) -> None: ...

class DataEncryption(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: _wrappers_pb2.BoolValue
    def __init__(self, enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
