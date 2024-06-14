# This is an example of how to list the clusters you have, and get the output in a pythonic object structure

import doublecloud


sa_key = json.loads(open('authorized_key.json').read())
sdk = doublecloud.SDK(service_account_key=sa_key)

from google.protobuf.wrappers_pb2 import Int64Value

from doublecloud.clickhouse.v1.cluster_pb2 import ClusterResources
from doublecloud.clickhouse.v1.cluster_service_pb2 import CreateClusterRequest, ListClustersRequest
from doublecloud.clickhouse.v1.cluster_service_pb2_grpc import ClusterServiceStub,ClusterService

cluster_service = sdk.client(ClusterServiceStub)

clusters = cluster_service.List(
    ListClustersRequest(
        project_id='<project_id>'
    )
)

import json
from google.protobuf.json_format import MessageToDict

def protobuf_to_native(protobuf_message):
    """
    Serialize a protobuf message to native Python objects.

    Args:
        protobuf_message: The protobuf message to be serialized.

    Returns:
        A native Python representation (nested dictionaries and lists) of the protobuf message.
    """
    try:
        native_data = MessageToDict(protobuf_message, preserving_proto_field_name=True)
        return native_data
    except Exception as e:
        print(f"Error occurred while serializing to native Python objects: {e}")
        return None

native_clusters = protobuf_to_native(clusters)

print(native_clusters)
