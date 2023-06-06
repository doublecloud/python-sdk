from doublecloud.transfer.v1.transfer_service_pb2 import DeleteTransferRequest


def delete_transfer(svc, transfer_id: str):
    return svc.Delete(DeleteTransferRequest(transfer_id=transfer_id))
