# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from doublecloud.kafka.v1 import operation_service_pb2 as doublecloud_dot_kafka_dot_v1_dot_operation__service__pb2
from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2


class OperationServiceStub(object):
    """A set of methods for managing operations that are asynchronous API requests.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/doublecloud.kafka.v1.OperationService/Get',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_operation__service__pb2.GetOperationRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/doublecloud.kafka.v1.OperationService/List',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_operation__service__pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=doublecloud_dot_kafka_dot_v1_dot_operation__service__pb2.ListOperationsResponse.FromString,
                _registered_method=True)


class OperationServiceServicer(object):
    """A set of methods for managing operations that are asynchronous API requests.
    """

    def Get(self, request, context):
        """Returns the specified operation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves a list of operations that belong to the specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OperationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_operation__service__pb2.GetOperationRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_operation__service__pb2.ListOperationsRequest.FromString,
                    response_serializer=doublecloud_dot_kafka_dot_v1_dot_operation__service__pb2.ListOperationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'doublecloud.kafka.v1.OperationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('doublecloud.kafka.v1.OperationService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class OperationService(object):
    """A set of methods for managing operations that are asynchronous API requests.
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
            '/doublecloud.kafka.v1.OperationService/Get',
            doublecloud_dot_kafka_dot_v1_dot_operation__service__pb2.GetOperationRequest.SerializeToString,
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
            '/doublecloud.kafka.v1.OperationService/List',
            doublecloud_dot_kafka_dot_v1_dot_operation__service__pb2.ListOperationsRequest.SerializeToString,
            doublecloud_dot_kafka_dot_v1_dot_operation__service__pb2.ListOperationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
