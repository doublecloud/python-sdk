# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/transfer/v1/endpoint/airbyte/google_ads_source.proto
# Protobuf Python Version: 5.27.4
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
    4,
    '',
    'doublecloud/transfer/v1/endpoint/airbyte/google_ads_source.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@doublecloud/transfer/v1/endpoint/airbyte/google_ads_source.proto\x12(doublecloud.transfer.v1.endpoint.airbyte\"\xac\x05\n\x0fGoogleAdsSource\x12\x1f\n\x0b\x63ustomer_id\x18\x01 \x01(\tR\ncustomerId\x12\x1d\n\nstart_date\x18\x02 \x01(\tR\tstartDate\x12\x19\n\x08\x65nd_date\x18\x03 \x01(\tR\x07\x65ndDate\x12l\n\x0e\x63ustom_queries\x18\x04 \x03(\x0b\x32\x45.doublecloud.transfer.v1.endpoint.airbyte.GoogleAdsSource.CustomQueryR\rcustomQueries\x12*\n\x11login_customer_id\x18\x05 \x01(\tR\x0floginCustomerId\x12\x34\n\x16\x63onversion_window_days\x18\x06 \x01(\x01R\x14\x63onversionWindowDays\x12g\n\x0b\x63redentials\x18\x07 \x01(\x0b\x32\x45.doublecloud.transfer.v1.endpoint.airbyte.GoogleAdsSource.CredentialsR\x0b\x63redentials\x1a\xc0\x01\n\x0b\x43redentials\x12\'\n\x0f\x64\x65veloper_token\x18\x01 \x01(\tR\x0e\x64\x65veloperToken\x12\x1b\n\tclient_id\x18\x02 \x01(\tR\x08\x63lientId\x12#\n\rclient_secret\x18\x03 \x01(\tR\x0c\x63lientSecret\x12!\n\x0c\x61\x63\x63\x65ss_token\x18\x04 \x01(\tR\x0b\x61\x63\x63\x65ssToken\x12#\n\rrefresh_token\x18\x05 \x01(\tR\x0crefreshToken\x1a\x42\n\x0b\x43ustomQuery\x12\x14\n\x05query\x18\x01 \x01(\tR\x05query\x12\x1d\n\ntable_name\x18\x02 \x01(\tR\ttableNameB^Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyteb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.airbyte.google_ads_source_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyte'
  _globals['_GOOGLEADSSOURCE']._serialized_start=111
  _globals['_GOOGLEADSSOURCE']._serialized_end=795
  _globals['_GOOGLEADSSOURCE_CREDENTIALS']._serialized_start=535
  _globals['_GOOGLEADSSOURCE_CREDENTIALS']._serialized_end=727
  _globals['_GOOGLEADSSOURCE_CUSTOMQUERY']._serialized_start=729
  _globals['_GOOGLEADSSOURCE_CUSTOMQUERY']._serialized_end=795
# @@protoc_insertion_point(module_scope)
