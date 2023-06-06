from doublecloud.transfer.v1.transfer_service_pb2 import DeactivateTransferRequest


def deactivate_transfer(svc, transfer_id: str):
    return svc.Deactivate(DeactivateTransferRequest(transfer_id=transfer_id))
