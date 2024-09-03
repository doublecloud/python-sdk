from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Network(_message.Message):
    __slots__ = ("id", "project_id", "cloud_type", "region_id", "create_time", "name", "description", "ipv4_cidr_block", "ipv6_cidr_block", "status", "status_reason", "aws", "gcp", "is_external")
    class NetworkStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NETWORK_STATUS_INVALID: _ClassVar[Network.NetworkStatus]
        NETWORK_STATUS_CREATING: _ClassVar[Network.NetworkStatus]
        NETWORK_STATUS_ACTIVE: _ClassVar[Network.NetworkStatus]
        NETWORK_STATUS_DELETING: _ClassVar[Network.NetworkStatus]
        NETWORK_STATUS_ERROR: _ClassVar[Network.NetworkStatus]
    NETWORK_STATUS_INVALID: Network.NetworkStatus
    NETWORK_STATUS_CREATING: Network.NetworkStatus
    NETWORK_STATUS_ACTIVE: Network.NetworkStatus
    NETWORK_STATUS_DELETING: Network.NetworkStatus
    NETWORK_STATUS_ERROR: Network.NetworkStatus
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TYPE_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IPV4_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    IPV6_CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_REASON_FIELD_NUMBER: _ClassVar[int]
    AWS_FIELD_NUMBER: _ClassVar[int]
    GCP_FIELD_NUMBER: _ClassVar[int]
    IS_EXTERNAL_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    cloud_type: str
    region_id: str
    create_time: _timestamp_pb2.Timestamp
    name: str
    description: str
    ipv4_cidr_block: str
    ipv6_cidr_block: str
    status: Network.NetworkStatus
    status_reason: str
    aws: AwsExternalResources
    gcp: GcpExternalResources
    is_external: bool
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., cloud_type: _Optional[str] = ..., region_id: _Optional[str] = ..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., ipv4_cidr_block: _Optional[str] = ..., ipv6_cidr_block: _Optional[str] = ..., status: _Optional[_Union[Network.NetworkStatus, str]] = ..., status_reason: _Optional[str] = ..., aws: _Optional[_Union[AwsExternalResources, _Mapping]] = ..., gcp: _Optional[_Union[GcpExternalResources, _Mapping]] = ..., is_external: bool = ...) -> None: ...

class AwsExternalResources(_message.Message):
    __slots__ = ("vpc_id", "account_id", "iam_role_arn", "stack_id", "cf_template_version", "private_subnets")
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    IAM_ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    STACK_ID_FIELD_NUMBER: _ClassVar[int]
    CF_TEMPLATE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_SUBNETS_FIELD_NUMBER: _ClassVar[int]
    vpc_id: str
    account_id: _wrappers_pb2.StringValue
    iam_role_arn: _wrappers_pb2.StringValue
    stack_id: _wrappers_pb2.StringValue
    cf_template_version: _wrappers_pb2.StringValue
    private_subnets: _wrappers_pb2.BoolValue
    def __init__(self, vpc_id: _Optional[str] = ..., account_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., iam_role_arn: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., stack_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., cf_template_version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., private_subnets: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class GcpExternalResources(_message.Message):
    __slots__ = ("project_name", "service_account_email", "network_name", "subnetwork_name")
    PROJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    project_name: _wrappers_pb2.StringValue
    service_account_email: _wrappers_pb2.StringValue
    network_name: _wrappers_pb2.StringValue
    subnetwork_name: _wrappers_pb2.StringValue
    def __init__(self, project_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service_account_email: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., network_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., subnetwork_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
