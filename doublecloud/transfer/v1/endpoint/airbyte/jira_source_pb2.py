# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/transfer/v1/endpoint/airbyte/jira_source.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:doublecloud/transfer/v1/endpoint/airbyte/jira_source.proto\x12(doublecloud.transfer.v1.endpoint.airbyte\"\xa1\x03\n\nJiraSource\x12\x1b\n\tapi_token\x18\x01 \x01(\tR\x08\x61piToken\x12\x16\n\x06\x64omain\x18\x02 \x01(\tR\x06\x64omain\x12\x14\n\x05\x65mail\x18\x03 \x01(\tR\x05\x65mail\x12\x1a\n\x08projects\x18\x04 \x03(\tR\x08projects\x12\x1d\n\nstart_date\x18\x05 \x01(\tR\tstartDate\x12v\n\x19issues_stream_expand_with\x18\x06 \x03(\x0e\x32;.doublecloud.transfer.v1.endpoint.airbyte.JiraSource.ExpandR\x16issuesStreamExpandWith\x12>\n\x1b\x65nable_experimental_streams\x18\x07 \x01(\x08R\x19\x65nableExperimentalStreams\"U\n\x06\x45xpand\x12\x16\n\x12\x45XPAND_UNSPECIFIED\x10\x00\x12\x13\n\x0fRENDERED_FIELDS\x10\x01\x12\x0f\n\x0bTRANSITIONS\x10\x02\x12\r\n\tCHANGELOG\x10\x03\x42^Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyteb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.airbyte.jira_source_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyte'
  _globals['_JIRASOURCE']._serialized_start=105
  _globals['_JIRASOURCE']._serialized_end=522
  _globals['_JIRASOURCE_EXPAND']._serialized_start=437
  _globals['_JIRASOURCE_EXPAND']._serialized_end=522
# @@protoc_insertion_point(module_scope)
