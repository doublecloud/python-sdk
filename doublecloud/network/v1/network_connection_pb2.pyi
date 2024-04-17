from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkConnection(_message.Message):
    __slots__ = ("id", "network_id", "aws", "google", "create_time", "description", "status", "status_reason")
    class NetworkConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NETWORK_CONNECTION_STATUS_INVALID: _ClassVar[NetworkConnection.NetworkConnectionStatus]
        NETWORK_CONNECTION_STATUS_CREATING: _ClassVar[NetworkConnection.NetworkConnectionStatus]
        NETWORK_CONNECTION_STATUS_PENDING: _ClassVar[NetworkConnection.NetworkConnectionStatus]
        NETWORK_CONNECTION_STATUS_ACTIVE: _ClassVar[NetworkConnection.NetworkConnectionStatus]
        NETWORK_CONNECTION_STATUS_DELETING: _ClassVar[NetworkConnection.NetworkConnectionStatus]
        NETWORK_CONNECTION_STATUS_ERROR: _ClassVar[NetworkConnection.NetworkConnectionStatus]
    NETWORK_CONNECTION_STATUS_INVALID: NetworkConnection.NetworkConnectionStatus
    NETWORK_CONNECTION_STATUS_CREATING: NetworkConnection.NetworkConnectionStatus
    NETWORK_CONNECTION_STATUS_PENDING: NetworkConnection.NetworkConnectionStatus
    NETWORK_CONNECTION_STATUS_ACTIVE: NetworkConnection.NetworkConnectionStatus
    NETWORK_CONNECTION_STATUS_DELETING: NetworkConnection.NetworkConnectionStatus
    NETWORK_CONNECTION_STATUS_ERROR: NetworkConnection.NetworkConnectionStatus
    ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    network_id: str
    aws: AWSNetworkConnectionInfo
    google: GoogleNetworkConnectionInfo
    create_time: _timestamp_pb2.Timestamp
    description: str
    status: NetworkConnection.NetworkConnectionStatus
    status_reason: str
    def __init__(self, id: _Optional[str] = ..., network_id: _Optional[str] = ..., aws: _Optional[_Union[AWSNetworkConnectionInfo, _Mapping]] = ..., google: _Optional[_Union[GoogleNetworkConnectionInfo, _Mapping]] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., status: _Optional[_Union[NetworkConnection.NetworkConnectionStatus, str]] = ..., status_reason: _Optional[str] = ...) -> None: ...

class AWSNetworkConnectionInfo(_message.Message):
    __slots__ = ("peering",)
    PEERING_FIELD_NUMBER: _ClassVar[int]
    peering: AWSNetworkConnectionPeeringInfo
    def __init__(self, peering: _Optional[_Union[AWSNetworkConnectionPeeringInfo, _Mapping]] = ...) -> None: ...

class AWSNetworkConnectionPeeringInfo(_message.Message):
    __slots__ = ("vpc_id", "account_id", "region_id", "ipv4_cidr_block", "ipv6_cidr_block", "peering_connection_id", "managed_ipv4_cidr_block", "managed_ipv6_cidr_block")
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    IPV6_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    PEERING_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    MANAGED_IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    MANAGED_IPV6_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    vpc_id: str
    account_id: str
    region_id: str
    ipv4_cidr_block: str
    ipv6_cidr_block: str
    peering_connection_id: str
    managed_ipv4_cidr_block: str
    managed_ipv6_cidr_block: str
    def __init__(self, vpc_id: _Optional[str] = ..., account_id: _Optional[str] = ..., region_id: _Optional[str] = ..., ipv4_cidr_block: _Optional[str] = ..., ipv6_cidr_block: _Optional[str] = ..., peering_connection_id: _Optional[str] = ..., managed_ipv4_cidr_block: _Optional[str] = ..., managed_ipv6_cidr_block: _Optional[str] = ...) -> None: ...

class GoogleNetworkConnectionInfo(_message.Message):
    __slots__ = ("name", "peer_network_url", "managed_network_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PEER_NETWORK_URL_FIELD_NUMBER: _ClassVar[int]
    MANAGED_NETWORK_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    peer_network_url: str
    managed_network_url: str
    def __init__(self, name: _Optional[str] = ..., peer_network_url: _Optional[str] = ..., managed_network_url: _Optional[str] = ...) -> None: ...
