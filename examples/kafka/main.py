#!/usr/bin/env python3
import argparse
import json
import logging

# pylint: disable=E0401
from create import create_cluster
from delete import delete_cluster
from topics import create_topic, delete_topic
from users import create_user, delete_user

import doublecloud
from doublecloud.kafka.v1.user_pb2 import Permission


def populate(sdk, cluster_id):
    for topic in ["events", "orders", "calls"]:
        logging.info(f'🪵 Creating topic "{topic}" ...')
        create_topic(sdk, cluster_id, name=topic, partitions=1)
    logging.info(f"🪵 Topics: https://app.double.cloud/kafka/{cluster_id}/topics")

    logging.info('🤖 Creating user "engineer" ...')
    create_user(
        sdk,
        cluster_id,
        name="engineer",
        password="Gizmo-Headsman-Travel3",
        permissions=[Permission(topic_name="*", role=Permission.ACCESS_ROLE_ADMIN)],
    )
    logging.info('🤖 Creating user "api" who will produce messages to topics ...')
    # A user without permission will have all permissions
    create_user(sdk, cluster_id, name="api", password="Happiness1-Confirm-Saloon")

    logging.info('🤖 Creating user "crm" who will consume messages for CRM system ...')
    create_user(
        sdk,
        cluster_id,
        name="crm",
        password="Crazed-Unclamped-Efficient0",
        permissions=[
            Permission(topic_name="orders", role=Permission.ACCESS_ROLE_CONSUMER),
            Permission(topic_name="calls", role=Permission.ACCESS_ROLE_PRODUCER),
        ],
    )
    logging.info('🤖 Creating user "transfer" who will consume messages for CRM system ...')
    create_user(
        sdk,
        cluster_id,
        name="transfer",
        password="Delegator-Chaos0-Driven",
        permissions=[
            Permission(topic_name="events", role=Permission.ACCESS_ROLE_CONSUMER),
            Permission(topic_name="orders", role=Permission.ACCESS_ROLE_CONSUMER),
            Permission(topic_name="calls", role=Permission.ACCESS_ROLE_CONSUMER),
        ],
    )


def clean(sdk, cluster_id):
    for topic in ["events", "orders", "calls"]:
        logging.info(f'🪵 Deleting topic "{topic}" ...\n')
        delete_topic(sdk, cluster_id, topic)

    for user in ["engineer", "api", "crm", "transfer"]:
        logging.info(f'🤖 Deleting user "{user}" ...\n')
        delete_user(sdk, cluster_id, name=user)


def main():
    logging.basicConfig(level=logging.INFO)
    arguments = parse_args()
    if arguments.token:
        sdk = doublecloud.SDK(token=arguments.token)
    else:
        with open(arguments.sa_json_path) as infile:
            sdk = doublecloud.SDK(service_account_key=json.load(infile))

    cluster_id = None
    try:
        operation = create_cluster(
            sdk, arguments.project_id, arguments.cloud_type, arguments.region, arguments.name, arguments.network_id
        )
        operation_result = sdk.wait_operation_and_get_result(
            operation,
        )
        cluster_id = operation_result.operation.resource_id

        logging.info("\n\nWonderful! 🚀 Check out created cluster\n" f"https://app.double.cloud/kafka/{cluster_id}\n")

        populate(sdk, cluster_id)
        input("Press F to respect and delete all created resources ...")
        clean(sdk, cluster_id)
    finally:
        if cluster_id:
            logging.info(f"Deleting cluster {cluster_id}")
            operation = delete_cluster(sdk, cluster_id)
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
    parser.add_argument("--cloud-type", default="aws", help="Cloud provider")
    parser.add_argument("--region", default="eu-central-1", help="Region to deploy to.")
    parser.add_argument("--name", default="sdk-example", help="New cluster name.")
    parser.add_argument("--network-id", help="Network of the cluster.")

    return parser.parse_args()


if __name__ == "__main__":
    main()
