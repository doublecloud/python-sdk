import inspect

import grpc

from doublecloud import _channels, _operation_waiter
from doublecloud._backoff import backoff_exponential_with_jitter
from doublecloud._retry_interceptor import RetryInterceptor
from doublecloud._wrappers import Wrappers


class SDK(object):
    def __init__(self, interceptor=None, user_agent=None, **kwargs):
        """
        API entry-point object.

        :param interceptor: GRPC interceptor to be used instead of default RetryInterceptor
        :type interceptor: Union[
            UnaryUnaryClientInterceptor,
            UnaryStreamClientInterceptor,
            StreamUnaryClientInterceptor,
            StreamStreamClientInterceptor
        ]
        :param user_agent: String to prepend User-Agent metadata header for all GRPC requests made via SDK object
        :type user_agent: Optional[str]
        """
        self._channels = _channels.Channels(client_user_agent=user_agent, **kwargs)
        if interceptor is None:
            interceptor = RetryInterceptor(
                max_retry_count=5,
                per_call_timeout=30,
                back_off_func=backoff_exponential_with_jitter(1, 30),
            )
        self._default_interceptor = interceptor
        self.wrappers = Wrappers(self)

    def set_interceptor(self, interceptor):
        self._default_interceptor = interceptor

    def client(self, stub_ctor, interceptor=None):
        service = _service_for_ctor(stub_ctor)
        channel = self._channels.channel(service)
        if interceptor is not None:
            channel = grpc.intercept_channel(channel, interceptor)
        elif self._default_interceptor is not None:
            channel = grpc.intercept_channel(channel, self._default_interceptor)
        return stub_ctor(channel)

    def waiter(self, operation_id, timeout=None):
        return _operation_waiter.operation_waiter(self, operation_id, timeout)

    def wait_operation_and_get_result(self, operation, meta_type=None, timeout=None, logger=None):
        return _operation_waiter.get_operation_result(self, operation, meta_type, timeout, logger)

    def create_operation_and_get_result(
        self,
        request,
        service,
        method_name,
        meta_type=None,
        timeout=None,
        logger=None,
    ):
        operation = getattr(self.client(service), method_name)(request)
        return self.wait_operation_and_get_result(
            operation,
            meta_type=meta_type,
            timeout=timeout,
            logger=logger,
        )


def _service_for_ctor(stub_ctor):
    m = inspect.getmodule(stub_ctor)
    name = m.__name__
    if not name.startswith("doublecloud"):
        raise RuntimeError(f"Not a double.cloud service {stub_ctor}")

    for k, v in _supported_modules:
        if name.startswith(k):
            return v

    raise RuntimeError(f"Unknown service {stub_ctor}")


_supported_modules = [
    ("doublecloud.kafka", "kafka"),
    ("doublecloud.clickhouse", "clickhouse"),
    ("doublecloud.network", "network"),
    ("doublecloud.transfer", "transfer"),
    ("doublecloud.visualization", "visualization"),
]
