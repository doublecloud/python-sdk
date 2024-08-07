# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from doublecloud.kafka.v1 import connector_pb2 as doublecloud_dot_kafka_dot_v1_dot_connector__pb2
from doublecloud.kafka.v1 import connector_service_pb2 as doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2
from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2


class ConnectorServiceStub(object):
    """A set of methods for managing Apache Kafka® connectors.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/doublecloud.kafka.v1.ConnectorService/Get',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.GetConnectorRequest.SerializeToString,
                response_deserializer=doublecloud_dot_kafka_dot_v1_dot_connector__pb2.Connector.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/doublecloud.kafka.v1.ConnectorService/List',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.ListConnectorsRequest.SerializeToString,
                response_deserializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.ListConnectorsResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/doublecloud.kafka.v1.ConnectorService/Create',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.CreateConnectorRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/doublecloud.kafka.v1.ConnectorService/Update',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.UpdateConnectorRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/doublecloud.kafka.v1.ConnectorService/Delete',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.DeleteConnectorRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Resume = channel.unary_unary(
                '/doublecloud.kafka.v1.ConnectorService/Resume',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.ResumeConnectorRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Pause = channel.unary_unary(
                '/doublecloud.kafka.v1.ConnectorService/Pause',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.PauseConnectorRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class ConnectorServiceServicer(object):
    """A set of methods for managing Apache Kafka® connectors.
    """

    def Get(self, request, context):
        """Returns information about an Apache Kafka® connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of Apache Kafka® connectors in a cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a new Apache Kafka® connector in a cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates an Apache Kafka® connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes an Apache Kafka® connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Resume(self, request, context):
        """Resumes an Apache Kafka® connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Pause(self, request, context):
        """Pauses an Apache Kafka® connector.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConnectorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.GetConnectorRequest.FromString,
                    response_serializer=doublecloud_dot_kafka_dot_v1_dot_connector__pb2.Connector.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.ListConnectorsRequest.FromString,
                    response_serializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.ListConnectorsResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.CreateConnectorRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.UpdateConnectorRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.DeleteConnectorRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Resume': grpc.unary_unary_rpc_method_handler(
                    servicer.Resume,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.ResumeConnectorRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Pause': grpc.unary_unary_rpc_method_handler(
                    servicer.Pause,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.PauseConnectorRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'doublecloud.kafka.v1.ConnectorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('doublecloud.kafka.v1.ConnectorService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ConnectorService(object):
    """A set of methods for managing Apache Kafka® connectors.
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
            '/doublecloud.kafka.v1.ConnectorService/Get',
            doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.GetConnectorRequest.SerializeToString,
            doublecloud_dot_kafka_dot_v1_dot_connector__pb2.Connector.FromString,
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
            '/doublecloud.kafka.v1.ConnectorService/List',
            doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.ListConnectorsRequest.SerializeToString,
            doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.ListConnectorsResponse.FromString,
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
            '/doublecloud.kafka.v1.ConnectorService/Create',
            doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.CreateConnectorRequest.SerializeToString,
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
            '/doublecloud.kafka.v1.ConnectorService/Update',
            doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.UpdateConnectorRequest.SerializeToString,
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
            '/doublecloud.kafka.v1.ConnectorService/Delete',
            doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.DeleteConnectorRequest.SerializeToString,
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
    def Resume(request,
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
            '/doublecloud.kafka.v1.ConnectorService/Resume',
            doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.ResumeConnectorRequest.SerializeToString,
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
    def Pause(request,
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
            '/doublecloud.kafka.v1.ConnectorService/Pause',
            doublecloud_dot_kafka_dot_v1_dot_connector__service__pb2.PauseConnectorRequest.SerializeToString,
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
