#!/usr/bin/env python3
import argparse
import json
import logging

# pylint: disable=E0401
from advise_dataset_fields import advise_dataset_fields
from create import create_workbook
from create_connection import create_workbook_connection
from delete import delete_workbook
from delete_connection import delete_connection
from google.protobuf.json_format import MessageToDict
from modify import modify_workbook

import doublecloud
from doublecloud.visualization.v1.workbook_service_pb2_grpc import WorkbookServiceStub


def get_workbook_config_with_single_dataset(
    dataset_name: str,
    ds_fields: list = None,
    ds_avatars: dict = None,
    ds_sources: list = None,
    charts: list = None,
    dashboards: list = None,
) -> dict:
    """
    Function returns a declarative structure of a sample workbook with single dataset.
    Structure used for changing workbook config through API
    """
    return {
        "datasets": [
            {
                "name": dataset_name,
                "dataset": {
                    "fields": ds_fields or [],
                    "avatars": ds_avatars or None,
                    "sources": ds_sources or [],
                },
            }
        ],
        "charts": charts or [],
        "dashboards": dashboards or [],
    }


def get_clickhouse_table_dataset_sources(*, connection_name: str, db_name: str, table_name: str) -> list:
    """
    Function returns a dataset source as DB table or view.
    You can use another datasource types:
    https://double.cloud/docs/en/public-api/api-reference/visualization/configs/DataSourceSpec
    And another connection types:
    https://double.cloud/docs/en/public-api/api-reference/visualization/configs/Connection
    """
    return [
        {
            "id": "production_marts",
            "title": "hits_sample",
            "connection_ref": connection_name,
            "spec": {"kind": "sql_table", "db_name": db_name, "table_name": table_name},
        }
    ]


def a_column_chart(name: str, *, dataset_name: str) -> dict:
    """
    This is an example of column chart
    See https://double.cloud/docs/en/data-visualization/quickstart#create-a-column-chart
    """
    return {
        "chart": {
            "ad_hoc_fields": [
                {
                    # Here we adding field with applied aggregation to chart
                    # This is equal to adding field to dataset. But only when used with this chart.
                    "field": {
                        "description": None,
                        "id": "time_spent_sum",
                        "cast": "float",
                        # Example of calculated field
                        # https://double.cloud/docs/en/data-visualization/concepts/calculated-fields
                        # Note that in API fields should be referenced by ID, not title
                        "calc_spec": {
                            "kind": "id_formula",
                            "formula": "SUM([Time_Spent])",
                        },
                        "aggregation": "none",
                        "hidden": False,
                        "title": "Time Spent Sum",
                    },
                    "dataset_name": dataset_name,
                }
            ],
            "visualization": {
                "y": [
                    {
                        "source": {
                            "kind": "ref",
                            "id": "time_spent_sum",
                        }
                    }
                ],
                "kind": "column_chart",
                "sort": [],
                "coloring": {
                    "mounts": [],
                    "palette_id": None,
                    "kind": "dimension",
                    "source": {"kind": "ref", "id": "browser"},
                },
                "x": [{"source": {"kind": "ref", "id": "date"}}],
            },
            "datasets": [dataset_name],
        },
        "name": name,
    }


def a_donut_chart(name: str, *, dataset_name: str) -> dict:
    """
    Example of a donut chart
    See https://double.cloud/docs/en/data-visualization/quickstart#create-a-donut-chart
    """
    return {
        "chart": {
            "ad_hoc_fields": [
                # Here we adding field with applied aggregation to chart
                # This is equal to adding field to dataset. But only when used with this chart.
                {
                    "field": {
                        "description": None,
                        "id": "browser_count_unique",
                        "cast": "string",
                        "title": "Browser Count Unique",
                        # Example of direct field with applied aggregation
                        "aggregation": "countunique",
                        "calc_spec": {"kind": "direct", "avatar_id": "production_marts", "field_name": "Browser"},
                        "hidden": False,
                    },
                }
            ],
            "visualization": {
                "kind": "donut_chart",
                "sort": [],
                "coloring": {
                    "mounts": [],
                    "palette_id": None,
                    "source": {"kind": "ref", "id": "technology"},
                },
                "measures": {
                    "source": {
                        "kind": "ref",
                        "id": "browser_count_unique",
                    }
                },
            },
            "datasets": [dataset_name],
        },
        "name": name,
    }


