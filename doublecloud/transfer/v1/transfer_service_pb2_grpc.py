# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from doublecloud.transfer.v1 import transfer_pb2 as doublecloud_dot_transfer_dot_v1_dot_transfer__pb2
from doublecloud.transfer.v1 import transfer_service_pb2 as doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2
from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2


class TransferServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/doublecloud.transfer.v1.TransferService/Create',
                request_serializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.CreateTransferRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/doublecloud.transfer.v1.TransferService/Update',
                request_serializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.UpdateTransferRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/doublecloud.transfer.v1.TransferService/Delete',
                request_serializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.DeleteTransferRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                )
        self.List = channel.unary_unary(
                '/doublecloud.transfer.v1.TransferService/List',
                request_serializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.ListTransfersRequest.SerializeToString,
                response_deserializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.ListTransfersResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/doublecloud.transfer.v1.TransferService/Get',
                request_serializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.GetTransferRequest.SerializeToString,
                response_deserializer=doublecloud_dot_transfer_dot_v1_dot_transfer__pb2.Transfer.FromString,
                )
        self.Deactivate = channel.unary_unary(
                '/doublecloud.transfer.v1.TransferService/Deactivate',
                request_serializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.DeactivateTransferRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                )
        self.Activate = channel.unary_unary(
                '/doublecloud.transfer.v1.TransferService/Activate',
                request_serializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.ActivateTransferRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                )


class TransferServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deactivate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Activate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransferServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.CreateTransferRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.UpdateTransferRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.DeleteTransferRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.ListTransfersRequest.FromString,
                    response_serializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.ListTransfersResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.GetTransferRequest.FromString,
                    response_serializer=doublecloud_dot_transfer_dot_v1_dot_transfer__pb2.Transfer.SerializeToString,
            ),
            'Deactivate': grpc.unary_unary_rpc_method_handler(
                    servicer.Deactivate,
                    request_deserializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.DeactivateTransferRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Activate': grpc.unary_unary_rpc_method_handler(
                    servicer.Activate,
                    request_deserializer=doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.ActivateTransferRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'doublecloud.transfer.v1.TransferService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TransferService(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/doublecloud.transfer.v1.TransferService/Create',
            doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.CreateTransferRequest.SerializeToString,
            doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/doublecloud.transfer.v1.TransferService/Update',
            doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.UpdateTransferRequest.SerializeToString,
            doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/doublecloud.transfer.v1.TransferService/Delete',
            doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.DeleteTransferRequest.SerializeToString,
            doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/doublecloud.transfer.v1.TransferService/List',
            doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.ListTransfersRequest.SerializeToString,
            doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.ListTransfersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/doublecloud.transfer.v1.TransferService/Get',
            doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.GetTransferRequest.SerializeToString,
            doublecloud_dot_transfer_dot_v1_dot_transfer__pb2.Transfer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deactivate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/doublecloud.transfer.v1.TransferService/Deactivate',
            doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.DeactivateTransferRequest.SerializeToString,
            doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Activate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/doublecloud.transfer.v1.TransferService/Activate',
            doublecloud_dot_transfer_dot_v1_dot_transfer__service__pb2.ActivateTransferRequest.SerializeToString,
            doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
