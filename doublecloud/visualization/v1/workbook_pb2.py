# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/visualization/v1/workbook.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+doublecloud/visualization/v1/workbook.proto\x12\x1c\x64oublecloud.visualization.v1\x1a\x1cgoogle/protobuf/struct.proto\"%\n\x0bPlainSecret\x12\x16\n\x06secret\x18\x01 \x01(\tR\x06secret\"b\n\x06Secret\x12N\n\x0cplain_secret\x18\x01 \x01(\x0b\x32).doublecloud.visualization.v1.PlainSecretH\x00R\x0bplainSecretB\x08\n\x06secret\":\n\x08Workbook\x12.\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x16.google.protobuf.ValueR\x06\x63onfig\"9\n\x07\x44\x61taset\x12.\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x16.google.protobuf.ValueR\x06\x63onfig\"<\n\nConnection\x12.\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x16.google.protobuf.ValueR\x06\x63onfig\":\n\x12WorkbooksIndexItem\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x14\n\x05title\x18\x02 \x01(\tR\x05titleBOZMgithub.com/doublecloud/go-genproto/doublecloud/visualization/v1;visualizationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.visualization.v1.workbook_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZMgithub.com/doublecloud/go-genproto/doublecloud/visualization/v1;visualization'
  _globals['_PLAINSECRET']._serialized_start=107
  _globals['_PLAINSECRET']._serialized_end=144
  _globals['_SECRET']._serialized_start=146
  _globals['_SECRET']._serialized_end=244
  _globals['_WORKBOOK']._serialized_start=246
  _globals['_WORKBOOK']._serialized_end=304
  _globals['_DATASET']._serialized_start=306
  _globals['_DATASET']._serialized_end=363
  _globals['_CONNECTION']._serialized_start=365
  _globals['_CONNECTION']._serialized_end=425
  _globals['_WORKBOOKSINDEXITEM']._serialized_start=427
  _globals['_WORKBOOKSINDEXITEM']._serialized_end=485
# @@protoc_insertion_point(module_scope)
