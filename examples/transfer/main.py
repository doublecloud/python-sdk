#!/usr/bin/env python3
import argparse
import json
import logging

# pylint: disable=E0401
from activate import activate_transfer
from create import create_transfer
from deactivate import deactivate_transfer
from delete import delete_transfer
from endpoints import create_ch_dst_endpoint, create_s3_src_endpoint, delete_endpoint

import doublecloud
from doublecloud.transfer.v1.endpoint_service_pb2_grpc import EndpointServiceStub
from doublecloud.transfer.v1.transfer_service_pb2_grpc import TransferServiceStub


def main():
    logging.basicConfig(level=logging.INFO)
    arguments = parse_args()
    if arguments.token:
        sdk = doublecloud.SDK(token=arguments.token)
    else:
        with open(arguments.sa_json_path) as infile:
            sdk = doublecloud.SDK(service_account_key=json.load(infile))

    s3_src_endpoint, ch_dst_endpoint, transfer_id = None, None, None
    endpoint_service, transfer_service = sdk.client(EndpointServiceStub), sdk.client(TransferServiceStub)

    try:
        # Create source endpoint for gathering data
        operation = create_s3_src_endpoint(endpoint_service, arguments.project_id, arguments.name)
        operation_result = sdk.wait_operation_and_get_result(operation)
        s3_src_endpoint = operation_result.operation.resource_id
        logging.info(f"Created s3 src endpoint: {s3_src_endpoint}")

        # Create dst endpoint for pushing data
        operation = create_ch_dst_endpoint(endpoint_service, arguments.project_id, arguments.name)
        operation_result = sdk.wait_operation_and_get_result(operation)
        ch_dst_endpoint = operation_result.operation.resource_id
        logging.info(f"Created ch dst endpoint: {ch_dst_endpoint}")

        # Link endpoints into single transfer
        logging.info("Linking endpoints into transfer")
        operation = create_transfer(
            transfer_service, arguments.project_id, arguments.name, s3_src_endpoint, ch_dst_endpoint
        )
        operation_result = sdk.wait_operation_and_get_result(operation)
        transfer_id = operation_result.operation.resource_id

        # Activate created transfer
        activate_transfer(transfer_service, transfer_id)
        logging.info(f"Created transfer: {transfer_id}")

        logging.info(
            "\n\nWonderful! 🚀 Check out created transfer\n" f"https://app.double.cloud/data-transfer/{transfer_id}\n"
        )

        input("Press F to respect and delete all created resources ...")

    finally:
        if transfer_id:
            deactivate_transfer(transfer_service, transfer_id)

            logging.info(f"Deleting transfer {transfer_id}")
            operation = delete_transfer(transfer_service, transfer_id)
            sdk.wait_operation_and_get_result(
                operation,
            )

        if s3_src_endpoint:
            logging.info(f"Deleting s3 endpoint {s3_src_endpoint}")
            operation = delete_endpoint(endpoint_service, s3_src_endpoint)
            sdk.wait_operation_and_get_result(
                operation,
            )
        if ch_dst_endpoint:
            logging.info(f"Deleting ch endpoint {ch_dst_endpoint}")
            operation = delete_endpoint(endpoint_service, ch_dst_endpoint)
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
