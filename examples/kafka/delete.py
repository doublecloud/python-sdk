from doublecloud.kafka.v1.cluster_service_pb2 import DeleteClusterRequest
from doublecloud.kafka.v1.cluster_service_pb2_grpc import ClusterServiceStub


def delete_cluster(sdk, cluster_id):
    cluster_service = sdk.client(ClusterServiceStub)
    return cluster_service.Delete(DeleteClusterRequest(cluster_id=cluster_id))
