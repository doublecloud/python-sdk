import os

import pkg_resources

try:
    VERSION = pkg_resources.get_distribution("doublecloud").version
except pkg_resources.DistributionNotFound:
    VERSION = "0.0.0"

SDK_USER_AGENT = f"doublecloud-python-sdk/{VERSION}"

OPERATIONS_PREFIX_MAP = {
    "clickhouse": "cho",
    "kafka": "kfo",
    "transfer": "dtj",
    "transfer_endpoints": "dte",
}


def get_endpoint():
    return os.environ.get("DC_ENDPOINT", "double.cloud")
