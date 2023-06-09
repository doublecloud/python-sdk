from doublecloud.visualization.v1.workbook_pb2 import Dataset
from doublecloud.visualization.v1.workbook_service_pb2 import AdviseDatasetFieldsRequest


def advise_dataset_fields(svc, workbook_id: str, sources: list, connection_name: str):
    """
    Function helps to automatically define all fields, their names/IDs and types
    based on underlying data source (table, view, SQL query, etc.).
    ID of fields will be equal to column names.
    You can define them manually or use this handler to simplify for popular cases
    """
    dataset = Dataset()
    dataset.config.struct_value.update(
        {
            "fields": [],
            "avatars": None,
            "sources": sources,
        }
    )

    return svc.AdviseDatasetFields(
        AdviseDatasetFieldsRequest(
            workbook_id=workbook_id,
            connection_name=connection_name,
            partial_dataset=dataset,
        )
    )
