# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/transfer/v1/endpoint/object_storage.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'doublecloud/transfer/v1/endpoint/object_storage.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from doublecloud.transfer.v1.endpoint import common_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_common__pb2
from doublecloud.transfer.v1.endpoint import parsers_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_parsers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5doublecloud/transfer/v1/endpoint/object_storage.proto\x12 doublecloud.transfer.v1.endpoint\x1a\x1bgoogle/protobuf/empty.proto\x1a-doublecloud/transfer/v1/endpoint/common.proto\x1a.doublecloud/transfer/v1/endpoint/parsers.proto\"\xf2\x01\n\x17ObjectStorageConnection\x12)\n\x11\x61ws_access_key_id\x18\x03 \x01(\tR\x0e\x61wsAccessKeyId\x12\x31\n\x15\x61ws_secret_access_key\x18\x04 \x01(\tR\x12\x61wsSecretAccessKey\x12\x16\n\x06region\x18\x05 \x01(\tR\x06region\x12\x1a\n\x08\x65ndpoint\x18\x06 \x01(\tR\x08\x65ndpoint\x12\x17\n\x07use_ssl\x18\x07 \x01(\x08R\x06useSsl\x12&\n\x0fverify_ssl_cert\x18\x08 \x01(\x08R\rverifySslCertJ\x04\x08\x01\x10\x03\"C\n\x1dObjectStorageSerializerConfig\x12\"\n\rany_as_string\x18\x01 \x01(\x08R\x0b\x61nyAsString\"\xc9\x05\n\x13ObjectStorageTarget\x12\x16\n\x06\x62ucket\x18\x01 \x01(\tR\x06\x62ucket\x12g\n\routput_format\x18\x04 \x01(\x0e\x32\x42.doublecloud.transfer.v1.endpoint.ObjectStorageSerializationFormatR\x0coutputFormat\x12#\n\rbucket_layout\x18\x05 \x01(\tR\x0c\x62ucketLayout\x12\x1f\n\x0b\x62uffer_size\x18\x06 \x01(\tR\nbufferSize\x12\'\n\x0f\x62uffer_interval\x18\x07 \x01(\tR\x0e\x62ufferInterval\x12,\n\x12service_account_id\x18\x08 \x01(\tR\x10serviceAccountId\x12]\n\x0foutput_encoding\x18\t \x01(\x0e\x32\x34.doublecloud.transfer.v1.endpoint.ObjectStorageCodecR\x0eoutputEncoding\x12Y\n\nconnection\x18\n \x01(\x0b\x32\x39.doublecloud.transfer.v1.endpoint.ObjectStorageConnectionR\nconnection\x12\x34\n\x16\x62ucket_layout_timezone\x18\x0b \x01(\tR\x14\x62ucketLayoutTimezone\x12\x30\n\x14\x62ucket_layout_column\x18\x0c \x01(\tR\x12\x62ucketLayoutColumn\x12l\n\x11serializer_config\x18\r \x01(\x0b\x32?.doublecloud.transfer.v1.endpoint.ObjectStorageSerializerConfigR\x10serializerConfigJ\x04\x08\x02\x10\x04\"\xa3\x02\n\x15ObjectStorageProvider\x12\x16\n\x06\x62ucket\x18\x01 \x01(\tR\x06\x62ucket\x12)\n\x11\x61ws_access_key_id\x18\x02 \x01(\tR\x0e\x61wsAccessKeyId\x12\x31\n\x15\x61ws_secret_access_key\x18\x03 \x01(\tR\x12\x61wsSecretAccessKey\x12\x1f\n\x0bpath_prefix\x18\x04 \x01(\tR\npathPrefix\x12\x1a\n\x08\x65ndpoint\x18\x05 \x01(\tR\x08\x65ndpoint\x12\x17\n\x07use_ssl\x18\x06 \x01(\x08R\x06useSsl\x12&\n\x0fverify_ssl_cert\x18\x07 \x01(\x08R\rverifySslCert\x12\x16\n\x06region\x18\x08 \x01(\tR\x06region\"\xf9\x0f\n\x19ObjectStorageReaderFormat\x12S\n\x03\x63sv\x18\x04 \x01(\x0b\x32?.doublecloud.transfer.v1.endpoint.ObjectStorageReaderFormat.CsvH\x00R\x03\x63sv\x12_\n\x07parquet\x18\x05 \x01(\x0b\x32\x43.doublecloud.transfer.v1.endpoint.ObjectStorageReaderFormat.ParquetH\x00R\x07parquet\x12V\n\x04\x61vro\x18\x06 \x01(\x0b\x32@.doublecloud.transfer.v1.endpoint.ObjectStorageReaderFormat.AvroH\x00R\x04\x61vro\x12Y\n\x05jsonl\x18\x07 \x01(\x0b\x32\x41.doublecloud.transfer.v1.endpoint.ObjectStorageReaderFormat.JsonlH\x00R\x05jsonl\x12\x45\n\x05proto\x18\x08 \x01(\x0b\x32-.doublecloud.transfer.v1.endpoint.ProtoParserH\x00R\x05proto\x1a\xa9\x03\n\x05Jsonl\x12,\n\x12newlines_in_values\x18\x02 \x01(\x08R\x10newlinesInValues\x12\x95\x01\n\x19unexpected_field_behavior\x18\x03 \x01(\x0e\x32Y.doublecloud.transfer.v1.endpoint.ObjectStorageReaderFormat.Jsonl.UnexpectedFieldBehaviorR\x17unexpectedFieldBehavior\x12\x1d\n\nblock_size\x18\x04 \x01(\x03R\tblockSize\"\xb4\x01\n\x17UnexpectedFieldBehavior\x12)\n%UNEXPECTED_FIELD_BEHAVIOR_UNSPECIFIED\x10\x00\x12$\n UNEXPECTED_FIELD_BEHAVIOR_IGNORE\x10\x01\x12#\n\x1fUNEXPECTED_FIELD_BEHAVIOR_INFER\x10\x02\x12#\n\x1fUNEXPECTED_FIELD_BEHAVIOR_ERROR\x10\x03J\x04\x08\x01\x10\x02\x1a\xdc\x08\n\x03\x43sv\x12\x1c\n\tdelimiter\x18\x02 \x01(\tR\tdelimiter\x12\x1d\n\nquote_char\x18\x03 \x01(\tR\tquoteChar\x12\x1f\n\x0b\x65scape_char\x18\x04 \x01(\tR\nescapeChar\x12\x1a\n\x08\x65ncoding\x18\x05 \x01(\tR\x08\x65ncoding\x12!\n\x0c\x64ouble_quote\x18\x06 \x01(\x08R\x0b\x64oubleQuote\x12,\n\x12newlines_in_values\x18\x07 \x01(\x08R\x10newlinesInValues\x12\x1d\n\nblock_size\x18\x08 \x01(\x03R\tblockSize\x12z\n\x10\x61\x64vanced_options\x18\t \x01(\x0b\x32O.doublecloud.transfer.v1.endpoint.ObjectStorageReaderFormat.Csv.AdvancedOptionsR\x0f\x61\x64vancedOptions\x12\x86\x01\n\x12\x61\x64\x64itional_options\x18\n \x01(\x0b\x32W.doublecloud.transfer.v1.endpoint.ObjectStorageReaderFormat.Csv.AdditionalReaderOptionsR\x11\x61\x64\x64itionalOptions\x1a\xc0\x01\n\x0f\x41\x64vancedOptions\x12\x1b\n\tskip_rows\x18\x01 \x01(\x03R\x08skipRows\x12\x31\n\x15skip_rows_after_names\x18\x02 \x01(\x03R\x12skipRowsAfterNames\x12:\n\x19\x61utogenerate_column_names\x18\x03 \x01(\x08R\x17\x61utogenerateColumnNames\x12!\n\x0c\x63olumn_names\x18\x04 \x03(\tR\x0b\x63olumnNames\x1a\x9c\x03\n\x17\x41\x64\x64itionalReaderOptions\x12\x1f\n\x0bnull_values\x18\x01 \x03(\tR\nnullValues\x12\x1f\n\x0btrue_values\x18\x02 \x03(\tR\ntrueValues\x12!\n\x0c\x66\x61lse_values\x18\x03 \x03(\tR\x0b\x66\x61lseValues\x12#\n\rdecimal_point\x18\x04 \x01(\tR\x0c\x64\x65\x63imalPoint\x12-\n\x13strings_can_be_null\x18\x05 \x01(\x08R\x10stringsCanBeNull\x12:\n\x1aquoted_strings_can_be_null\x18\x06 \x01(\x08R\x16quotedStringsCanBeNull\x12\'\n\x0finclude_columns\x18\x07 \x03(\tR\x0eincludeColumns\x12\x36\n\x17include_missing_columns\x18\x08 \x01(\x08R\x15includeMissingColumns\x12+\n\x11timestamp_parsers\x18\t \x03(\tR\x10timestampParsersJ\x04\x08\x01\x10\x02\x1a\x06\n\x04\x41vro\x1a\t\n\x07ParquetB\x08\n\x06\x66ormatJ\x04\x08\x01\x10\x04\"\xa4\x01\n\x17ObjectStorageDataSchema\x12.\n\x05infer\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00R\x05infer\x12O\n\x0b\x64\x61ta_schema\x18\x02 \x01(\x0b\x32,.doublecloud.transfer.v1.endpoint.DataSchemaH\x00R\ndataSchemaB\x08\n\x06schema\"\x8a\x01\n\x18ObjectStorageResultTable\x12\'\n\x0ftable_namespace\x18\x01 \x01(\tR\x0etableNamespace\x12\x1d\n\ntable_name\x18\x02 \x01(\tR\ttableName\x12&\n\x0f\x61\x64\x64_system_cols\x18\x03 \x01(\x08R\raddSystemCols\"\x83\x01\n#ObjectStorageSourceAdvancedSettings\x12\\\n\runparsed_mode\x18\x01 \x01(\x0e\x32\x37.doublecloud.transfer.v1.endpoint.ObjectStorageUnparsedR\x0cunparsedMode\"\xd0\x04\n\x18ObjectStorageEventSource\x12R\n\x03sqs\x18\x01 \x01(\x0b\x32>.doublecloud.transfer.v1.endpoint.ObjectStorageEventSource.SQSH\x00R\x03sqs\x12R\n\x03sns\x18\x02 \x01(\x0b\x32>.doublecloud.transfer.v1.endpoint.ObjectStorageEventSource.SNSH\x00R\x03sns\x12\\\n\x07pub_sub\x18\x03 \x01(\x0b\x32\x41.doublecloud.transfer.v1.endpoint.ObjectStorageEventSource.PubSubH\x00R\x06pubSub\x1a\x92\x02\n\x03SQS\x12\x1d\n\nqueue_name\x18\x01 \x01(\tR\tqueueName\x12\x19\n\x08owner_id\x18\x02 \x01(\tR\x07ownerId\x12)\n\x11\x61ws_access_key_id\x18\x03 \x01(\tR\x0e\x61wsAccessKeyId\x12\x31\n\x15\x61ws_secret_access_key\x18\x04 \x01(\tR\x12\x61wsSecretAccessKey\x12\x1a\n\x08\x65ndpoint\x18\x05 \x01(\tR\x08\x65ndpoint\x12\x16\n\x06region\x18\x06 \x01(\tR\x06region\x12\x17\n\x07use_ssl\x18\x07 \x01(\x08R\x06useSsl\x12&\n\x0fverify_ssl_cert\x18\x08 \x01(\x08R\rverifySslCert\x1a\x05\n\x03SNS\x1a\x08\n\x06PubSubB\x08\n\x06source\"\xf4\x04\n\x13ObjectStorageSource\x12S\n\x08provider\x18\x01 \x01(\x0b\x32\x37.doublecloud.transfer.v1.endpoint.ObjectStorageProviderR\x08provider\x12S\n\x06\x66ormat\x18\x02 \x01(\x0b\x32;.doublecloud.transfer.v1.endpoint.ObjectStorageReaderFormatR\x06\x66ormat\x12!\n\x0cpath_pattern\x18\x03 \x01(\tR\x0bpathPattern\x12]\n\x0cresult_table\x18\x04 \x01(\x0b\x32:.doublecloud.transfer.v1.endpoint.ObjectStorageResultTableR\x0bresultTable\x12^\n\rresult_schema\x18\x05 \x01(\x0b\x32\x39.doublecloud.transfer.v1.endpoint.ObjectStorageDataSchemaR\x0cresultSchema\x12]\n\x0c\x65vent_source\x18\x06 \x01(\x0b\x32:.doublecloud.transfer.v1.endpoint.ObjectStorageEventSourceR\x0b\x65ventSource\x12r\n\x11\x61\x64vanced_settings\x18\x07 \x01(\x0b\x32\x45.doublecloud.transfer.v1.endpoint.ObjectStorageSourceAdvancedSettingsR\x10\x61\x64vancedSettings*V\n\x12ObjectStorageCodec\x12$\n OBJECT_STORAGE_CODEC_UNSPECIFIED\x10\x00\x12\x10\n\x0cUNCOMPRESSED\x10\x01\x12\x08\n\x04GZIP\x10\x02*\x90\x02\n ObjectStorageSerializationFormat\x12\x33\n/OBJECT_STORAGE_SERIALIZATION_FORMAT_UNSPECIFIED\x10\x00\x12,\n(OBJECT_STORAGE_SERIALIZATION_FORMAT_JSON\x10\x01\x12+\n\'OBJECT_STORAGE_SERIALIZATION_FORMAT_CSV\x10\x02\x12+\n\'OBJECT_STORAGE_SERIALIZATION_FORMAT_RAW\x10\x03\x12/\n+OBJECT_STORAGE_SERIALIZATION_FORMAT_PARQUET\x10\x04*\xab\x01\n\x15ObjectStorageUnparsed\x12\'\n#OBJECT_STORAGE_UNPARSED_UNSPECIFIED\x10\x00\x12!\n\x1dOBJECT_STORAGE_UNPARSED_RETRY\x10\x01\x12 \n\x1cOBJECT_STORAGE_UNPARSED_FAIL\x10\x02\x12$\n OBJECT_STORAGE_UNPARSED_CONTINUE\x10\x03\x42NZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.object_storage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpoint'
  _globals['_OBJECTSTORAGECODEC']._serialized_start=5251
  _globals['_OBJECTSTORAGECODEC']._serialized_end=5337
  _globals['_OBJECTSTORAGESERIALIZATIONFORMAT']._serialized_start=5340
  _globals['_OBJECTSTORAGESERIALIZATIONFORMAT']._serialized_end=5612
  _globals['_OBJECTSTORAGEUNPARSED']._serialized_start=5615
  _globals['_OBJECTSTORAGEUNPARSED']._serialized_end=5786
  _globals['_OBJECTSTORAGECONNECTION']._serialized_start=216
  _globals['_OBJECTSTORAGECONNECTION']._serialized_end=458
  _globals['_OBJECTSTORAGESERIALIZERCONFIG']._serialized_start=460
  _globals['_OBJECTSTORAGESERIALIZERCONFIG']._serialized_end=527
  _globals['_OBJECTSTORAGETARGET']._serialized_start=530
  _globals['_OBJECTSTORAGETARGET']._serialized_end=1243
  _globals['_OBJECTSTORAGEPROVIDER']._serialized_start=1246
  _globals['_OBJECTSTORAGEPROVIDER']._serialized_end=1537
  _globals['_OBJECTSTORAGEREADERFORMAT']._serialized_start=1540
  _globals['_OBJECTSTORAGEREADERFORMAT']._serialized_end=3581
  _globals['_OBJECTSTORAGEREADERFORMAT_JSONL']._serialized_start=2002
  _globals['_OBJECTSTORAGEREADERFORMAT_JSONL']._serialized_end=2427
  _globals['_OBJECTSTORAGEREADERFORMAT_JSONL_UNEXPECTEDFIELDBEHAVIOR']._serialized_start=2241
  _globals['_OBJECTSTORAGEREADERFORMAT_JSONL_UNEXPECTEDFIELDBEHAVIOR']._serialized_end=2421
  _globals['_OBJECTSTORAGEREADERFORMAT_CSV']._serialized_start=2430
  _globals['_OBJECTSTORAGEREADERFORMAT_CSV']._serialized_end=3546
  _globals['_OBJECTSTORAGEREADERFORMAT_CSV_ADVANCEDOPTIONS']._serialized_start=2933
  _globals['_OBJECTSTORAGEREADERFORMAT_CSV_ADVANCEDOPTIONS']._serialized_end=3125
  _globals['_OBJECTSTORAGEREADERFORMAT_CSV_ADDITIONALREADEROPTIONS']._serialized_start=3128
  _globals['_OBJECTSTORAGEREADERFORMAT_CSV_ADDITIONALREADEROPTIONS']._serialized_end=3540
  _globals['_OBJECTSTORAGEREADERFORMAT_AVRO']._serialized_start=3548
  _globals['_OBJECTSTORAGEREADERFORMAT_AVRO']._serialized_end=3554
  _globals['_OBJECTSTORAGEREADERFORMAT_PARQUET']._serialized_start=3556
  _globals['_OBJECTSTORAGEREADERFORMAT_PARQUET']._serialized_end=3565
  _globals['_OBJECTSTORAGEDATASCHEMA']._serialized_start=3584
  _globals['_OBJECTSTORAGEDATASCHEMA']._serialized_end=3748
  _globals['_OBJECTSTORAGERESULTTABLE']._serialized_start=3751
  _globals['_OBJECTSTORAGERESULTTABLE']._serialized_end=3889
  _globals['_OBJECTSTORAGESOURCEADVANCEDSETTINGS']._serialized_start=3892
  _globals['_OBJECTSTORAGESOURCEADVANCEDSETTINGS']._serialized_end=4023
  _globals['_OBJECTSTORAGEEVENTSOURCE']._serialized_start=4026
  _globals['_OBJECTSTORAGEEVENTSOURCE']._serialized_end=4618
  _globals['_OBJECTSTORAGEEVENTSOURCE_SQS']._serialized_start=4317
  _globals['_OBJECTSTORAGEEVENTSOURCE_SQS']._serialized_end=4591
  _globals['_OBJECTSTORAGEEVENTSOURCE_SNS']._serialized_start=4593
  _globals['_OBJECTSTORAGEEVENTSOURCE_SNS']._serialized_end=4598
  _globals['_OBJECTSTORAGEEVENTSOURCE_PUBSUB']._serialized_start=4600
  _globals['_OBJECTSTORAGEEVENTSOURCE_PUBSUB']._serialized_end=4608
  _globals['_OBJECTSTORAGESOURCE']._serialized_start=4621
  _globals['_OBJECTSTORAGESOURCE']._serialized_end=5249
# @@protoc_insertion_point(module_scope)
