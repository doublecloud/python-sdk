import time

from doublecloud._operation_waiter import OperationWaiter

from doublecloud.v1.operation_pb2 import Operation


class _OperationMock:
    def __init__(self, op_id, done):
        self.id = op_id
        self.status = Operation.Status.STATUS_DONE if done else Operation.Status.STATUS_RUNNING


class _WaitTenIterations:
    def __init__(self, op_id):
        self.__get_count = 0
        self.__id = op_id

    def Get(self, _):
        self.__get_count += 1
        return _OperationMock(self.__id, done=self.__get_count > 10)


def test_ten_iterations():
    waiter = OperationWaiter(Operation(id="choxx"), operation_service=_WaitTenIterations("cho1234"))

    count = 0
    for _ in waiter:
        count += 1

    assert waiter.operation.status == Operation.Status.STATUS_DONE
    assert count == 10


class _NeverDone:
    def __init__(self, op_id):
        self.__id = op_id

    def Get(self, _):
        return _OperationMock(self.__id, done=False)


def test_timeout():
    waiter = OperationWaiter(Operation(id="kfo1234"), operation_service=_NeverDone("kfo1234"), timeout=10)

    for _ in waiter:
        time.sleep(1)

    assert waiter.operation.status == Operation.Status.STATUS_RUNNING
