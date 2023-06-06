from doublecloud.visualization.v1.workbook_service_pb2 import (
    DeleteWorkbookConnectionRequest,
)


def delete_connection(svc, workbook_id, connection_name):
    operation = svc.DeleteConnection(
        DeleteWorkbookConnectionRequest(workbook_id=workbook_id, connection_name=connection_name)
    )
    return operation
