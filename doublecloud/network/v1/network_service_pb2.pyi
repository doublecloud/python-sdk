from doublecloud.network.v1 import network_pb2 as _network_pb2
from doublecloud.v1 import operation_pb2 as _operation_pb2
from doublecloud.v1 import paging_pb2 as _paging_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetNetworkRequest(_message.Message):
    __slots__ = ("network_id",)
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    network_id: str
    def __init__(self, network_id: _Optional[str] = ...) -> None: ...

class ListNetworksRequest(_message.Message):
    __slots__ = ("project_id", "paging", "filter")
    class Filter(_message.Message):
        __slots__ = ("cloud_type", "region_id", "status", "is_external")
        CLOUD_TYPE_FIELD_NUMBER: _ClassVar[int]
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        IS_EXTERNAL_FIELD_NUMBER: _ClassVar[int]
        cloud_type: _wrappers_pb2.StringValue
        region_id: _wrappers_pb2.StringValue
        status: _network_pb2.Network.NetworkStatus
        is_external: _wrappers_pb2.BoolValue
        def __init__(self, cloud_type: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., region_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., status: _Optional[_Union[_network_pb2.Network.NetworkStatus, str]] = ..., is_external: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    paging: _paging_pb2.Paging
    filter: ListNetworksRequest.Filter
    def __init__(self, project_id: _Optional[str] = ..., paging: _Optional[_Union[_paging_pb2.Paging, _Mapping]] = ..., filter: _Optional[_Union[ListNetworksRequest.Filter, _Mapping]] = ...) -> None: ...

class ListNetworksResponse(_message.Message):
    __slots__ = ("networks", "next_page")
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    networks: _containers.RepeatedCompositeFieldContainer[_network_pb2.Network]
    next_page: _paging_pb2.NextPage
    def __init__(self, networks: _Optional[_Iterable[_Union[_network_pb2.Network, _Mapping]]] = ..., next_page: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ...) -> None: ...

class CreateNetworkRequest(_message.Message):
    __slots__ = ("project_id", "cloud_type", "region_id", "name", "description", "ipv4_cidr_block")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TYPE_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    cloud_type: str
    region_id: str
    name: str
    description: str
    ipv4_cidr_block: str
    def __init__(self, project_id: _Optional[str] = ..., cloud_type: _Optional[str] = ..., region_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., ipv4_cidr_block: _Optional[str] = ...) -> None: ...

class DeleteNetworkRequest(_message.Message):
    __slots__ = ("network_id",)
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    network_id: str
    def __init__(self, network_id: _Optional[str] = ...) -> None: ...

class ImportNetworkRequest(_message.Message):
    __slots__ = ("project_id", "name", "description", "aws", "google")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AWS_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    name: str
    description: str
    aws: ImportAWSVPCRequest
    google: ImportGoogleVPCRequest
    def __init__(self, project_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., aws: _Optional[_Union[ImportAWSVPCRequest, _Mapping]] = ..., google: _Optional[_Union[ImportGoogleVPCRequest, _Mapping]] = ...) -> None: ...

class ImportAWSVPCRequest(_message.Message):
    __slots__ = ("vpc_id", "region_id", "account_id", "iam_role_arn", "stack_id", "version", "private_subnets")
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    IAM_ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    STACK_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_SUBNETS_FIELD_NUMBER: _ClassVar[int]
    vpc_id: str
    region_id: str
    account_id: str
    iam_role_arn: str
    stack_id: str
    version: str
    private_subnets: bool
    def __init__(self, vpc_id: _Optional[str] = ..., region_id: _Optional[str] = ..., account_id: _Optional[str] = ..., iam_role_arn: _Optional[str] = ..., stack_id: _Optional[str] = ..., version: _Optional[str] = ..., private_subnets: bool = ...) -> None: ...

class ImportGoogleVPCRequest(_message.Message):
    __slots__ = ("service_account_email", "project_name", "network_name", "region_id", "subnetwork_name")
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    service_account_email: str
    project_name: str
    network_name: str
    region_id: str
    subnetwork_name: str
    def __init__(self, service_account_email: _Optional[str] = ..., project_name: _Optional[str] = ..., network_name: _Optional[str] = ..., region_id: _Optional[str] = ..., subnetwork_name: _Optional[str] = ...) -> None: ...
