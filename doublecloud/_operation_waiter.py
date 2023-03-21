import logging
import time
import uuid
from datetime import datetime

import grpc
from google.protobuf.empty_pb2 import Empty

from doublecloud._backoff import backoff_exponential_jittered_min_interval
from doublecloud._consts import OPERATIONS_PREFIX_MAP
from doublecloud._retry_interceptor import RetryInterceptor
from doublecloud.clickhouse.v1.operation_service_pb2 import (
    GetOperationRequest as chGetOperationRequest,
)
from doublecloud.clickhouse.v1.operation_service_pb2_grpc import (
    OperationServiceStub as chOperationServiceStub,
)
from doublecloud.kafka.v1.operation_service_pb2 import (
    GetOperationRequest as kfGetOperationRequest,
)
from doublecloud.kafka.v1.operation_service_pb2_grpc import (
    OperationServiceStub as kfOperationServiceStub,
)
from doublecloud.network.v1.operation_service_pb2 import (
    GetOperationRequest as vpcGetOperationRequest,
)
from doublecloud.network.v1.operation_service_pb2_grpc import (
    OperationServiceStub as vpcOperationServiceStub,
)
from doublecloud.operations import OperationError, OperationResult
from doublecloud.transfer.v1.operation_service_pb2 import (
    GetOperationRequest as dtGetOperationRequest,
)
from doublecloud.transfer.v1.operation_service_pb2_grpc import (
    OperationServiceStub as dtOperationServiceStub,
)
from doublecloud.v1.operation_pb2 import Operation


def is_valid_uuid(s):
    try:
        uuid.UUID(s)
        return True
    except ValueError:
        return False


def get_operation_service_stub(operation):
    if operation.id.startswith(OPERATIONS_PREFIX_MAP["clickhouse"]):
        return chOperationServiceStub
    if operation.id.startswith(OPERATIONS_PREFIX_MAP["kafka"]):
        return kfOperationServiceStub
    if operation.id.startswith(OPERATIONS_PREFIX_MAP["transfer"]):
        return dtOperationServiceStub
    if operation.id.startswith(OPERATIONS_PREFIX_MAP["transfer_endpoints"]):
        return dtOperationServiceStub
    if is_valid_uuid(operation.id):
        return vpcOperationServiceStub
    raise RuntimeError(f"Unknown operation type, operation: {operation}")


def get_operation_get_request(operation):
    if operation.id.startswith(OPERATIONS_PREFIX_MAP["clickhouse"]):
        return chGetOperationRequest(operation_id=operation.id)
    if operation.id.startswith(OPERATIONS_PREFIX_MAP["kafka"]):
        return kfGetOperationRequest(operation_id=operation.id)
    if operation.id.startswith(OPERATIONS_PREFIX_MAP["transfer"]):
        return dtGetOperationRequest(operation_id=operation.id)
    if operation.id.startswith(OPERATIONS_PREFIX_MAP["transfer_endpoints"]):
        return dtGetOperationRequest(operation_id=operation.id)
    if is_valid_uuid(operation.id):
        return vpcGetOperationRequest(operation_id=operation.id)
    raise RuntimeError(f"Unknown operation type, operation_id: {operation.id}")


def operation_waiter(sdk, operation, timeout):
    retriable_codes = (
        grpc.StatusCode.UNAVAILABLE,
        grpc.StatusCode.RESOURCE_EXHAUSTED,
        grpc.StatusCode.INTERNAL,
    )
    # withstand server downtime for ~3.4 minutes with an exponential backof
    retry_interceptor = RetryInterceptor(
        max_retry_count=13,
        per_call_timeout=30,
        back_off_func=backoff_exponential_jittered_min_interval(),
        retriable_codes=retriable_codes,
    )
    return OperationWaiter(operation, retry_interceptor=retry_interceptor, timeout=timeout, sdk=sdk)


def wait_for_operation(sdk, operation, timeout):
    waiter = operation_waiter(sdk, operation, timeout)
    for _ in waiter:
        time.sleep(1)
    return waiter.operation


def get_operation_result(sdk, operation, meta_type=None, timeout=None, logger=None):
    if not logger:
        logger = logging.getLogger()
        logger.addHandler(logging.NullHandler())
    operation_result = OperationResult(operation)

    create_time = datetime.fromtimestamp(operation.create_time.seconds)
    message = (
        "Running double.cloud operation. ID: {id}. "
        + "Description: {description}. Created at: {create_time}. "
        + "Created by: {created_by}."
    )
    message = message.format(
        id=operation.id,
        description=operation.description,
        create_time=create_time,
        created_by=operation.created_by,
    )
    if meta_type and meta_type is not Empty:
        unpacked_meta = meta_type()
        operation.metadata.Unpack(unpacked_meta)
        operation_result.meta = unpacked_meta
        message += " Meta: {unpacked_meta}.".format(unpacked_meta=unpacked_meta)
    logger.info(message)
    result = wait_for_operation(sdk, operation, timeout=timeout)
    if result.error and result.error.code:
        error_message = (
            "Error double.cloud operation. ID: {id}. "
            + "Error code: {code}. Details: {details}. "
            + "Message: {message}."
        )
        error_message = error_message.format(
            id=result.id,
            code=result.error.code,
            details=result.error.details,
            message=result.error.message,
        )
        logger.error(error_message)
        raise OperationError(message=error_message, operation_result=result)

    logger.info(f"Done double.cloud operation. ID: {operation.id}.")
    return OperationResult(result)


class OperationWaiter:
    def __init__(self, operation, retry_interceptor=None, timeout=None, sdk=None, operation_service=None):
        self.__operation = operation
        self.__operation_service = operation_service
        self.__deadline = time.time() + timeout if timeout else None
        if sdk:
            try:
                stub = get_operation_service_stub(operation)
                self.__operation_service = sdk.client(stub, interceptor=retry_interceptor)
            except RuntimeError:
                pass
                # Some of services have already finished blocked operations
                # and they haven't additional operation services.
                # We will throw an exception in case of running operation without operation service.

    @property
    def operation(self):
        return self.__operation

    @property
    def done(self):
        if self.__operation is not None and self.__operation.status == Operation.Status.STATUS_DONE:
            # A shortcut for instantly finished operations
            return True
        if not self.__operation_service:
            raise RuntimeError(f"Unknown operation service for operation {self.__operation}")
        self.__operation = self.__operation_service.Get(get_operation_get_request(self.__operation))
        return self.__operation is not None and self.__operation.status == Operation.Status.STATUS_DONE

    def __iter__(self):
        return self

    def __next__(self):
        if self.done or self.__deadline is not None and time.time() >= self.__deadline:
            raise StopIteration()

    next = __next__  # for Python 2