def an_indicator_chart(name: str, *, dataset_name: str) -> dict:
    """
    Example of an indicator chart
    See https://double.cloud/docs/en/data-visualization/quickstart#create-an-indicator
    """
    return {
        "chart": {
            "ad_hoc_fields": [],
            "visualization": {
                "field": {
                    "source": {
                        "kind": "ref",
                        "id": "hits_count",
                    }
                },
                "kind": "indicator",
            },
            "datasets": [dataset_name],
        },
        "name": name,
    }


def dash_element_selector_by_dataset_field(
    element_id: str,
    title: str,
    dataset_name: str,
    field_id: str,
    # Element placement
    # See details here: https://double.cloud/docs/en/public-api/api-reference/visualization/configs/Dashboard
    x: int,
    y: int,
    h: int,
    w: int,
):
    return {
        "element": {
            "kind": "control_multiselect",
            "show_title": True,
            "title": title,
            "source": {
                "kind": "dataset_field",
                "dataset_name": dataset_name,
                "field_id": field_id,
            },
            "comparison_operation": None,
            "default_value": None,
        },
        "id": element_id,
        "placement": {"x": x, "y": y, "h": h, "w": w},
    }


def dash_element_chart(
    title: str,
    chart_name: str,
    element_id: str,
    # Element placement
    # See details here: https://double.cloud/docs/en/public-api/api-reference/visualization/configs/Dashboard
    x: int,
    y: int,
    h: int,
    w: int,
):
    # Generating unique chart tab ID based on element ID
    chart_tab_id = "ctid_" + element_id + "_1"

    return {
        "element": {
            "hide_title": False,
            "kind": "charts_container",
            "default_active_chart_tab_id": chart_tab_id,
            "tabs": [
                {
                    "title": title,
                    "id": chart_tab_id,
                    "chart_name": chart_name,
                }
            ],
        },
        "id": element_id,
        "placement": {"x": x, "y": y, "h": h, "w": w},
    }


def get_single_tab_dashboard(dashboard_name: str, elements: list[dict]) -> list:
    return [
        {
            "dashboard": {
                "tabs": [
                    {
                        "title": "Tab 1",
                        "id": "qG",
                        "items": elements,
                        "ignored_connections": [],
                    }
                ]
            },
            "name": dashboard_name,
        }
    ]


