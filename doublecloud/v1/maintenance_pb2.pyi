from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import dayofweek_pb2 as _dayofweek_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RescheduleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESCHEDULE_TYPE_INVALID: _ClassVar[RescheduleType]
    RESCHEDULE_TYPE_IMMEDIATE: _ClassVar[RescheduleType]
    RESCHEDULE_TYPE_NEXT_AVAILABLE_WINDOW: _ClassVar[RescheduleType]
    RESCHEDULE_TYPE_SPECIFIC_TIME: _ClassVar[RescheduleType]
RESCHEDULE_TYPE_INVALID: RescheduleType
RESCHEDULE_TYPE_IMMEDIATE: RescheduleType
RESCHEDULE_TYPE_NEXT_AVAILABLE_WINDOW: RescheduleType
RESCHEDULE_TYPE_SPECIFIC_TIME: RescheduleType

class MaintenanceWindow(_message.Message):
    __slots__ = ("anytime", "weekly_maintenance_window")
    ANYTIME_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_MAINTENANCE_WINDOW_FIELD_NUMBER: _ClassVar[int]
    anytime: AnytimeMaintenanceWindow
    weekly_maintenance_window: WeeklyMaintenanceWindow
    def __init__(self, anytime: _Optional[_Union[AnytimeMaintenanceWindow, _Mapping]] = ..., weekly_maintenance_window: _Optional[_Union[WeeklyMaintenanceWindow, _Mapping]] = ...) -> None: ...

class AnytimeMaintenanceWindow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WeeklyMaintenanceWindow(_message.Message):
    __slots__ = ("day", "hour")
    DAY_FIELD_NUMBER: _ClassVar[int]
    HOUR_FIELD_NUMBER: _ClassVar[int]
    day: _dayofweek_pb2.DayOfWeek
    hour: int
    def __init__(self, day: _Optional[_Union[_dayofweek_pb2.DayOfWeek, str]] = ..., hour: _Optional[int] = ...) -> None: ...

class MaintenanceOperation(_message.Message):
    __slots__ = ("info", "scheduled_maintenance_time", "deadline_maintenance_time", "next_maintenance_window_time")
    INFO_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_MAINTENANCE_TIME_FIELD_NUMBER: _ClassVar[int]
    DEADLINE_MAINTENANCE_TIME_FIELD_NUMBER: _ClassVar[int]
    NEXT_MAINTENANCE_WINDOW_TIME_FIELD_NUMBER: _ClassVar[int]
    info: str
    scheduled_maintenance_time: _timestamp_pb2.Timestamp
    deadline_maintenance_time: _timestamp_pb2.Timestamp
    next_maintenance_window_time: _timestamp_pb2.Timestamp
    def __init__(self, info: _Optional[str] = ..., scheduled_maintenance_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deadline_maintenance_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., next_maintenance_window_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
