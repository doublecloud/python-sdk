import grpc

from doublecloud import _auth_plugin
from doublecloud import _consts as const
from doublecloud._auth_fabric import get_auth_token_requester


class Channels(object):
    def __init__(self, client_user_agent=None, **kwargs):
        self._channel_creds = grpc.ssl_channel_credentials(
            root_certificates=kwargs.get("root_certificates"),
            private_key=kwargs.get("private_key"),
            certificate_chain=kwargs.get("certificate_chain"),
        )
        self._endpoint = kwargs.get("endpoint", const.get_endpoint())
        self._token_requester = get_auth_token_requester(
            service_account_key=kwargs.get("service_account_key"),
            iam_token=kwargs.get("iam_token"),
            endpoint=self._endpoint,
            user_agent=kwargs.get("user_agent", const.SDK_USER_AGENT),
        )

        self._unauthenticated_channel = None
        self._channels = None
        self._client_user_agent = client_user_agent

    def channel_options(self):
        return tuple(
            ("grpc.primary_user_agent", user_agent)
            for user_agent in [self._client_user_agent, const.SDK_USER_AGENT]
            if user_agent is not None
        )

    def _get_endpoints(self):
        return {
            "clickhouse": f"clickhouse.api.{self._endpoint}:443",
            "kafka": f"kafka.api.{self._endpoint}:443",
            "network": f"vpc.api.{self._endpoint}:443",
            "transfer": f"transfer.api.{self._endpoint}:443",
            "visualization": f"visualization.api.{self._endpoint}:443",
        }

    def channel(self, endpoint):
        if not self._channels:
            self._unauthenticated_channel = grpc.secure_channel(
                self._endpoint, self._channel_creds, options=self.channel_options()
            )

            plugin = _auth_plugin.Credentials(self._token_requester)
            call_creds = grpc.metadata_call_credentials(plugin)
            creds = grpc.composite_channel_credentials(self._channel_creds, call_creds)

            self._channels = {
                svc: grpc.secure_channel(addr, creds, options=self.channel_options())
                for svc, addr in self._get_endpoints().items()
            }

        if endpoint not in self._channels:
            raise RuntimeError(f"Unknown endpoint: {endpoint}")

        return self._channels[endpoint]
