from doublecloud.network.v1.network_service_pb2 import DeleteNetworkRequest
from doublecloud.network.v1.network_service_pb2_grpc import NetworkServiceStub


def delete_network(sdk, network_id: str):
    network_service = sdk.client(NetworkServiceStub)
    return network_service.Delete(DeleteNetworkRequest(network_id=network_id))
