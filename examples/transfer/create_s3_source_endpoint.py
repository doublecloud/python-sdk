from doublecloud.transfer.v1.endpoint.airbyte.s3_source_pb2 import S3Source
from doublecloud.transfer.v1.endpoint_pb2 import EndpointSettings
from doublecloud.transfer.v1.endpoint_service_pb2 import CreateEndpointRequest


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
