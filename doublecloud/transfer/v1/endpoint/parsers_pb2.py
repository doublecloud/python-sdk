# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/transfer/v1/endpoint/parsers.proto
# Protobuf Python Version: 5.28.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    0,
    '',
    'doublecloud/transfer/v1/endpoint/parsers.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.transfer.v1.endpoint import common_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.doublecloud/transfer/v1/endpoint/parsers.proto\x12 doublecloud.transfer.v1.endpoint\x1a-doublecloud/transfer/v1/endpoint/common.proto\"\xe5\x04\n\x06Parser\x12X\n\x0bjson_parser\x18\x01 \x01(\x0b\x32\x35.doublecloud.transfer.v1.endpoint.GenericParserCommonH\x00R\njsonParser\x12\x65\n\x13\x64\x65\x62\x65zium_cdc_parser\x18\x05 \x01(\x0b\x32\x33.doublecloud.transfer.v1.endpoint.DebeziumCDCParserH\x00R\x11\x64\x65\x62\x65ziumCdcParser\x12X\n\x0btskv_parser\x18\x06 \x01(\x0b\x32\x35.doublecloud.transfer.v1.endpoint.GenericParserCommonH\x00R\ntskvParser\x12\x8a\x01\n confluent_schema_registry_parser\x18\x07 \x01(\x0b\x32?.doublecloud.transfer.v1.endpoint.ConfluentSchemaRegistryParserH\x00R\x1d\x63onfluentSchemaRegistryParser\x12R\n\x0c\x62lank_parser\x18\t \x01(\x0b\x32-.doublecloud.transfer.v1.endpoint.BlankParserH\x00R\x0b\x62lankParser\x12I\n\traw_table\x18\n \x01(\x0b\x32*.doublecloud.transfer.v1.endpoint.RawTableH\x00R\x08rawTableB\x08\n\x06parserJ\x04\x08\x02\x10\x05J\x04\x08\x08\x10\t\"\xb8\x01\n\x13GenericParserCommon\x12M\n\x0b\x64\x61ta_schema\x18\x01 \x01(\x0b\x32,.doublecloud.transfer.v1.endpoint.DataSchemaR\ndataSchema\x12*\n\x11null_keys_allowed\x18\x02 \x01(\x08R\x0fnullKeysAllowed\x12&\n\x0f\x61\x64\x64_rest_column\x18\x03 \x01(\x08R\raddRestColumn\"\x13\n\x11\x44\x65\x62\x65ziumCDCParser\"\xec\x01\n!ConfluentSchemaRegistryConnection\x12.\n\x13schema_registry_url\x18\x01 \x01(\tR\x11schemaRegistryUrl\x12\x44\n\x08tls_mode\x18\x02 \x01(\x0b\x32).doublecloud.transfer.v1.endpoint.TLSModeR\x07tlsMode\x12Q\n\x04\x61uth\x18\x03 \x01(\x0b\x32=.doublecloud.transfer.v1.endpoint.ConfluentSchemaRegistryAuthR\x04\x61uth\"\x8a\x01\n\x1d\x43onfluentSchemaRegistryParser\x12\x63\n\nconnection\x18\x04 \x01(\x0b\x32\x43.doublecloud.transfer.v1.endpoint.ConfluentSchemaRegistryConnectionR\nconnectionJ\x04\x08\x01\x10\x04\"\xcb\x01\n\x1b\x43onfluentSchemaRegistryAuth\x12\x43\n\x07no_auth\x18\x01 \x01(\x0b\x32(.doublecloud.transfer.v1.endpoint.NoAuthH\x00R\x06noAuth\x12\x45\n\x05\x62\x61sic\x18\x02 \x01(\x0b\x32-.doublecloud.transfer.v1.endpoint.BasicAuthSRH\x00R\x05\x62\x61sicB \n\x1e\x63onfluent_schema_registry_auth\"g\n\x0b\x42\x61sicAuthSR\x12\x12\n\x04user\x18\x01 \x01(\tR\x04user\x12\x44\n\x08password\x18\x02 \x01(\x0b\x32(.doublecloud.transfer.v1.endpoint.SecretR\x08password\"\x84\x03\n\x0bProtoParser\x12J\n\nproto_desc\x18\x01 \x01(\x0b\x32+.doublecloud.transfer.v1.endpoint.ProtoDescR\tprotoDesc\x12\x63\n\x10msg_package_type\x18\x02 \x01(\x0e\x32\x39.doublecloud.transfer.v1.endpoint.ProtoMessagePackageTypeR\x0emsgPackageType\x12\x19\n\x08msg_name\x18\x03 \x01(\tR\x07msgName\x12!\n\x0cprimary_keys\x18\x04 \x03(\tR\x0bprimaryKeys\x12Z\n\x0fincluded_fields\x18\x05 \x01(\x0b\x32\x31.doublecloud.transfer.v1.endpoint.ProtoDataSchemaR\x0eincludedFields\x12*\n\x11null_keys_allowed\x18\x06 \x01(\x08R\x0fnullKeysAllowed\"2\n\tProtoDesc\x12\x1d\n\tdesc_file\x18\x01 \x01(\x0cH\x00R\x08\x64\x65scFileB\x06\n\x04\x64\x65sc\"y\n\x0fProtoDataSchema\x12\\\n\x0f\x63ol_params_list\x18\x01 \x01(\x0b\x32\x32.doublecloud.transfer.v1.endpoint.ColumnParamsListH\x00R\rcolParamsListB\x08\n\x06schema\"a\n\x10\x43olumnParamsList\x12M\n\ncol_params\x18\x01 \x03(\x0b\x32..doublecloud.transfer.v1.endpoint.ColumnParamsR\tcolParams\">\n\x0c\x43olumnParams\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1a\n\x08required\x18\x02 \x01(\x08R\x08required\"\r\n\x0b\x42lankParser\"\xb9\x01\n\x08RawTable\x12$\n\x0evalue_as_bytes\x18\x02 \x01(\x08R\x0cvalueAsBytes\x12\"\n\rkeys_as_bytes\x18\x03 \x01(\x08R\x0bkeysAsBytes\x12#\n\radd_timestamp\x18\x04 \x01(\x08R\x0c\x61\x64\x64Timestamp\x12\x1f\n\x0b\x61\x64\x64_headers\x18\x05 \x01(\x08R\naddHeaders\x12\x17\n\x07\x61\x64\x64_key\x18\x06 \x01(\x08R\x06\x61\x64\x64KeyJ\x04\x08\x01\x10\x02*u\n\x17ProtoMessagePackageType\x12*\n&PROTO_MESSAGE_PACKAGE_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08PROTOSEQ\x10\x01\x12\x0c\n\x08REPEATED\x10\x02\x12\x12\n\x0eSINGLE_MESSAGE\x10\x03\x42NZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.parsers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpoint'
  _globals['_PROTOMESSAGEPACKAGETYPE']._serialized_start=2578
  _globals['_PROTOMESSAGEPACKAGETYPE']._serialized_end=2695
  _globals['_PARSER']._serialized_start=132
  _globals['_PARSER']._serialized_end=745
  _globals['_GENERICPARSERCOMMON']._serialized_start=748
  _globals['_GENERICPARSERCOMMON']._serialized_end=932
  _globals['_DEBEZIUMCDCPARSER']._serialized_start=934
  _globals['_DEBEZIUMCDCPARSER']._serialized_end=953
  _globals['_CONFLUENTSCHEMAREGISTRYCONNECTION']._serialized_start=956
  _globals['_CONFLUENTSCHEMAREGISTRYCONNECTION']._serialized_end=1192
  _globals['_CONFLUENTSCHEMAREGISTRYPARSER']._serialized_start=1195
  _globals['_CONFLUENTSCHEMAREGISTRYPARSER']._serialized_end=1333
  _globals['_CONFLUENTSCHEMAREGISTRYAUTH']._serialized_start=1336
  _globals['_CONFLUENTSCHEMAREGISTRYAUTH']._serialized_end=1539
  _globals['_BASICAUTHSR']._serialized_start=1541
  _globals['_BASICAUTHSR']._serialized_end=1644
  _globals['_PROTOPARSER']._serialized_start=1647
  _globals['_PROTOPARSER']._serialized_end=2035
  _globals['_PROTODESC']._serialized_start=2037
  _globals['_PROTODESC']._serialized_end=2087
  _globals['_PROTODATASCHEMA']._serialized_start=2089
  _globals['_PROTODATASCHEMA']._serialized_end=2210
  _globals['_COLUMNPARAMSLIST']._serialized_start=2212
  _globals['_COLUMNPARAMSLIST']._serialized_end=2309
  _globals['_COLUMNPARAMS']._serialized_start=2311
  _globals['_COLUMNPARAMS']._serialized_end=2373
  _globals['_BLANKPARSER']._serialized_start=2375
  _globals['_BLANKPARSER']._serialized_end=2388
  _globals['_RAWTABLE']._serialized_start=2391
  _globals['_RAWTABLE']._serialized_end=2576
# @@protoc_insertion_point(module_scope)
