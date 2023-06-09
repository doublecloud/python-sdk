from google.protobuf.wrappers_pb2 import BoolValue

from doublecloud.v1.operation_pb2 import Operation
from doublecloud.visualization.v1.workbook_pb2 import Workbook
from doublecloud.visualization.v1.workbook_service_pb2 import UpdateWorkbookRequest


def modify_workbook(svc, workbook_id: str, workbook_config: dict) -> Operation:
    """
    Function rewrites workbook with declarative description,
    which is usually given from `describe_workbook` method.
    """
    wb = Workbook()
    wb.config.struct_value.update(workbook_config)
    return svc.Update(
        UpdateWorkbookRequest(
            workbook_id=workbook_id,
            workbook=wb,
            force_rewrite=BoolValue(value=True),
        )
    )
