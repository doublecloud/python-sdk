from doublecloud.v1.operation_pb2 import Operation
from doublecloud.visualization.v1.workbook_pb2 import Connection, PlainSecret, Secret
from doublecloud.visualization.v1.workbook_service_pb2 import (
    CreateWorkbookConnectionRequest,
)


def create_workbook_connection(svc, workbook_id: str, connection_name: str) -> Operation:
    """
    A special sample database available from all projects.
    You can easily create this connection and try all the
    DoubleCloud Visualisation features.

    Please DO NOT work with secrets this way in your production environments.

    It's just an example. Ask your system administrator for your secrets provider.
    """
    connection = Connection()
    connection.config.struct_value.update(
        {
            "kind": "clickhouse",
            "cache_ttl_sec": 600,
            "host": "rw.chcpbbeap8lpuv24hhh4.at.double.cloud",
            "port": 8443,
            "username": "examples_user",
            "secure": True,
            "raw_sql_level": "off",
        }
    )

    operation = svc.CreateConnection(
        CreateWorkbookConnectionRequest(
            workbook_id=workbook_id,
            connection_name=connection_name,
            connection=connection,
            secret=Secret(plain_secret=PlainSecret(secret="yahj@ah5foth")),
        )
    )
    return operation
