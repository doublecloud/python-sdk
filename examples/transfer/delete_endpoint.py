from doublecloud.transfer.v1.endpoint_service_pb2 import DeleteEndpointRequest


def delete_endpoint(svc, endpoint_id: str):
    return svc.Delete(DeleteEndpointRequest(endpoint_id=endpoint_id))
