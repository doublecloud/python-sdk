from doublecloud.transfer.v1.endpoint import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetricaStreamType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRICA_STREAM_TYPE_UNSPECIFIED: _ClassVar[MetricaStreamType]
    METRICA_STREAM_TYPE_VISITS: _ClassVar[MetricaStreamType]
    METRICA_STREAM_TYPE_HITS_V2: _ClassVar[MetricaStreamType]
METRICA_STREAM_TYPE_UNSPECIFIED: MetricaStreamType
METRICA_STREAM_TYPE_VISITS: MetricaStreamType
METRICA_STREAM_TYPE_HITS_V2: MetricaStreamType

class MetricaStream(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: MetricaStreamType
    def __init__(self, type: _Optional[_Union[MetricaStreamType, str]] = ...) -> None: ...

class MetricaSource(_message.Message):
    __slots__ = ("counter_ids", "token", "streams", "enable_dashboard")
    COUNTER_IDS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    counter_ids: _containers.RepeatedScalarFieldContainer[int]
    token: _common_pb2.Secret
    streams: _containers.RepeatedCompositeFieldContainer[MetricaStream]
    enable_dashboard: bool
    def __init__(self, counter_ids: _Optional[_Iterable[int]] = ..., token: _Optional[_Union[_common_pb2.Secret, _Mapping]] = ..., streams: _Optional[_Iterable[_Union[MetricaStream, _Mapping]]] = ..., enable_dashboard: bool = ...) -> None: ...
