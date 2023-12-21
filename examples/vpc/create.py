import logging

from doublecloud.network.v1.network_service_pb2 import CreateNetworkRequest
from doublecloud.network.v1.network_service_pb2_grpc import NetworkServiceStub


def create_network(sdk, project_id: str, cloud_type: str, region_id: str, name: str, ipv4_cidr_block: str):
    network_service = sdk.client(NetworkServiceStub)
    operation = network_service.Create(
        CreateNetworkRequest(
            project_id=project_id,
            cloud_type=cloud_type,
            region_id=region_id,
            name=name,
            ipv4_cidr_block=ipv4_cidr_block,
        )
    )
    logging.info("Creating initiated")
    return operation
