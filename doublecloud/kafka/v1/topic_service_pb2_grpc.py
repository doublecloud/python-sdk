# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from doublecloud.kafka.v1 import topic_pb2 as doublecloud_dot_kafka_dot_v1_dot_topic__pb2
from doublecloud.kafka.v1 import topic_service_pb2 as doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2
from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2


class TopicServiceStub(object):
    """A set of methods for managing Apache Kafka Topic resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/doublecloud.kafka.v1.TopicService/Get',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.GetTopicRequest.SerializeToString,
                response_deserializer=doublecloud_dot_kafka_dot_v1_dot_topic__pb2.Topic.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/doublecloud.kafka.v1.TopicService/List',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.ListTopicsRequest.SerializeToString,
                response_deserializer=doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.ListTopicsResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/doublecloud.kafka.v1.TopicService/Create',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.CreateTopicRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/doublecloud.kafka.v1.TopicService/Update',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.UpdateTopicRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/doublecloud.kafka.v1.TopicService/Delete',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.DeleteTopicRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class TopicServiceServicer(object):
    """A set of methods for managing Apache Kafka Topic resources.
    """

    def Get(self, request, context):
        """Returns the specified Apache Kafka Topic resource.

        To get the list of available Apache Kafka Topic resources, make a [List]
        request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of Apache Kafka Topic resources in the specified cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a new Apache Kafka topic in the specified cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified Apache Kafka topic.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified Apache Kafka topic.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TopicServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.GetTopicRequest.FromString,
                    response_serializer=doublecloud_dot_kafka_dot_v1_dot_topic__pb2.Topic.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.ListTopicsRequest.FromString,
                    response_serializer=doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.ListTopicsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.CreateTopicRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.UpdateTopicRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.DeleteTopicRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'doublecloud.kafka.v1.TopicService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('doublecloud.kafka.v1.TopicService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TopicService(object):
    """A set of methods for managing Apache Kafka Topic resources.
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/doublecloud.kafka.v1.TopicService/Get',
            doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.GetTopicRequest.SerializeToString,
            doublecloud_dot_kafka_dot_v1_dot_topic__pb2.Topic.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/doublecloud.kafka.v1.TopicService/List',
            doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.ListTopicsRequest.SerializeToString,
            doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.ListTopicsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/doublecloud.kafka.v1.TopicService/Create',
            doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.CreateTopicRequest.SerializeToString,
            doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/doublecloud.kafka.v1.TopicService/Update',
            doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.UpdateTopicRequest.SerializeToString,
            doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/doublecloud.kafka.v1.TopicService/Delete',
            doublecloud_dot_kafka_dot_v1_dot_topic__service__pb2.DeleteTopicRequest.SerializeToString,
            doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
