# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/transfer/v1/endpoint/mysql.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.transfer.v1.endpoint import common_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,doublecloud/transfer/v1/endpoint/mysql.proto\x12 doublecloud.transfer.v1.endpoint\x1a-doublecloud/transfer/v1/endpoint/common.proto\"\x8c\x01\n\x0eOnPremiseMysql\x12\x12\n\x04port\x18\x02 \x01(\x03R\x04port\x12\x14\n\x05hosts\x18\x05 \x03(\tR\x05hosts\x12\x44\n\x08tls_mode\x18\x06 \x01(\x0b\x32).doublecloud.transfer.v1.endpoint.TLSModeR\x07tlsModeJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x05\"x\n\x0fMysqlConnection\x12Q\n\non_premise\x18\x02 \x01(\x0b\x32\x30.doublecloud.transfer.v1.endpoint.OnPremiseMysqlH\x00R\tonPremiseB\x0c\n\nconnectionJ\x04\x08\x01\x10\x02\"\xd9\x02\n\x1bMysqlObjectTransferSettings\x12I\n\x04view\x18\x01 \x01(\x0e\x32\x35.doublecloud.transfer.v1.endpoint.ObjectTransferStageR\x04view\x12O\n\x07routine\x18\x02 \x01(\x0e\x32\x35.doublecloud.transfer.v1.endpoint.ObjectTransferStageR\x07routine\x12O\n\x07trigger\x18\x03 \x01(\x0e\x32\x35.doublecloud.transfer.v1.endpoint.ObjectTransferStageR\x07trigger\x12M\n\x06tables\x18\x04 \x01(\x0e\x32\x35.doublecloud.transfer.v1.endpoint.ObjectTransferStageR\x06tables\"\x8c\x04\n\x0bMysqlSource\x12Q\n\nconnection\x18\x01 \x01(\x0b\x32\x31.doublecloud.transfer.v1.endpoint.MysqlConnectionR\nconnection\x12\x1a\n\x08\x64\x61tabase\x18\x02 \x01(\tR\x08\x64\x61tabase\x12\x12\n\x04user\x18\x03 \x01(\tR\x04user\x12\x44\n\x08password\x18\x04 \x01(\x0b\x32(.doublecloud.transfer.v1.endpoint.SecretR\x08password\x12\x1a\n\x08timezone\x18\x08 \x01(\tR\x08timezone\x12w\n\x18object_transfer_settings\x18\x0b \x01(\x0b\x32=.doublecloud.transfer.v1.endpoint.MysqlObjectTransferSettingsR\x16objectTransferSettings\x12\x30\n\x14include_tables_regex\x18\x0c \x03(\tR\x12includeTablesRegex\x12\x30\n\x14\x65xclude_tables_regex\x18\r \x03(\tR\x12\x65xcludeTablesRegex\x12)\n\x10service_database\x18\x0f \x01(\tR\x0fserviceDatabaseJ\x04\x08\x05\x10\x08J\x04\x08\t\x10\x0bJ\x04\x08\x0e\x10\x0f\"\xf5\x03\n\x0bMysqlTarget\x12Q\n\nconnection\x18\x01 \x01(\x0b\x32\x31.doublecloud.transfer.v1.endpoint.MysqlConnectionR\nconnection\x12\x1a\n\x08\x64\x61tabase\x18\x02 \x01(\tR\x08\x64\x61tabase\x12\x12\n\x04user\x18\x03 \x01(\tR\x04user\x12\x44\n\x08password\x18\x04 \x01(\x0b\x32(.doublecloud.transfer.v1.endpoint.SecretR\x08password\x12\x19\n\x08sql_mode\x18\x05 \x01(\tR\x07sqlMode\x12\x34\n\x16skip_constraint_checks\x18\x06 \x01(\x08R\x14skipConstraintChecks\x12\x1a\n\x08timezone\x18\x07 \x01(\tR\x08timezone\x12V\n\x0e\x63leanup_policy\x18\x08 \x01(\x0e\x32/.doublecloud.transfer.v1.endpoint.CleanupPolicyR\rcleanupPolicy\x12)\n\x10service_database\x18\x0f \x01(\tR\x0fserviceDatabase\x12\'\n\x0fsecurity_groups\x18\x10 \x03(\tR\x0esecurityGroupsJ\x04\x08\t\x10\x0f\x42NZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpointb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.mysql_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint;endpoint'
  _globals['_ONPREMISEMYSQL']._serialized_start=130
  _globals['_ONPREMISEMYSQL']._serialized_end=270
  _globals['_MYSQLCONNECTION']._serialized_start=272
  _globals['_MYSQLCONNECTION']._serialized_end=392
  _globals['_MYSQLOBJECTTRANSFERSETTINGS']._serialized_start=395
  _globals['_MYSQLOBJECTTRANSFERSETTINGS']._serialized_end=740
  _globals['_MYSQLSOURCE']._serialized_start=743
  _globals['_MYSQLSOURCE']._serialized_end=1267
  _globals['_MYSQLTARGET']._serialized_start=1270
  _globals['_MYSQLTARGET']._serialized_end=1771
# @@protoc_insertion_point(module_scope)
