# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/kafka/v1/connector_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2
from doublecloud.v1 import paging_pb2 as doublecloud_dot_v1_dot_paging__pb2
from doublecloud.kafka.v1 import connector_pb2 as doublecloud_dot_kafka_dot_v1_dot_connector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,doublecloud/kafka/v1/connector_service.proto\x12\x14\x64oublecloud.kafka.v1\x1a\x1e\x64oublecloud/v1/operation.proto\x1a\x1b\x64oublecloud/v1/paging.proto\x1a$doublecloud/kafka/v1/connector.proto\"[\n\x13GetConnectorRequest\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12%\n\x0e\x63onnector_name\x18\x02 \x01(\tR\rconnectorName\"f\n\x15ListConnectorsRequest\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12.\n\x06paging\x18\x02 \x01(\x0b\x32\x16.doublecloud.v1.PagingR\x06paging\"\x90\x01\n\x16ListConnectorsResponse\x12?\n\nconnectors\x18\x01 \x03(\x0b\x32\x1f.doublecloud.kafka.v1.ConnectorR\nconnectors\x12\x35\n\tnext_page\x18\x02 \x01(\x0b\x32\x18.doublecloud.v1.NextPageR\x08nextPage\"\x83\x01\n\x16\x43reateConnectorRequest\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12J\n\x0e\x63onnector_spec\x18\x02 \x01(\x0b\x32#.doublecloud.kafka.v1.ConnectorSpecR\rconnectorSpec\"_\n\x17\x43reateConnectorMetadata\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12%\n\x0e\x63onnector_name\x18\x02 \x01(\tR\rconnectorName\"\xb6\x01\n\x16UpdateConnectorRequest\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12%\n\x0e\x63onnector_name\x18\x02 \x01(\tR\rconnectorName\x12P\n\x0e\x63onnector_spec\x18\x04 \x01(\x0b\x32).doublecloud.kafka.v1.UpdateConnectorSpecR\rconnectorSpecJ\x04\x08\x03\x10\x04\"_\n\x17UpdateConnectorMetadata\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12%\n\x0e\x63onnector_name\x18\x02 \x01(\tR\rconnectorName\"^\n\x16\x44\x65leteConnectorRequest\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12%\n\x0e\x63onnector_name\x18\x02 \x01(\tR\rconnectorName\"_\n\x17\x44\x65leteConnectorMetadata\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12%\n\x0e\x63onnector_name\x18\x02 \x01(\tR\rconnectorName\"^\n\x16ResumeConnectorRequest\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12%\n\x0e\x63onnector_name\x18\x02 \x01(\tR\rconnectorName\"_\n\x17ResumeConnectorMetadata\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12%\n\x0e\x63onnector_name\x18\x02 \x01(\tR\rconnectorName\"]\n\x15PauseConnectorRequest\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12%\n\x0e\x63onnector_name\x18\x02 \x01(\tR\rconnectorName\"^\n\x16PauseConnectorMetadata\x12\x1d\n\ncluster_id\x18\x01 \x01(\tR\tclusterId\x12%\n\x0e\x63onnector_name\x18\x02 \x01(\tR\rconnectorName2\xe5\x04\n\x10\x43onnectorService\x12Q\n\x03Get\x12).doublecloud.kafka.v1.GetConnectorRequest\x1a\x1f.doublecloud.kafka.v1.Connector\x12\x61\n\x04List\x12+.doublecloud.kafka.v1.ListConnectorsRequest\x1a,.doublecloud.kafka.v1.ListConnectorsResponse\x12Q\n\x06\x43reate\x12,.doublecloud.kafka.v1.CreateConnectorRequest\x1a\x19.doublecloud.v1.Operation\x12Q\n\x06Update\x12,.doublecloud.kafka.v1.UpdateConnectorRequest\x1a\x19.doublecloud.v1.Operation\x12Q\n\x06\x44\x65lete\x12,.doublecloud.kafka.v1.DeleteConnectorRequest\x1a\x19.doublecloud.v1.Operation\x12Q\n\x06Resume\x12,.doublecloud.kafka.v1.ResumeConnectorRequest\x1a\x19.doublecloud.v1.Operation\x12O\n\x05Pause\x12+.doublecloud.kafka.v1.PauseConnectorRequest\x1a\x19.doublecloud.v1.OperationB?Z=github.com/doublecloud/go-genproto/doublecloud/kafka/v1;kafkab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.kafka.v1.connector_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/doublecloud/go-genproto/doublecloud/kafka/v1;kafka'
  _globals['_GETCONNECTORREQUEST']._serialized_start=169
  _globals['_GETCONNECTORREQUEST']._serialized_end=260
  _globals['_LISTCONNECTORSREQUEST']._serialized_start=262
  _globals['_LISTCONNECTORSREQUEST']._serialized_end=364
  _globals['_LISTCONNECTORSRESPONSE']._serialized_start=367
  _globals['_LISTCONNECTORSRESPONSE']._serialized_end=511
  _globals['_CREATECONNECTORREQUEST']._serialized_start=514
  _globals['_CREATECONNECTORREQUEST']._serialized_end=645
  _globals['_CREATECONNECTORMETADATA']._serialized_start=647
  _globals['_CREATECONNECTORMETADATA']._serialized_end=742
  _globals['_UPDATECONNECTORREQUEST']._serialized_start=745
  _globals['_UPDATECONNECTORREQUEST']._serialized_end=927
  _globals['_UPDATECONNECTORMETADATA']._serialized_start=929
  _globals['_UPDATECONNECTORMETADATA']._serialized_end=1024
  _globals['_DELETECONNECTORREQUEST']._serialized_start=1026
  _globals['_DELETECONNECTORREQUEST']._serialized_end=1120
  _globals['_DELETECONNECTORMETADATA']._serialized_start=1122
  _globals['_DELETECONNECTORMETADATA']._serialized_end=1217
  _globals['_RESUMECONNECTORREQUEST']._serialized_start=1219
  _globals['_RESUMECONNECTORREQUEST']._serialized_end=1313
  _globals['_RESUMECONNECTORMETADATA']._serialized_start=1315
  _globals['_RESUMECONNECTORMETADATA']._serialized_end=1410
  _globals['_PAUSECONNECTORREQUEST']._serialized_start=1412
  _globals['_PAUSECONNECTORREQUEST']._serialized_end=1505
  _globals['_PAUSECONNECTORMETADATA']._serialized_start=1507
  _globals['_PAUSECONNECTORMETADATA']._serialized_end=1601
  _globals['_CONNECTORSERVICE']._serialized_start=1604
  _globals['_CONNECTORSERVICE']._serialized_end=2217
# @@protoc_insertion_point(module_scope)
