import pytest
import jwt
import time

from doublecloud._auth_fabric import get_auth_token_requester


def test_both_params_error(iam_token, service_account_key):
    with pytest.raises(RuntimeError) as e:
        get_auth_token_requester(iam_token=iam_token, service_account_key=service_account_key).get_token()

    assert str(e.value) == "Conflicting API credentials properties are set: ['service_account_key', 'iam_token']."


def test_invalid_service_account_type():
    with pytest.raises(RuntimeError) as e:
        get_auth_token_requester(service_account_key=[]).get_token()

    assert str(e.value).startswith("Invalid Service Account Key: expecting dictionary, actually got")


@pytest.mark.parametrize("key, error_msg", [
    ("id", "Invalid Service Account Key: missing key object id."),
    ("service_account_id", "Invalid Service Account Key: missing service account id."),
    ("private_key", "Invalid Service Account Key: missing private key."),
])
def test_service_account_no_id(service_account_key, key, error_msg):
    service_account_key.pop(key)

    with pytest.raises(RuntimeError) as e:
        get_auth_token_requester(service_account_key=service_account_key).get_token()

    assert str(e.value) == error_msg


def test_service_account_key(service_account_key):
    request = get_auth_token_requester(service_account_key=service_account_key).get_token_request()
    now = int(time.time())
    headers = jwt.get_unverified_header(request)
    parsed = jwt.decode(
        request,
        key=service_account_key["public_key"],
        algorithms=['PS256'],
        audience="https://auth.double.cloud/oauth/token",
    )
    assert headers["typ"] == "JWT"
    assert headers["alg"] == "PS256"
    assert headers["kid"] == service_account_key["id"]

    assert parsed["iss"] == service_account_key["service_account_id"]
    assert parsed["sub"] == service_account_key["service_account_id"]
    assert parsed["aud"] == "https://auth.double.cloud/oauth/token"
    assert now - 60 <= int(parsed["iat"]) <= now


def test_iam_token(iam_token):
    token_func = get_auth_token_requester(iam_token=iam_token).get_token
    token = token_func()
    assert token == iam_token
