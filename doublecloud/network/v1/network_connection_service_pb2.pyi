from doublecloud.network.v1 import network_connection_pb2 as _network_connection_pb2
from doublecloud.v1 import operation_pb2 as _operation_pb2
from doublecloud.v1 import paging_pb2 as _paging_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetNetworkConnectionRequest(_message.Message):
    __slots__ = ("network_connection_id",)
    NETWORK_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    network_connection_id: str
    def __init__(self, network_connection_id: _Optional[str] = ...) -> None: ...

class ListNetworkConnectionsRequest(_message.Message):
    __slots__ = ("project_id", "paging")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    paging: _paging_pb2.Paging
    def __init__(self, project_id: _Optional[str] = ..., paging: _Optional[_Union[_paging_pb2.Paging, _Mapping]] = ...) -> None: ...

class ListNetworkConnectionsResponse(_message.Message):
    __slots__ = ("network_connections", "next_page")
    NETWORK_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    network_connections: _containers.RepeatedCompositeFieldContainer[_network_connection_pb2.NetworkConnection]
    next_page: _paging_pb2.NextPage
    def __init__(self, network_connections: _Optional[_Iterable[_Union[_network_connection_pb2.NetworkConnection, _Mapping]]] = ..., next_page: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ...) -> None: ...

class CreateNetworkConnectionRequest(_message.Message):
    __slots__ = ("network_id", "aws", "google", "description")
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    network_id: str
    aws: CreateAWSNetworkConnectionRequest
    google: CreateGoogleNetworkConnectionRequest
    description: str
    def __init__(self, network_id: _Optional[str] = ..., aws: _Optional[_Union[CreateAWSNetworkConnectionRequest, _Mapping]] = ..., google: _Optional[_Union[CreateGoogleNetworkConnectionRequest, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class CreateAWSNetworkConnectionRequest(_message.Message):
    __slots__ = ("peering",)
    PEERING_FIELD_NUMBER: _ClassVar[int]
    peering: CreateAWSNetworkConnectionPeeringRequest
    def __init__(self, peering: _Optional[_Union[CreateAWSNetworkConnectionPeeringRequest, _Mapping]] = ...) -> None: ...

class CreateAWSNetworkConnectionPeeringRequest(_message.Message):
    __slots__ = ("vpc_id", "account_id", "region_id", "ipv4_cidr_block", "ipv6_cidr_block")
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    IPV6_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    vpc_id: str
    account_id: str
    region_id: str
    ipv4_cidr_block: str
    ipv6_cidr_block: str
    def __init__(self, vpc_id: _Optional[str] = ..., account_id: _Optional[str] = ..., region_id: _Optional[str] = ..., ipv4_cidr_block: _Optional[str] = ..., ipv6_cidr_block: _Optional[str] = ...) -> None: ...

class CreateGoogleNetworkConnectionRequest(_message.Message):
    __slots__ = ("name", "peer_network_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PEER_NETWORK_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    peer_network_url: str
    def __init__(self, name: _Optional[str] = ..., peer_network_url: _Optional[str] = ...) -> None: ...

class DeleteNetworkConnectionRequest(_message.Message):
    __slots__ = ("network_connection_id",)
    NETWORK_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    network_connection_id: str
    def __init__(self, network_connection_id: _Optional[str] = ...) -> None: ...

class UpdateNetworkConnectionRequest(_message.Message):
    __slots__ = ("network_connection_id", "description")
    NETWORK_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    network_connection_id: str
    description: str
    def __init__(self, network_connection_id: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
