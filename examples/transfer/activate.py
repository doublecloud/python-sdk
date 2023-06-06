from doublecloud.transfer.v1.transfer_service_pb2 import ActivateTransferRequest


def activate_transfer(svc, transfer_id: str):
    return svc.Activate(ActivateTransferRequest(transfer_id=transfer_id))
