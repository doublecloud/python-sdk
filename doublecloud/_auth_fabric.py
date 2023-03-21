import time
from datetime import datetime

# noinspection PyUnresolvedReferences
# jwt package depends on cryptography
import cryptography  # noqa: F401; pylint: disable=unused-import
import jwt
import requests
import six

from doublecloud import _consts as const


def __validate_service_account_key(sa_key):
    if not isinstance(sa_key, dict):
        actual_type = type(sa_key)
        raise RuntimeError(f"Invalid Service Account Key: expecting dictionary, actually got {actual_type}")

    obj_id = sa_key.get("id")
    sa_id = sa_key.get("service_account_id")
    private_key = sa_key.get("private_key")

    if not obj_id:
        raise RuntimeError("Invalid Service Account Key: missing key object id.")

    if not sa_id:
        raise RuntimeError("Invalid Service Account Key: missing service account id.")

    if not private_key:
        raise RuntimeError("Invalid Service Account Key: missing private key.")

    private_key_prefix = "-----BEGIN PRIVATE KEY-----"
    if not isinstance(private_key, six.string_types) or not private_key.startswith(private_key_prefix):
        error_message = (
            "Invalid Service Account Key: private key is in incorrect format."
            + f"Should start with {private_key_prefix}.\n"
        )
        raise RuntimeError(error_message)


def get_auth_token_requester(service_account_key=None, iam_token=None, endpoint=None, user_agent=None):
    if endpoint is None:
        endpoint = const.get_endpoint()
    auth_methods = [("service_account_key", service_account_key), ("iam_token", iam_token)]
    auth_methods = [(auth_type, value) for auth_type, value in auth_methods if value is not None]

    if not auth_methods:
        raise RuntimeError("Auth method didn't provided, credentials are unset.")

    if len(auth_methods) > 1:
        properties = [auth[0] for auth in auth_methods]
        raise RuntimeError(f"Conflicting API credentials properties are set: {properties}.")

    auth_name, _ = auth_methods[0]
    if auth_name == "service_account_key":
        __validate_service_account_key(service_account_key)
        return ServiceAccountAuth(service_account_key, endpoint, user_agent)
    if auth_name == "iam_token":
        return IamTokenAuth(iam_token)

    raise RuntimeError(f"Unknown auth method: {auth_name}")


class ServiceAccountAuth:
    __SECONDS_IN_HOUR = 60.0 * 60.0

    def __init__(self, sa_key, endpoint=None, user_agent=const.SDK_USER_AGENT):
        self.__sa_key = sa_key
        if endpoint is None:
            endpoint = const.get_endpoint()
        self._endpoint = endpoint
        self._user_agent = user_agent

    def get_token(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        if self._user_agent:
            headers["User-Agent"] = self._user_agent

        assertion = self.get_token_request()
        r = requests.post(
            f"https://auth.{self._endpoint}/oauth/token",
            headers=headers,
            data=f"grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion={assertion}",
            timeout=30.0,
        )
        r.raise_for_status()
        return r.json()["access_token"]

    def get_token_request(self):
        now = time.time()
        now_utc = datetime.utcfromtimestamp(now)
        exp_utc = datetime.utcfromtimestamp(now + self.__SECONDS_IN_HOUR)
        aud = f"https://auth.{self._endpoint}/oauth/token"
        payload = {
            "iss": self.__sa_key["service_account_id"],
            "sub": self.__sa_key["service_account_id"],
            "aud": aud,
            "iat": now_utc,
            "exp": exp_utc,
        }

        headers = {
            "typ": "JWT",
            "alg": "PS256",
            "kid": self.__sa_key["id"],
        }

        return jwt.encode(payload, self.__sa_key["private_key"], algorithm="PS256", headers=headers)


class IamTokenAuth:
    def __init__(self, iam_token):
        self.__iam_token = iam_token

    def get_token(self):
        return self.__iam_token
