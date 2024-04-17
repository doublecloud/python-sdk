from doublecloud.v1 import operation_pb2 as _operation_pb2
from doublecloud.v1 import paging_pb2 as _paging_pb2
from doublecloud.kafka.v1 import topic_pb2 as _topic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetTopicRequest(_message.Message):
    __slots__ = ("cluster_id", "topic_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    topic_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., topic_name: _Optional[str] = ...) -> None: ...

class ListTopicsRequest(_message.Message):
    __slots__ = ("cluster_id", "paging")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    paging: _paging_pb2.Paging
    def __init__(self, cluster_id: _Optional[str] = ..., paging: _Optional[_Union[_paging_pb2.Paging, _Mapping]] = ...) -> None: ...

class ListTopicsResponse(_message.Message):
    __slots__ = ("topics", "next_page")
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    topics: _containers.RepeatedCompositeFieldContainer[_topic_pb2.Topic]
    next_page: _paging_pb2.NextPage
    def __init__(self, topics: _Optional[_Iterable[_Union[_topic_pb2.Topic, _Mapping]]] = ..., next_page: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ...) -> None: ...

class CreateTopicRequest(_message.Message):
    __slots__ = ("cluster_id", "topic_spec")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    topic_spec: _topic_pb2.TopicSpec
    def __init__(self, cluster_id: _Optional[str] = ..., topic_spec: _Optional[_Union[_topic_pb2.TopicSpec, _Mapping]] = ...) -> None: ...

class UpdateTopicRequest(_message.Message):
    __slots__ = ("cluster_id", "topic_name", "topic_spec")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    TOPIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    topic_name: str
    topic_spec: _topic_pb2.TopicSpec
    def __init__(self, cluster_id: _Optional[str] = ..., topic_name: _Optional[str] = ..., topic_spec: _Optional[_Union[_topic_pb2.TopicSpec, _Mapping]] = ...) -> None: ...

class DeleteTopicRequest(_message.Message):
    __slots__ = ("cluster_id", "topic_name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    TOPIC_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    topic_name: str
    def __init__(self, cluster_id: _Optional[str] = ..., topic_name: _Optional[str] = ...) -> None: ...