def main():  # pylint: disable=too-many-locals,too-many-statements
    logging.basicConfig(level=logging.INFO)
    arguments = parse_args()
    if arguments.token:
        sdk = doublecloud.SDK(token=arguments.token)
    else:
        with open(arguments.sa_json_path) as infile:
            sdk = doublecloud.SDK(service_account_key=json.load(infile))

    workbook_id = None
    connection_created = False

    # Entries references each other by it's names
    # So we define it here
    connection_name = "conn_ch_1"
    dataset_name = "ds_hits_sample"
    chart_name_total_hits = "chart_total_hits"
    chart_name_time_spent_per_browser = "chart_time_spent_per_browser"
    chart_name_user_share_by_platform = "chart_user_share_by_platform"
    dashboard_name = "dash_main"

    svc = sdk.client(WorkbookServiceStub)
    try:
        # Create a new workbook
        operation = create_workbook(svc, arguments.project_id, arguments.name)
        operation_result = sdk.wait_operation_and_get_result(operation)
        workbook_id = operation_result.operation.resource_id
        logging.info(f"Created a new workbook: {workbook_id}, https://app.double.cloud/workbooks/{workbook_id}")

        # Create a connection to a database
        operation = create_workbook_connection(svc, workbook_id, connection_name=connection_name)
        sdk.wait_operation_and_get_result(operation)
        connection_created = True
        logging.info(f"Created a new connection: {connection_name}")

        logging.info("Modify workbook and add data source")
        sources = get_clickhouse_table_dataset_sources(
            connection_name=connection_name,
            db_name="examples",
            table_name="hits",
        )
        workbook_spec = get_workbook_config_with_single_dataset(
            dataset_name=dataset_name,
            ds_sources=sources,
        )
        operation = modify_workbook(svc, workbook_id, workbook_spec)
        sdk.wait_operation_and_get_result(operation)

        # Get advised fields for our datasource, instead of manually write all of them
        advised_ds_config = MessageToDict(
            advise_dataset_fields(svc, workbook_id, sources, connection_name).dataset.config
        )
        # Adding aggregated field to dataset
        advised_ds_config["fields"].append(
            {
                "description": None,
                "id": "hits_count",
                "cast": "integer",
                "calc_spec": {"kind": "direct", "field_name": "Hit_ID"},
                "aggregation": "countunique",
                "hidden": False,
                "title": "Total hits",
            }
        )

        # Fill the workbook with advised fields
        workbook_spec = get_workbook_config_with_single_dataset(
            dataset_name=dataset_name, ds_fields=advised_ds_config["fields"], ds_sources=advised_ds_config["sources"]
        )
        operation = modify_workbook(svc, workbook_id, workbook_spec)
        sdk.wait_operation_and_get_result(operation)
        logging.info("Filled advised fields for our datasets")

        # Create example charts and dashboard
        charts = [
            an_indicator_chart(chart_name_total_hits, dataset_name=dataset_name),
            a_donut_chart(chart_name_user_share_by_platform, dataset_name=dataset_name),
            a_column_chart(chart_name_time_spent_per_browser, dataset_name=dataset_name),
        ]
        dashboards = get_single_tab_dashboard(
            dashboard_name,
            [
                dash_element_selector_by_dataset_field(
                    title="Traffic Source",
                    dataset_name=dataset_name,
                    field_id="traffic_source",
                    element_id="P9",
                    x=0,
                    y=0,
                    h=2,
                    w=20,
                ),
                dash_element_chart(
                    chart_name=chart_name_time_spent_per_browser,
                    title="Time spent per browser",
                    element_id="K5",
                    x=0,
                    y=2,
                    h=16,
                    w=20,
                ),
                dash_element_chart(
                    chart_name=chart_name_user_share_by_platform,
                    title="User shares by platform",
                    element_id="nd",
                    x=20,
                    y=0,
                    h=23,
                    w=16,
                ),
                dash_element_chart(
                    chart_name=chart_name_total_hits,
                    title="Total hits",
                    element_id="L7",
                    x=0,
                    y=18,
                    h=12,
                    w=20,
                ),
            ],
        )
        workbook_spec = get_workbook_config_with_single_dataset(
            dataset_name=dataset_name,
            ds_fields=advised_ds_config["fields"],
            ds_sources=advised_ds_config["sources"],
            charts=charts,
            dashboards=dashboards,
        )
        operation = modify_workbook(svc, workbook_id, workbook_spec)
        sdk.wait_operation_and_get_result(operation)
        logging.info("Added charts for our data")

        logging.info(
            "\n\nWonderful! 🚀 Check out created workbook\n" f"https://app.double.cloud/workbooks/{workbook_id}\n"
        )

        input("Press F to respect and delete all created resources ...")
    finally:
        if workbook_id:
            try:
                if connection_created:
                    logging.info(f"Deleting connection {connection_name}")
                    operation = delete_connection(svc, workbook_id, connection_name)
                    sdk.wait_operation_and_get_result(
                        operation,
                    )
            finally:
                logging.info(f"Deleting workbook {workbook_id}")
                operation = delete_workbook(svc, workbook_id)
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
    parser.add_argument("--name", default="sdk-example", help="New workbook title")

    return parser.parse_args()


if __name__ == "__main__":
    main()
