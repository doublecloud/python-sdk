# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from doublecloud.airflow.v1 import cluster_pb2 as doublecloud_dot_airflow_dot_v1_dot_cluster__pb2
from doublecloud.airflow.v1 import cluster_service_pb2 as doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2
from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2


class ClusterServiceStub(object):
    """A set of methods for managing Apache Airflow® clusters.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/doublecloud.airflow.v1.ClusterService/Get',
                request_serializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.GetClusterRequest.SerializeToString,
                response_deserializer=doublecloud_dot_airflow_dot_v1_dot_cluster__pb2.Cluster.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/doublecloud.airflow.v1.ClusterService/List',
                request_serializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListClustersRequest.SerializeToString,
                response_deserializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListClustersResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/doublecloud.airflow.v1.ClusterService/Create',
                request_serializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.CreateClusterRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/doublecloud.airflow.v1.ClusterService/Delete',
                request_serializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.DeleteClusterRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/doublecloud.airflow.v1.ClusterService/Update',
                request_serializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.UpdateClusterRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListOperations = channel.unary_unary(
                '/doublecloud.airflow.v1.ClusterService/ListOperations',
                request_serializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListClusterOperationsRequest.SerializeToString,
                response_deserializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListClusterOperationsResponse.FromString,
                _registered_method=True)
        self.RescheduleMaintenance = channel.unary_unary(
                '/doublecloud.airflow.v1.ClusterService/RescheduleMaintenance',
                request_serializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.RescheduleMaintenanceRequest.SerializeToString,
                response_deserializer=doublecloud_dot_v1_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.ListCustomImages = channel.unary_unary(
                '/doublecloud.airflow.v1.ClusterService/ListCustomImages',
                request_serializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListCustomImagesRequest.SerializeToString,
                response_deserializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListCustomImagesResponse.FromString,
                _registered_method=True)


class ClusterServiceServicer(object):
    """A set of methods for managing Apache Airflow® clusters.
    """

    def Get(self, request, context):
        """Returns the specified Apache Airflow® cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Retrieves a list of Apache Airflow® clusters that belong to the specified
        project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates an Apache Airflow® cluster in the specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified Apache Airflow® cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified Apache Airflow® cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """List cluster operations.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RescheduleMaintenance(self, request, context):
        """Reschedule planned maintenance operation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCustomImages(self, request, context):
        """List of custom images associated to the cluster
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClusterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.GetClusterRequest.FromString,
                    response_serializer=doublecloud_dot_airflow_dot_v1_dot_cluster__pb2.Cluster.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListClustersRequest.FromString,
                    response_serializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListClustersResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.CreateClusterRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.DeleteClusterRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.UpdateClusterRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListClusterOperationsRequest.FromString,
                    response_serializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListClusterOperationsResponse.SerializeToString,
            ),
            'RescheduleMaintenance': grpc.unary_unary_rpc_method_handler(
                    servicer.RescheduleMaintenance,
                    request_deserializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.RescheduleMaintenanceRequest.FromString,
                    response_serializer=doublecloud_dot_v1_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListCustomImages': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCustomImages,
                    request_deserializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListCustomImagesRequest.FromString,
                    response_serializer=doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListCustomImagesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'doublecloud.airflow.v1.ClusterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('doublecloud.airflow.v1.ClusterService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ClusterService(object):
    """A set of methods for managing Apache Airflow® clusters.
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
            '/doublecloud.airflow.v1.ClusterService/Get',
            doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.GetClusterRequest.SerializeToString,
            doublecloud_dot_airflow_dot_v1_dot_cluster__pb2.Cluster.FromString,
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
            '/doublecloud.airflow.v1.ClusterService/List',
            doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListClustersRequest.SerializeToString,
            doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListClustersResponse.FromString,
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
            '/doublecloud.airflow.v1.ClusterService/Create',
            doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.CreateClusterRequest.SerializeToString,
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
            '/doublecloud.airflow.v1.ClusterService/Delete',
            doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.DeleteClusterRequest.SerializeToString,
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
            '/doublecloud.airflow.v1.ClusterService/Update',
            doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.UpdateClusterRequest.SerializeToString,
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
    def ListOperations(request,
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
            '/doublecloud.airflow.v1.ClusterService/ListOperations',
            doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListClusterOperationsRequest.SerializeToString,
            doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListClusterOperationsResponse.FromString,
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
    def RescheduleMaintenance(request,
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
            '/doublecloud.airflow.v1.ClusterService/RescheduleMaintenance',
            doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.RescheduleMaintenanceRequest.SerializeToString,
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
    def ListCustomImages(request,
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
            '/doublecloud.airflow.v1.ClusterService/ListCustomImages',
            doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListCustomImagesRequest.SerializeToString,
            doublecloud_dot_airflow_dot_v1_dot_cluster__service__pb2.ListCustomImagesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
