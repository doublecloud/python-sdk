# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/v1/maintenance.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.type import dayofweek_pb2 as google_dot_type_dot_dayofweek__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n doublecloud/v1/maintenance.proto\x12\x0e\x64oublecloud.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/type/dayofweek.proto\"\xca\x01\n\x11MaintenanceWindow\x12\x44\n\x07\x61nytime\x18\x01 \x01(\x0b\x32(.doublecloud.v1.AnytimeMaintenanceWindowH\x00R\x07\x61nytime\x12\x65\n\x19weekly_maintenance_window\x18\x02 \x01(\x0b\x32\'.doublecloud.v1.WeeklyMaintenanceWindowH\x00R\x17weeklyMaintenanceWindowB\x08\n\x06policy\"\x1a\n\x18\x41nytimeMaintenanceWindow\"W\n\x17WeeklyMaintenanceWindow\x12(\n\x03\x64\x61y\x18\x01 \x01(\x0e\x32\x16.google.type.DayOfWeekR\x03\x64\x61y\x12\x12\n\x04hour\x18\x02 \x01(\x03R\x04hour\"\xb9\x02\n\x14MaintenanceOperation\x12\x12\n\x04info\x18\x01 \x01(\tR\x04info\x12X\n\x1ascheduled_maintenance_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x18scheduledMaintenanceTime\x12V\n\x19\x64\x65\x61\x64line_maintenance_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x17\x64\x65\x61\x64lineMaintenanceTime\x12[\n\x1cnext_maintenance_window_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x19nextMaintenanceWindowTime*\x9a\x01\n\x0eRescheduleType\x12\x1b\n\x17RESCHEDULE_TYPE_INVALID\x10\x00\x12\x1d\n\x19RESCHEDULE_TYPE_IMMEDIATE\x10\x01\x12)\n%RESCHEDULE_TYPE_NEXT_AVAILABLE_WINDOW\x10\x02\x12!\n\x1dRESCHEDULE_TYPE_SPECIFIC_TIME\x10\x03\x42?Z=github.com/doublecloud/go-genproto/doublecloud/v1;doublecloudb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.v1.maintenance_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z=github.com/doublecloud/go-genproto/doublecloud/v1;doublecloud'
  _globals['_RESCHEDULETYPE']._serialized_start=753
  _globals['_RESCHEDULETYPE']._serialized_end=907
  _globals['_MAINTENANCEWINDOW']._serialized_start=115
  _globals['_MAINTENANCEWINDOW']._serialized_end=317
  _globals['_ANYTIMEMAINTENANCEWINDOW']._serialized_start=319
  _globals['_ANYTIMEMAINTENANCEWINDOW']._serialized_end=345
  _globals['_WEEKLYMAINTENANCEWINDOW']._serialized_start=347
  _globals['_WEEKLYMAINTENANCEWINDOW']._serialized_end=434
  _globals['_MAINTENANCEOPERATION']._serialized_start=437
  _globals['_MAINTENANCEOPERATION']._serialized_end=750
# @@protoc_insertion_point(module_scope)
