# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/transfer/v1/endpoint/airbyte/s3_source.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8doublecloud/transfer/v1/endpoint/airbyte/s3_source.proto\x12(doublecloud.transfer.v1.endpoint.airbyte\"\xc9\r\n\x08S3Source\x12\x18\n\x07\x64\x61taset\x18\x01 \x01(\tR\x07\x64\x61taset\x12!\n\x0cpath_pattern\x18\x02 \x01(\tR\x0bpathPattern\x12\x16\n\x06schema\x18\x03 \x01(\tR\x06schema\x12Q\n\x06\x66ormat\x18\x05 \x01(\x0b\x32\x39.doublecloud.transfer.v1.endpoint.airbyte.S3Source.FormatR\x06\x66ormat\x12W\n\x08provider\x18\x06 \x01(\x0b\x32;.doublecloud.transfer.v1.endpoint.airbyte.S3Source.ProviderR\x08provider\x1a\xd7\x02\n\x06\x46ormat\x12J\n\x03\x63sv\x18\x04 \x01(\x0b\x32\x36.doublecloud.transfer.v1.endpoint.airbyte.S3Source.CsvH\x00R\x03\x63sv\x12V\n\x07parquet\x18\x05 \x01(\x0b\x32:.doublecloud.transfer.v1.endpoint.airbyte.S3Source.ParquetH\x00R\x07parquet\x12M\n\x04\x61vro\x18\x06 \x01(\x0b\x32\x37.doublecloud.transfer.v1.endpoint.airbyte.S3Source.AvroH\x00R\x04\x61vro\x12P\n\x05jsonl\x18\x07 \x01(\x0b\x32\x38.doublecloud.transfer.v1.endpoint.airbyte.S3Source.JsonlH\x00R\x05jsonlB\x08\n\x06\x66ormat\x1a\xfe\x01\n\x08Provider\x12\x16\n\x06\x62ucket\x18\x01 \x01(\tR\x06\x62ucket\x12)\n\x11\x61ws_access_key_id\x18\x02 \x01(\tR\x0e\x61wsAccessKeyId\x12\x31\n\x15\x61ws_secret_access_key\x18\x03 \x01(\tR\x12\x61wsSecretAccessKey\x12\x1f\n\x0bpath_prefix\x18\x04 \x01(\tR\npathPrefix\x12\x1a\n\x08\x65ndpoint\x18\x05 \x01(\tR\x08\x65ndpoint\x12\x17\n\x07use_ssl\x18\x06 \x01(\x08R\x06useSsl\x12&\n\x0fverify_ssl_cert\x18\x07 \x01(\x08R\rverifySslCert\x1a\xd6\x02\n\x03\x43sv\x12\x1c\n\tdelimiter\x18\x02 \x01(\tR\tdelimiter\x12\x1d\n\nquote_char\x18\x03 \x01(\tR\tquoteChar\x12\x1f\n\x0b\x65scape_char\x18\x04 \x01(\tR\nescapeChar\x12\x1a\n\x08\x65ncoding\x18\x05 \x01(\tR\x08\x65ncoding\x12!\n\x0c\x64ouble_quote\x18\x06 \x01(\x08R\x0b\x64oubleQuote\x12,\n\x12newlines_in_values\x18\x07 \x01(\x08R\x10newlinesInValues\x12\x1d\n\nblock_size\x18\x08 \x01(\x03R\tblockSize\x12:\n\x19\x61\x64\x64itional_reader_options\x18\t \x01(\tR\x17\x61\x64\x64itionalReaderOptions\x12)\n\x10\x61\x64vanced_options\x18\n \x01(\tR\x0f\x61\x64vancedOptions\x1a\x06\n\x04\x41vro\x1a\x9a\x03\n\x05Jsonl\x12,\n\x12newlines_in_values\x18\x02 \x01(\x08R\x10newlinesInValues\x12\x8c\x01\n\x19unexpected_field_behavior\x18\x03 \x01(\x0e\x32P.doublecloud.transfer.v1.endpoint.airbyte.S3Source.Jsonl.UnexpectedFieldBehaviorR\x17unexpectedFieldBehavior\x12\x1d\n\nblock_size\x18\x04 \x01(\x03R\tblockSize\"\xb4\x01\n\x17UnexpectedFieldBehavior\x12)\n%UNEXPECTED_FIELD_BEHAVIOR_UNSPECIFIED\x10\x00\x12$\n UNEXPECTED_FIELD_BEHAVIOR_IGNORE\x10\x01\x12#\n\x1fUNEXPECTED_FIELD_BEHAVIOR_INFER\x10\x02\x12#\n\x1fUNEXPECTED_FIELD_BEHAVIOR_ERROR\x10\x03\x1a\x63\n\x07Parquet\x12\x1f\n\x0b\x62uffer_size\x18\x02 \x01(\x03R\nbufferSize\x12\x18\n\x07\x63olumns\x18\x03 \x03(\tR\x07\x63olumns\x12\x1d\n\nbatch_size\x18\x04 \x01(\x03R\tbatchSizeB^Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyteb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.airbyte.s3_source_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyte'
  _globals['_S3SOURCE']._serialized_start=103
  _globals['_S3SOURCE']._serialized_end=1840
  _globals['_S3SOURCE_FORMAT']._serialized_start=373
  _globals['_S3SOURCE_FORMAT']._serialized_end=716
  _globals['_S3SOURCE_PROVIDER']._serialized_start=719
  _globals['_S3SOURCE_PROVIDER']._serialized_end=973
  _globals['_S3SOURCE_CSV']._serialized_start=976
  _globals['_S3SOURCE_CSV']._serialized_end=1318
  _globals['_S3SOURCE_AVRO']._serialized_start=1320
  _globals['_S3SOURCE_AVRO']._serialized_end=1326
  _globals['_S3SOURCE_JSONL']._serialized_start=1329
  _globals['_S3SOURCE_JSONL']._serialized_end=1739
  _globals['_S3SOURCE_JSONL_UNEXPECTEDFIELDBEHAVIOR']._serialized_start=1559
  _globals['_S3SOURCE_JSONL_UNEXPECTEDFIELDBEHAVIOR']._serialized_end=1739
  _globals['_S3SOURCE_PARQUET']._serialized_start=1741
  _globals['_S3SOURCE_PARQUET']._serialized_end=1840
# @@protoc_insertion_point(module_scope)
