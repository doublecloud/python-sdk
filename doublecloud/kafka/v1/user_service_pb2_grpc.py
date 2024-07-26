# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from doublecloud.kafka.v1 import user_pb2 as doublecloud_dot_kafka_dot_v1_dot_user__pb2
from doublecloud.kafka.v1 import user_service_pb2 as doublecloud_dot_kafka_dot_v1_dot_user__service__pb2
from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2


class UserServiceStub(object):
    """A set of methods for managing Apache Kafka User resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/doublecloud.kafka.v1.UserService/Get',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.GetUserRequest.SerializeToString,
                response_deserializer=doublecloud_dot_kafka_dot_v1_dot_user__pb2.User.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/doublecloud.kafka.v1.UserService/List',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.ListUsersRequest.SerializeToString,
                response_deserializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.ListUsersResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/doublecloud.kafka.v1.UserService/Create',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/doublecloud.kafka.v1.UserService/Update',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/doublecloud.kafka.v1.UserService/Delete',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.GrantPermission = channel.unary_unary(
                '/doublecloud.kafka.v1.UserService/GrantPermission',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.GrantUserPermissionRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.RevokePermission = channel.unary_unary(
                '/doublecloud.kafka.v1.UserService/RevokePermission',
                request_serializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.RevokeUserPermissionRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class UserServiceServicer(object):
    """A set of methods for managing Apache Kafka User resources.
    """

    def Get(self, request, context):
        """Returns the specified Apache Kafka User resource.

        To get the list of available Apache Kafka User resources, make a [List] request.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves the list of Apache Kafka User resources for the specified cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates an Apache Kafka User on the specified cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified Apache Kafka User.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified Apache Kafka User.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GrantPermission(self, request, context):
        """Grants permission to the specified Apache Kafka User.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevokePermission(self, request, context):
        """Revokes permission from the specified Apache Kafka User.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.GetUserRequest.FromString,
                    response_serializer=doublecloud_dot_kafka_dot_v1_dot_user__pb2.User.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.ListUsersRequest.FromString,
                    response_serializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.ListUsersResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.CreateUserRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.UpdateUserRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.DeleteUserRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GrantPermission': grpc.unary_unary_rpc_method_handler(
                    servicer.GrantPermission,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.GrantUserPermissionRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'RevokePermission': grpc.unary_unary_rpc_method_handler(
                    servicer.RevokePermission,
                    request_deserializer=doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.RevokeUserPermissionRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'doublecloud.kafka.v1.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('doublecloud.kafka.v1.UserService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """A set of methods for managing Apache Kafka User resources.
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
            '/doublecloud.kafka.v1.UserService/Get',
            doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.GetUserRequest.SerializeToString,
            doublecloud_dot_kafka_dot_v1_dot_user__pb2.User.FromString,
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
            '/doublecloud.kafka.v1.UserService/List',
            doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.ListUsersRequest.SerializeToString,
            doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.ListUsersResponse.FromString,
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
            '/doublecloud.kafka.v1.UserService/Create',
            doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.CreateUserRequest.SerializeToString,
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
            '/doublecloud.kafka.v1.UserService/Update',
            doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.UpdateUserRequest.SerializeToString,
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
            '/doublecloud.kafka.v1.UserService/Delete',
            doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.DeleteUserRequest.SerializeToString,
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
    def GrantPermission(request,
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
            '/doublecloud.kafka.v1.UserService/GrantPermission',
            doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.GrantUserPermissionRequest.SerializeToString,
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
    def RevokePermission(request,
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
            '/doublecloud.kafka.v1.UserService/RevokePermission',
            doublecloud_dot_kafka_dot_v1_dot_user__service__pb2.RevokeUserPermissionRequest.SerializeToString,
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
