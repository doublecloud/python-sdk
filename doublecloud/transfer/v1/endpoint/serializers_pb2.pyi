from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SerializerAuto(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SerializerJSON(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DebeziumSerializerParameter(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class SerializerDebezium(_message.Message):
    __slots__ = ("serializer_parameters",)
    SERIALIZER_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    serializer_parameters: _containers.RepeatedCompositeFieldContainer[DebeziumSerializerParameter]
    def __init__(self, serializer_parameters: _Optional[_Iterable[_Union[DebeziumSerializerParameter, _Mapping]]] = ...) -> None: ...

class Serializer(_message.Message):
    __slots__ = ("serializer_auto", "serializer_json", "serializer_debezium")
    SERIALIZER_AUTO_FIELD_NUMBER: _ClassVar[int]
    SERIALIZER_JSON_FIELD_NUMBER: _ClassVar[int]
    SERIALIZER_DEBEZIUM_FIELD_NUMBER: _ClassVar[int]
    serializer_auto: SerializerAuto
    serializer_json: SerializerJSON
    serializer_debezium: SerializerDebezium
    def __init__(self, serializer_auto: _Optional[_Union[SerializerAuto, _Mapping]] = ..., serializer_json: _Optional[_Union[SerializerJSON, _Mapping]] = ..., serializer_debezium: _Optional[_Union[SerializerDebezium, _Mapping]] = ...) -> None: ...
