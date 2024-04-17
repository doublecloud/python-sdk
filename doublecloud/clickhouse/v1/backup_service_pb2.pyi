from doublecloud.v1 import operation_pb2 as _operation_pb2
from doublecloud.v1 import paging_pb2 as _paging_pb2
from doublecloud.clickhouse.v1 import backup_pb2 as _backup_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetBackupRequest(_message.Message):
    __slots__ = ("backup_id",)
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    backup_id: str
    def __init__(self, backup_id: _Optional[str] = ...) -> None: ...

class ListBackupsRequest(_message.Message):
    __slots__ = ("project_id", "paging")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    paging: _paging_pb2.Paging
    def __init__(self, project_id: _Optional[str] = ..., paging: _Optional[_Union[_paging_pb2.Paging, _Mapping]] = ...) -> None: ...

class ListBackupsResponse(_message.Message):
    __slots__ = ("backups", "next_page")
    BACKUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_FIELD_NUMBER: _ClassVar[int]
    backups: _containers.RepeatedCompositeFieldContainer[_backup_pb2.Backup]
    next_page: _paging_pb2.NextPage
    def __init__(self, backups: _Optional[_Iterable[_Union[_backup_pb2.Backup, _Mapping]]] = ..., next_page: _Optional[_Union[_paging_pb2.NextPage, _Mapping]] = ...) -> None: ...

class CreateBackupRequest(_message.Message):
    __slots__ = ("cluster_id", "name")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    name: str
    def __init__(self, cluster_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class DeleteBackupRequest(_message.Message):
    __slots__ = ("backup_id",)
    BACKUP_ID_FIELD_NUMBER: _ClassVar[int]
    backup_id: str
    def __init__(self, backup_id: _Optional[str] = ...) -> None: ...
