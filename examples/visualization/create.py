from doublecloud.v1.operation_pb2 import Operation
from doublecloud.visualization.v1.workbook_service_pb2 import CreateWorkbookRequest


def create_workbook(svc, project_id: str, name: str) -> Operation:
    """
    Function creates an empty workbook
    We will fill it with other functions
    """
    return svc.Create(CreateWorkbookRequest(project_id=project_id, workbook_title=name))
