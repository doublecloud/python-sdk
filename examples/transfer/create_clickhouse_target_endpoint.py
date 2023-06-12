from doublecloud.transfer.v1.endpoint.clickhouse_pb2 import (
    ClickhouseConnection,
    ClickhouseConnectionOptions,
    ClickhouseTarget,
)
from doublecloud.transfer.v1.endpoint.common_pb2 import Secret
from doublecloud.transfer.v1.endpoint_pb2 import EndpointSettings
from doublecloud.transfer.v1.endpoint_service_pb2 import CreateEndpointRequest


def create_ch_dst_endpoint(svc, project_id: str, name: str):
    return svc.Create(
        CreateEndpointRequest(
            project_id=project_id,
            name=f"ch-dst-{name}",
            settings=EndpointSettings(
                clickhouse_target=ClickhouseTarget(
                    connection=ClickhouseConnection(
                        connection_options=ClickhouseConnectionOptions(
                            mdb_cluster_id="xoxo",
                            database="default",
                            user="user",
                            password=Secret(raw="98s*%^P!3Bw38"),
                        )
                    )
                )
            ),
        )
    )
