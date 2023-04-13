#!/usr/bin/env python3
import argparse
import json
import logging

import doublecloud
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
from doublecloud.transfer.v1.endpoint_service_pb2_grpc import EndpointServiceStub
from doublecloud.transfer.v1.transfer_pb2 import TransferType
from doublecloud.transfer.v1.transfer_service_pb2 import (
    CreateTransferRequest,
    DeleteTransferRequest,
)
from doublecloud.transfer.v1.transfer_service_pb2_grpc import TransferServiceStub


def create_s3_src_endpoint(sdk, project_id, name):
    svc = sdk.client(EndpointServiceStub)
    operation = svc.Create(
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
    return operation


def delete_endpoint(sdk, endpoint_id):
    svc = sdk.client(EndpointServiceStub)
    operation = svc.Delete(DeleteEndpointRequest(endpoint_id=endpoint_id))
    return operation


def create_ch_dst_endpoint(sdk, project_id, name):
    svc = sdk.client(EndpointServiceStub)
    operation = svc.Create(
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
    return operation


def create_transfer(sdk, project_id, name, src_id, dst_id):
    svc = sdk.client(TransferServiceStub)
    operation = svc.Create(
        CreateTransferRequest(
            source_id=src_id, target_id=dst_id, name=name, project_id=project_id, type=TransferType.SNAPSHOT_ONLY
        )
    )
    return operation


def delete_transfer(sdk, transfer_id):
    svc = sdk.client(TransferServiceStub)
    operation = svc.Delete(DeleteTransferRequest(transfer_id=transfer_id))
    return operation


def main():
    logging.basicConfig(level=logging.INFO)
    arguments = parse_args()
    if arguments.token:
        sdk = doublecloud.SDK(token=arguments.token)
    else:
        with open(arguments.sa_json_path) as infile:
            sdk = doublecloud.SDK(service_account_key=json.load(infile))

    s3_src_endpoint, ch_dst_endpoint, transfer_id = None, None, None
    try:
        # Create source endpoint for gathering data
        operation = create_s3_src_endpoint(sdk, arguments.project_id, arguments.name)
        operation_result = sdk.wait_operation_and_get_result(operation)
        s3_src_endpoint = operation_result.operation.resource_id
        logging.info(f"Created s3 src endpoint: {s3_src_endpoint}")

        # Create dst endpoint for pushing data
        operation = create_ch_dst_endpoint(sdk, arguments.project_id, arguments.name)
        operation_result = sdk.wait_operation_and_get_result(operation)
        ch_dst_endpoint = operation_result.operation.resource_id
        logging.info(f"Created ch dst endpoint: {ch_dst_endpoint}")

        # Link endpoints into single transfer
        logging.info("Linking endpoints into transfer")
        operation = create_transfer(sdk, arguments.project_id, arguments.name, s3_src_endpoint, ch_dst_endpoint)
        operation_result = sdk.wait_operation_and_get_result(operation)
        transfer_id = operation_result.operation.resource_id
        logging.info(f"Created transfer: {transfer_id}")

        logging.info(
            "\n\nWonderful! 🚀 Check out created transfer\n" f"https://app.double.cloud/data-transfer/{transfer_id}\n"
        )

        input("Press F to respect and delete all created resources ...")

    finally:
        if transfer_id:
            logging.info(f"Deleting transfer {transfer_id}")
            operation = delete_transfer(sdk, transfer_id)
            sdk.wait_operation_and_get_result(
                operation,
            )

        if s3_src_endpoint:
            logging.info(f"Deleting s3 endpoint {s3_src_endpoint}")
            operation = delete_endpoint(sdk, s3_src_endpoint)
            sdk.wait_operation_and_get_result(
                operation,
            )
        if ch_dst_endpoint:
            logging.info(f"Deleting ch endpoint {ch_dst_endpoint}")
            operation = delete_endpoint(sdk, ch_dst_endpoint)
            sdk.wait_operation_and_get_result(
                operation,
            )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)

    auth = parser.add_mutually_exclusive_group(required=True)
    auth.add_argument(
        "--sa-json-path",
        help="Path to the service account key JSON file.\nThis file can be created using UI:\n"
        "Members -> Service Accounts -> Create and then create authorized keys",
    )
    auth.add_argument("--token", help="IAM token")
    parser.add_argument("--project-id", help="Your project id", required=True)
    parser.add_argument("--name", default="sdk-example", help="New cluster name.")

    return parser.parse_args()


if __name__ == "__main__":
    main()
