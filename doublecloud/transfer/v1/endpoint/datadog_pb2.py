# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/transfer/v1/endpoint/datadog.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.doublecloud/transfer/v1/endpoint/datadog.proto\x12 doublecloud.transfer.v1.endpoint\"\xc6\x02\n\rDatadogTarget\x12$\n\x0e\x63lient_api_key\x18\x01 \x01(\tR\x0c\x63lientApiKey\x12\x12\n\x04host\x18\x02 \x01(\tR\x04host\x12\x64\n\x0e\x63olumn_mapping\x18\x03 \x01(\x0b\x32=.doublecloud.transfer.v1.endpoint.DatadogTarget.ColumnMappingR\rcolumnMapping\x1a\x94\x01\n\rColumnMapping\x12\x16\n\x06source\x18\x01 \x01(\tR\x06source\x12\x12\n\x04tags\x18\x02 \x03(\tR\x04tags\x12\x12\n\x04host\x18\x03 \x01(\tR\x04host\x12)\n\x10message_template\x18\x04 \x01(\tR\x0fmessageTemplate\x12\x18\n\x07service\x18\x05 \x01(\tR\x07serviceBNZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.datadog_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpoint'
  _globals['_DATADOGTARGET']._serialized_start=85
  _globals['_DATADOGTARGET']._serialized_end=411
  _globals['_DATADOGTARGET_COLUMNMAPPING']._serialized_start=263
  _globals['_DATADOGTARGET_COLUMNMAPPING']._serialized_end=411
# @@protoc_insertion_point(module_scope)
