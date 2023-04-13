#!/usr/bin/env python3
import argparse
import json
import logging

import doublecloud
from doublecloud.network.v1.network_service_pb2 import (
    CreateNetworkRequest,
    DeleteNetworkRequest,
)
from doublecloud.network.v1.network_service_pb2_grpc import NetworkServiceStub


def create_network(sdk, project_id, region_id, name, ipv4_cidr_block):
    network_service = sdk.client(NetworkServiceStub)
    operation = network_service.Create(
        CreateNetworkRequest(
            project_id=project_id,
            cloud_type="aws",
            region_id=region_id,
            name=name,
            ipv4_cidr_block=ipv4_cidr_block,
        )
    )
    logging.info("Creating initiated")
    return operation


def delete_network(sdk, network_id):
    network_service = sdk.client(NetworkServiceStub)
    return network_service.Delete(DeleteNetworkRequest(network_id=network_id))


def main():
    logging.basicConfig(level=logging.INFO)
    arguments = parse_args()
    if arguments.token:
        sdk = doublecloud.SDK(token=arguments.token)
    else:
        with open(arguments.sa_json_path) as infile:
            sdk = doublecloud.SDK(service_account_key=json.load(infile))

    network_id = None
    try:
        operation = create_network(sdk, arguments.project_id, arguments.region, arguments.name, arguments.ipv4_cidr)
        operation_result = sdk.wait_operation_and_get_result(
            operation,
        )
        network_id = operation_result.operation.resource_id
        logging.info(
            "\n\nWonderful! 🚀 Check out created network\n" f"https://app.double.cloud/vpc/network/{network_id}\n"
        )

        input("Press F to respect and delete all created resources ...")

    finally:
        if network_id:
            logging.info("Deleting network {network_id}")
            operation = delete_network(sdk, network_id)
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
    parser.add_argument("--region", default="eu-central-1", help="Region to deploy to.")
    parser.add_argument("--name", default="sdk-example", help="New cluster name.")
    parser.add_argument("--ipv4-cidr", help="IPv4 block for network", default="10.0.0.0/16")

    return parser.parse_args()


if __name__ == "__main__":
    main()
