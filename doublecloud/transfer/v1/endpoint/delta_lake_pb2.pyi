from doublecloud.transfer.v1.endpoint.airbyte import s3_source_pb2 as _s3_source_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeltaLakeSource(_message.Message):
    __slots__ = ("provider", "table", "settings")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    provider: _s3_source_pb2.S3Source.Provider
    table: DeltaResultTable
    settings: DeltaSettings
    def __init__(self, provider: _Optional[_Union[_s3_source_pb2.S3Source.Provider, _Mapping]] = ..., table: _Optional[_Union[DeltaResultTable, _Mapping]] = ..., settings: _Optional[_Union[DeltaSettings, _Mapping]] = ...) -> None: ...

class DeltaResultTable(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeltaSettings(_message.Message):
    __slots__ = ("region",)
    REGION_FIELD_NUMBER: _ClassVar[int]
    region: str
    def __init__(self, region: _Optional[str] = ...) -> None: ...
