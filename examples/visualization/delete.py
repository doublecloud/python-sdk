from doublecloud.visualization.v1.workbook_service_pb2 import DeleteWorkbookRequest


def delete_workbook(svc, workbook_id):
    operation = svc.Delete(DeleteWorkbookRequest(workbook_id=workbook_id))
    return operation
