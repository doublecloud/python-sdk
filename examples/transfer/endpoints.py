from doublecloud.transfer.v1.endpoint.airbyte.s3_source_pb2 import S3Source
from doublecloud.transfer.v1.endpoint.clickhouse_pb2 import (
    ClickhouseConnection,
    ClickhouseConnectionOptions,
    ClickhouseTarget,
)
from doublecloud.transfer.v1.endpoint.common_pb2 import Secret
from doublecloud.transfer.v1.endpoint_pb2 import EndpointSettings
from doublecloud.transfer.v1.endpoint_service_pb2 import (
    CreateEndpointRequest,
    DeleteEndpointRequest,
)


def create_s3_src_endpoint(svc, project_id: str, name: str):
    return svc.Create(
        CreateEndpointRequest(
            project_id=project_id,
            name=f"s3-src-{name}",
            settings=EndpointSettings(
                s3_source=S3Source(
                    dataset="test",
                    path_pattern="test",
                    schema="test",
                    format=S3Source.Format(csv=S3Source.Csv()),
                    provider=S3Source.Provider(bucket="test"),
                )
            ),
        )
    )


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


def delete_endpoint(svc, endpoint_id: str):
    return svc.Delete(DeleteEndpointRequest(endpoint_id=endpoint_id))
