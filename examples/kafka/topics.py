from google.protobuf.wrappers_pb2 import Int64Value

from doublecloud.kafka.v1.topic_pb2 import TopicConfig3, TopicSpec
from doublecloud.kafka.v1.topic_service_pb2 import (
    CreateTopicRequest,
    DeleteTopicRequest,
)
from doublecloud.kafka.v1.topic_service_pb2_grpc import TopicServiceStub


def create_topic(sdk, cluster_id, **kwargs):
    topic_service = sdk.client(TopicServiceStub)
    sdk.wait_operation_and_get_result(
        topic_service.Create(
            CreateTopicRequest(
                cluster_id=cluster_id,
                topic_spec=TopicSpec(
                    name=kwargs.get("name", "topic-name"),
                    partitions=Int64Value(value=kwargs.get("partitions", 1)),
                    replication_factor=Int64Value(value=kwargs.get("replication_factor", 1)),
                    topic_config_3=TopicConfig3(compression_type=TopicConfig3.COMPRESSION_TYPE_ZSTD),
                ),
            )
        )
    )


def delete_topic(sdk, cluster_id, topic_name):
    topic_service = sdk.client(TopicServiceStub)
    sdk.wait_operation_and_get_result(
        topic_service.Delete(DeleteTopicRequest(cluster_id=cluster_id, topic_name=topic_name)),
    )
