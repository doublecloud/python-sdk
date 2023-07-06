# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/visualization/v1/workbook_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2
from doublecloud.visualization.v1 import workbook_pb2 as doublecloud_dot_visualization_dot_v1_dot_workbook__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3doublecloud/visualization/v1/workbook_service.proto\x12\x1c\x64oublecloud.visualization.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1e\x64oublecloud/v1/operation.proto\x1a+doublecloud/visualization/v1/workbook.proto\"5\n\x12GetWorkbookRequest\x12\x1f\n\x0bworkbook_id\x18\x01 \x01(\tR\nworkbookId\"\x9e\x01\n\x13GetWorkbookResponse\x12\x42\n\x08workbook\x18\x01 \x01(\x0b\x32&.doublecloud.visualization.v1.WorkbookR\x08workbook\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\x12\x14\n\x05title\x18\x03 \x01(\tR\x05title\x12\x1d\n\nproject_id\x18\x04 \x01(\tR\tprojectId\"]\n\x15\x43reateWorkbookRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12%\n\x0eworkbook_title\x18\x02 \x01(\tR\rworkbookTitle\"\xbd\x01\n\x15UpdateWorkbookRequest\x12\x1f\n\x0bworkbook_id\x18\x01 \x01(\tR\nworkbookId\x12\x42\n\x08workbook\x18\x02 \x01(\x0b\x32&.doublecloud.visualization.v1.WorkbookR\x08workbook\x12?\n\rforce_rewrite\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x0c\x66orceRewrite\"8\n\x15\x44\x65leteWorkbookRequest\x12\x1f\n\x0bworkbook_id\x18\x01 \x01(\tR\nworkbookId\"h\n\x1cGetWorkbookConnectionRequest\x12\x1f\n\x0bworkbook_id\x18\x01 \x01(\tR\nworkbookId\x12\'\n\x0f\x63onnection_name\x18\x02 \x01(\tR\x0e\x63onnectionName\"i\n\x1dGetWorkbookConnectionResponse\x12H\n\nconnection\x18\x01 \x01(\x0b\x32(.doublecloud.visualization.v1.ConnectionR\nconnection\"\xf3\x01\n\x1f\x43reateWorkbookConnectionRequest\x12\x1f\n\x0bworkbook_id\x18\x01 \x01(\tR\nworkbookId\x12\'\n\x0f\x63onnection_name\x18\x02 \x01(\tR\x0e\x63onnectionName\x12H\n\nconnection\x18\x03 \x01(\x0b\x32(.doublecloud.visualization.v1.ConnectionR\nconnection\x12<\n\x06secret\x18\x04 \x01(\x0b\x32$.doublecloud.visualization.v1.SecretR\x06secret\"\xf3\x01\n\x1fUpdateWorkbookConnectionRequest\x12\x1f\n\x0bworkbook_id\x18\x01 \x01(\tR\nworkbookId\x12\'\n\x0f\x63onnection_name\x18\x02 \x01(\tR\x0e\x63onnectionName\x12H\n\nconnection\x18\x03 \x01(\x0b\x32(.doublecloud.visualization.v1.ConnectionR\nconnection\x12<\n\x06secret\x18\x04 \x01(\x0b\x32$.doublecloud.visualization.v1.SecretR\x06secret\"k\n\x1f\x44\x65leteWorkbookConnectionRequest\x12\x1f\n\x0bworkbook_id\x18\x01 \x01(\tR\nworkbookId\x12\'\n\x0f\x63onnection_name\x18\x02 \x01(\tR\x0e\x63onnectionName\"\xb6\x01\n\x1a\x41\x64viseDatasetFieldsRequest\x12\x1f\n\x0bworkbook_id\x18\x01 \x01(\tR\nworkbookId\x12\'\n\x0f\x63onnection_name\x18\x02 \x01(\tR\x0e\x63onnectionName\x12N\n\x0fpartial_dataset\x18\x03 \x01(\x0b\x32%.doublecloud.visualization.v1.DatasetR\x0epartialDataset\"^\n\x1b\x41\x64viseDatasetFieldsResponse\x12?\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32%.doublecloud.visualization.v1.DatasetR\x07\x64\x61taset2\xed\x07\n\x0fWorkbookService\x12j\n\x03Get\x12\x30.doublecloud.visualization.v1.GetWorkbookRequest\x1a\x31.doublecloud.visualization.v1.GetWorkbookResponse\x12X\n\x06\x43reate\x12\x33.doublecloud.visualization.v1.CreateWorkbookRequest\x1a\x19.doublecloud.v1.Operation\x12X\n\x06Update\x12\x33.doublecloud.visualization.v1.UpdateWorkbookRequest\x1a\x19.doublecloud.v1.Operation\x12X\n\x06\x44\x65lete\x12\x33.doublecloud.visualization.v1.DeleteWorkbookRequest\x1a\x19.doublecloud.v1.Operation\x12\x88\x01\n\rGetConnection\x12:.doublecloud.visualization.v1.GetWorkbookConnectionRequest\x1a;.doublecloud.visualization.v1.GetWorkbookConnectionResponse\x12l\n\x10\x43reateConnection\x12=.doublecloud.visualization.v1.CreateWorkbookConnectionRequest\x1a\x19.doublecloud.v1.Operation\x12l\n\x10UpdateConnection\x12=.doublecloud.visualization.v1.UpdateWorkbookConnectionRequest\x1a\x19.doublecloud.v1.Operation\x12l\n\x10\x44\x65leteConnection\x12=.doublecloud.visualization.v1.DeleteWorkbookConnectionRequest\x1a\x19.doublecloud.v1.Operation\x12\x8a\x01\n\x13\x41\x64viseDatasetFields\x12\x38.doublecloud.visualization.v1.AdviseDatasetFieldsRequest\x1a\x39.doublecloud.visualization.v1.AdviseDatasetFieldsResponseBOZMgithub.com/doublecloud/go-genproto/doublecloud/visualization/v1;visualizationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.visualization.v1.workbook_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZMgithub.com/doublecloud/go-genproto/doublecloud/visualization/v1;visualization'
  _globals['_GETWORKBOOKREQUEST']._serialized_start=194
  _globals['_GETWORKBOOKREQUEST']._serialized_end=247
  _globals['_GETWORKBOOKRESPONSE']._serialized_start=250
  _globals['_GETWORKBOOKRESPONSE']._serialized_end=408
  _globals['_CREATEWORKBOOKREQUEST']._serialized_start=410
  _globals['_CREATEWORKBOOKREQUEST']._serialized_end=503
  _globals['_UPDATEWORKBOOKREQUEST']._serialized_start=506
  _globals['_UPDATEWORKBOOKREQUEST']._serialized_end=695
  _globals['_DELETEWORKBOOKREQUEST']._serialized_start=697
  _globals['_DELETEWORKBOOKREQUEST']._serialized_end=753
  _globals['_GETWORKBOOKCONNECTIONREQUEST']._serialized_start=755
  _globals['_GETWORKBOOKCONNECTIONREQUEST']._serialized_end=859
  _globals['_GETWORKBOOKCONNECTIONRESPONSE']._serialized_start=861
  _globals['_GETWORKBOOKCONNECTIONRESPONSE']._serialized_end=966
  _globals['_CREATEWORKBOOKCONNECTIONREQUEST']._serialized_start=969
  _globals['_CREATEWORKBOOKCONNECTIONREQUEST']._serialized_end=1212
  _globals['_UPDATEWORKBOOKCONNECTIONREQUEST']._serialized_start=1215
  _globals['_UPDATEWORKBOOKCONNECTIONREQUEST']._serialized_end=1458
  _globals['_DELETEWORKBOOKCONNECTIONREQUEST']._serialized_start=1460
  _globals['_DELETEWORKBOOKCONNECTIONREQUEST']._serialized_end=1567
  _globals['_ADVISEDATASETFIELDSREQUEST']._serialized_start=1570
  _globals['_ADVISEDATASETFIELDSREQUEST']._serialized_end=1752
  _globals['_ADVISEDATASETFIELDSRESPONSE']._serialized_start=1754
  _globals['_ADVISEDATASETFIELDSRESPONSE']._serialized_end=1848
  _globals['_WORKBOOKSERVICE']._serialized_start=1851
  _globals['_WORKBOOKSERVICE']._serialized_end=2856
# @@protoc_insertion_point(module_scope)
