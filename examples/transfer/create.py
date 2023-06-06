from doublecloud.transfer.v1.transfer_pb2 import TransferType
from doublecloud.transfer.v1.transfer_service_pb2 import CreateTransferRequest


def create_transfer(svc, project_id: str, name: str, src_id: str, dst_id: str):
    return svc.Create(
        CreateTransferRequest(
            source_id=src_id, target_id=dst_id, name=name, project_id=project_id, type=TransferType.SNAPSHOT_ONLY
        )
    )
