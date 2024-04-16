from doublecloud.kafka.v1.user_pb2 import UserSpec
from doublecloud.kafka.v1.user_service_pb2 import CreateUserRequest, DeleteUserRequest
from doublecloud.kafka.v1.user_service_pb2_grpc import UserServiceStub


def create_user(sdk, cluster_id, **kwargs):
    user_service = sdk.client(UserServiceStub)
    sdk.wait_operation_and_get_result(
        user_service.Create(
            CreateUserRequest(
                cluster_id=cluster_id,
                user_spec=UserSpec(
                    name=kwargs.get("name", "producer"),
                    password=kwargs.get("name", "producer"),
                    permissions=kwargs.get("permissions", None),
                ),
            )
        )
    )


def delete_user(sdk, cluster_id, name):
    user_service = sdk.client(UserServiceStub)
    sdk.wait_operation_and_get_result(user_service.Delete(DeleteUserRequest(cluster_id=cluster_id, user_name=name)))
