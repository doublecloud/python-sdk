# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/transfer/v1/endpoint/airbyte/mssql_source.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;doublecloud/transfer/v1/endpoint/airbyte/mssql_source.proto\x12(doublecloud.transfer.v1.endpoint.airbyte\"\xf1\x07\n\x0bMSSQLSource\x12\x12\n\x04host\x18\x01 \x01(\tR\x04host\x12\x12\n\x04port\x18\x02 \x01(\x03R\x04port\x12\x1a\n\x08\x64\x61tabase\x18\x03 \x01(\tR\x08\x64\x61tabase\x12\x1a\n\x08username\x18\x04 \x01(\tR\x08username\x12\x1a\n\x08password\x18\x05 \x01(\tR\x08password\x12{\n\x12replication_method\x18\x06 \x01(\x0e\x32L.doublecloud.transfer.v1.endpoint.airbyte.MSSQLSource.MSSQLReplicationMethodR\x11replicationMethod\x12^\n\nssl_method\x18\x07 \x01(\x0b\x32?.doublecloud.transfer.v1.endpoint.airbyte.MSSQLSource.SSLConfigR\tsslMethod\x1a\x10\n\x0eSSLUnencrypted\x1a\x15\n\x13SSLEncryptedTrusted\x1aQ\n\x16SSLEncryptedVerifyCert\x12\x37\n\x18host_name_in_certificate\x18\x01 \x01(\tR\x15hostNameInCertificate\x1a\xb1\x03\n\tSSLConfig\x12h\n\x0bunencrypted\x18\x01 \x01(\x0b\x32\x44.doublecloud.transfer.v1.endpoint.airbyte.MSSQLSource.SSLUnencryptedH\x00R\x0bunencrypted\x12\x98\x01\n\"encrypted_trust_server_certificate\x18\x02 \x01(\x0b\x32I.doublecloud.transfer.v1.endpoint.airbyte.MSSQLSource.SSLEncryptedTrustedH\x00R\x1f\x65ncryptedTrustServerCertificate\x12\x90\x01\n\x1c\x65ncrypted_verify_certificate\x18\x03 \x01(\x0b\x32L.doublecloud.transfer.v1.endpoint.airbyte.MSSQLSource.SSLEncryptedVerifyCertH\x00R\x1a\x65ncryptedVerifyCertificateB\x0c\n\nssl_method\"Y\n\x16MSSQLReplicationMethod\x12(\n$MSSQL_REPLICATION_METHOD_UNSPECIFIED\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x07\n\x03\x43\x44\x43\x10\x02\x42^Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyteb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.airbyte.mssql_source_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyte'
  _globals['_MSSQLSOURCE']._serialized_start=106
  _globals['_MSSQLSOURCE']._serialized_end=1115
  _globals['_MSSQLSOURCE_SSLUNENCRYPTED']._serialized_start=466
  _globals['_MSSQLSOURCE_SSLUNENCRYPTED']._serialized_end=482
  _globals['_MSSQLSOURCE_SSLENCRYPTEDTRUSTED']._serialized_start=484
  _globals['_MSSQLSOURCE_SSLENCRYPTEDTRUSTED']._serialized_end=505
  _globals['_MSSQLSOURCE_SSLENCRYPTEDVERIFYCERT']._serialized_start=507
  _globals['_MSSQLSOURCE_SSLENCRYPTEDVERIFYCERT']._serialized_end=588
  _globals['_MSSQLSOURCE_SSLCONFIG']._serialized_start=591
  _globals['_MSSQLSOURCE_SSLCONFIG']._serialized_end=1024
  _globals['_MSSQLSOURCE_MSSQLREPLICATIONMETHOD']._serialized_start=1026
  _globals['_MSSQLSOURCE_MSSQLREPLICATIONMETHOD']._serialized_end=1115
# @@protoc_insertion_point(module_scope)
