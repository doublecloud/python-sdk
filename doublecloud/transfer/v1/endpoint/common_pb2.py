# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/transfer/v1/endpoint/common.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-doublecloud/transfer/v1/endpoint/common.proto\x12 doublecloud.transfer.v1.endpoint\x1a\x1bgoogle/protobuf/empty.proto\"?\n\x07\x41ltName\x12\x1b\n\tfrom_name\x18\x01 \x01(\tR\x08\x66romName\x12\x17\n\x07to_name\x18\x02 \x01(\tR\x06toName\"%\n\x06Secret\x12\x12\n\x03raw\x18\x01 \x01(\tH\x00R\x03rawB\x07\n\x05value\"\xa3\x01\n\tColSchema\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12@\n\x04type\x18\x02 \x01(\x0e\x32,.doublecloud.transfer.v1.endpoint.ColumnTypeR\x04type\x12\x10\n\x03key\x18\x03 \x01(\x08R\x03key\x12\x1a\n\x08required\x18\x04 \x01(\x08R\x08required\x12\x12\n\x04path\x18\x05 \x01(\tR\x04path\"\x94\x01\n\x07TLSMode\x12\x34\n\x08\x64isabled\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00R\x08\x64isabled\x12G\n\x07\x65nabled\x18\x02 \x01(\x0b\x32+.doublecloud.transfer.v1.endpoint.TLSConfigH\x00R\x07\x65nabledB\n\n\x08tls_mode\"2\n\tTLSConfig\x12%\n\x0e\x63\x61_certificate\x18\x01 \x01(\tR\rcaCertificate\";\n\x0b\x43olumnValue\x12#\n\x0cstring_value\x18\x01 \x01(\tH\x00R\x0bstringValueB\x07\n\x05value\"5\n\x0bHeaderValue\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"\xef\x02\n\x19\x44\x61taTransformationOptions\x12%\n\x0e\x63loud_function\x18\x01 \x01(\tR\rcloudFunction\x12*\n\x11number_of_retries\x18\x02 \x01(\x03R\x0fnumberOfRetries\x12\x1f\n\x0b\x62uffer_size\x18\x03 \x01(\tR\nbufferSize\x12\x32\n\x15\x62uffer_flush_interval\x18\x04 \x01(\tR\x13\x62ufferFlushInterval\x12-\n\x12invocation_timeout\x18\x05 \x01(\tR\x11invocationTimeout\x12,\n\x12\x63loud_function_url\x18\t \x01(\tR\x10\x63loudFunctionUrl\x12G\n\x07headers\x18\n \x03(\x0b\x32-.doublecloud.transfer.v1.endpoint.HeaderValueR\x07headersJ\x04\x08\x06\x10\t\"V\n\tFieldList\x12\x43\n\x06\x66ields\x18\x02 \x03(\x0b\x32+.doublecloud.transfer.v1.endpoint.ColSchemaR\x06\x66ieldsJ\x04\x08\x01\x10\x02\"\x80\x01\n\nDataSchema\x12!\n\x0bjson_fields\x18\x01 \x01(\tH\x00R\njsonFields\x12\x45\n\x06\x66ields\x18\x02 \x01(\x0b\x32+.doublecloud.transfer.v1.endpoint.FieldListH\x00R\x06\x66ieldsB\x08\n\x06schema\"\x08\n\x06NoAuth*h\n\x13ObjectTransferStage\x12%\n!OBJECT_TRANSFER_STAGE_UNSPECIFIED\x10\x00\x12\x0f\n\x0b\x42\x45\x46ORE_DATA\x10\x01\x12\x0e\n\nAFTER_DATA\x10\x02\x12\t\n\x05NEVER\x10\x03*U\n\rCleanupPolicy\x12\x1e\n\x1a\x43LEANUP_POLICY_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x44ISABLED\x10\x01\x12\x08\n\x04\x44ROP\x10\x02\x12\x0c\n\x08TRUNCATE\x10\x03*\xc9\x01\n\nColumnType\x12\x1b\n\x17\x43OLUMN_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05INT32\x10\x01\x12\t\n\x05INT16\x10\x02\x12\x08\n\x04INT8\x10\x03\x12\n\n\x06UINT64\x10\x04\x12\n\n\x06UINT32\x10\x05\x12\n\n\x06UINT16\x10\x06\x12\t\n\x05UINT8\x10\x07\x12\n\n\x06\x44OUBLE\x10\x08\x12\x0b\n\x07\x42OOLEAN\x10\t\x12\n\n\x06STRING\x10\n\x12\x08\n\x04UTF8\x10\x0b\x12\x07\n\x03\x41NY\x10\x0c\x12\x0c\n\x08\x44\x41TETIME\x10\r\x12\t\n\x05INT64\x10\x0e\x42NZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.common_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpoint'
  _globals['_OBJECTTRANSFERSTAGE']._serialized_start=1300
  _globals['_OBJECTTRANSFERSTAGE']._serialized_end=1404
  _globals['_CLEANUPPOLICY']._serialized_start=1406
  _globals['_CLEANUPPOLICY']._serialized_end=1491
  _globals['_COLUMNTYPE']._serialized_start=1494
  _globals['_COLUMNTYPE']._serialized_end=1695
  _globals['_ALTNAME']._serialized_start=112
  _globals['_ALTNAME']._serialized_end=175
  _globals['_SECRET']._serialized_start=177
  _globals['_SECRET']._serialized_end=214
  _globals['_COLSCHEMA']._serialized_start=217
  _globals['_COLSCHEMA']._serialized_end=380
  _globals['_TLSMODE']._serialized_start=383
  _globals['_TLSMODE']._serialized_end=531
  _globals['_TLSCONFIG']._serialized_start=533
  _globals['_TLSCONFIG']._serialized_end=583
  _globals['_COLUMNVALUE']._serialized_start=585
  _globals['_COLUMNVALUE']._serialized_end=644
  _globals['_HEADERVALUE']._serialized_start=646
  _globals['_HEADERVALUE']._serialized_end=699
  _globals['_DATATRANSFORMATIONOPTIONS']._serialized_start=702
  _globals['_DATATRANSFORMATIONOPTIONS']._serialized_end=1069
  _globals['_FIELDLIST']._serialized_start=1071
  _globals['_FIELDLIST']._serialized_end=1157
  _globals['_DATASCHEMA']._serialized_start=1160
  _globals['_DATASCHEMA']._serialized_end=1288
  _globals['_NOAUTH']._serialized_start=1290
  _globals['_NOAUTH']._serialized_end=1298
# @@protoc_insertion_point(module_scope)
