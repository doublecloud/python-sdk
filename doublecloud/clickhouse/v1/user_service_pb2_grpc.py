# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from doublecloud.clickhouse.v1 import user_pb2 as doublecloud_dot_clickhouse_dot_v1_dot_user__pb2
from doublecloud.clickhouse.v1 import user_service_pb2 as doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2
from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2


class UserServiceStub(object):
    """A set of methods for managing ClickHouse users.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/doublecloud.clickhouse.v1.UserService/Get',
                request_serializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.GetUserRequest.SerializeToString,
                response_deserializer=doublecloud_dot_clickhouse_dot_v1_dot_user__pb2.User.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/doublecloud.clickhouse.v1.UserService/List',
                request_serializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.ListUsersRequest.SerializeToString,
                response_deserializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.ListUsersResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/doublecloud.clickhouse.v1.UserService/Create',
                request_serializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/doublecloud.clickhouse.v1.UserService/Update',
                request_serializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/doublecloud.clickhouse.v1.UserService/Delete',
                request_serializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.GetRole = channel.unary_unary(
                '/doublecloud.clickhouse.v1.UserService/GetRole',
                request_serializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.GetRoleRequest.SerializeToString,
                response_deserializer=doublecloud_dot_clickhouse_dot_v1_dot_user__pb2.Role.FromString,
                _registered_method=True)
        self.ListRoles = channel.unary_unary(
                '/doublecloud.clickhouse.v1.UserService/ListRoles',
                request_serializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.ListRolesRequest.SerializeToString,
                response_deserializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.ListRolesResponse.FromString,
                _registered_method=True)
        self.CreateRole = channel.unary_unary(
                '/doublecloud.clickhouse.v1.UserService/CreateRole',
                request_serializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.CreateRoleRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.UpdateRole = channel.unary_unary(
                '/doublecloud.clickhouse.v1.UserService/UpdateRole',
                request_serializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.UpdateRoleRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.DeleteRole = channel.unary_unary(
                '/doublecloud.clickhouse.v1.UserService/DeleteRole',
                request_serializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.DeleteRoleRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


class UserServiceServicer(object):
    """A set of methods for managing ClickHouse users.
    """

    def Get(self, request, context):
        """Returns the specified ClickHouse user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves a list of ClickHouse users.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a new ClickHouse user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Modifies the specified ClickHouse user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified ClickHouse user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRole(self, request, context):
        """Returns the specified ClickHouse role.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRoles(self, request, context):
        """Retrieves a list of ClickHouse roles.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRole(self, request, context):
        """Creates a new ClickHouse role.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRole(self, request, context):
        """Modifies the specified ClickHouse role.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRole(self, request, context):
        """Deletes the specified ClickHouse role.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.GetUserRequest.FromString,
                    response_serializer=doublecloud_dot_clickhouse_dot_v1_dot_user__pb2.User.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.ListUsersRequest.FromString,
                    response_serializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.ListUsersResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.CreateUserRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.UpdateUserRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.DeleteUserRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GetRole': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRole,
                    request_deserializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.GetRoleRequest.FromString,
                    response_serializer=doublecloud_dot_clickhouse_dot_v1_dot_user__pb2.Role.SerializeToString,
            ),
            'ListRoles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRoles,
                    request_deserializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.ListRolesRequest.FromString,
                    response_serializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.ListRolesResponse.SerializeToString,
            ),
            'CreateRole': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRole,
                    request_deserializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.CreateRoleRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateRole': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRole,
                    request_deserializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.UpdateRoleRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeleteRole': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRole,
                    request_deserializer=doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.DeleteRoleRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'doublecloud.clickhouse.v1.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('doublecloud.clickhouse.v1.UserService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """A set of methods for managing ClickHouse users.
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
            '/doublecloud.clickhouse.v1.UserService/Get',
            doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.GetUserRequest.SerializeToString,
            doublecloud_dot_clickhouse_dot_v1_dot_user__pb2.User.FromString,
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
            '/doublecloud.clickhouse.v1.UserService/List',
            doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.ListUsersRequest.SerializeToString,
            doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.ListUsersResponse.FromString,
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
            '/doublecloud.clickhouse.v1.UserService/Create',
            doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.CreateUserRequest.SerializeToString,
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
            '/doublecloud.clickhouse.v1.UserService/Update',
            doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.UpdateUserRequest.SerializeToString,
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
            '/doublecloud.clickhouse.v1.UserService/Delete',
            doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.DeleteUserRequest.SerializeToString,
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
    def GetRole(request,
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
            '/doublecloud.clickhouse.v1.UserService/GetRole',
            doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.GetRoleRequest.SerializeToString,
            doublecloud_dot_clickhouse_dot_v1_dot_user__pb2.Role.FromString,
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
    def ListRoles(request,
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
            '/doublecloud.clickhouse.v1.UserService/ListRoles',
            doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.ListRolesRequest.SerializeToString,
            doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.ListRolesResponse.FromString,
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
    def CreateRole(request,
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
            '/doublecloud.clickhouse.v1.UserService/CreateRole',
            doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.CreateRoleRequest.SerializeToString,
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
    def UpdateRole(request,
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
            '/doublecloud.clickhouse.v1.UserService/UpdateRole',
            doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.UpdateRoleRequest.SerializeToString,
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
    def DeleteRole(request,
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
            '/doublecloud.clickhouse.v1.UserService/DeleteRole',
            doublecloud_dot_clickhouse_dot_v1_dot_user__service__pb2.DeleteRoleRequest.SerializeToString,
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