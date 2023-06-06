import logging

from google.protobuf.wrappers_pb2 import Int64Value

from doublecloud.clickhouse.v1.cluster_pb2 import ClusterResources
from doublecloud.clickhouse.v1.cluster_service_pb2 import CreateClusterRequest
from doublecloud.clickhouse.v1.cluster_service_pb2_grpc import ClusterServiceStub


def create_cluster(sdk, project_id, region_id, name, network_id):
    cluster_service = sdk.client(ClusterServiceStub)
    operation = cluster_service.Create(
        CreateClusterRequest(
            project_id=project_id,
            cloud_type="aws",
            region_id=region_id,
            name=name,
            resources=ClusterResources(
                clickhouse=ClusterResources.Clickhouse(
                    resource_preset_id="s1-c2-m4",
                    disk_size=Int64Value(value=32 * 2**30),
                    replica_count=Int64Value(value=1),
                )
            ),
            network_id=network_id,
        )
    )
    logging.info("Creating initiated")
    return operation
