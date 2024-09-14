# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/kafka/v1/connector.proto
# Protobuf Python Version: 5.28.1
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
    1,
    '',
    'doublecloud/kafka/v1/connector.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$doublecloud/kafka/v1/connector.proto\x12\x14\x64oublecloud.kafka.v1\x1a\x1egoogle/protobuf/wrappers.proto\"\xf1\x03\n\rConnectorSpec\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x38\n\ttasks_max\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x08tasksMax\x12S\n\nproperties\x18\x03 \x03(\x0b\x32\x33.doublecloud.kafka.v1.ConnectorSpec.PropertiesEntryR\nproperties\x12x\n\x1c\x63onnector_config_mirrormaker\x18\n \x01(\x0b\x32\x34.doublecloud.kafka.v1.ConnectorConfigMirrorMakerSpecH\x00R\x1a\x63onnectorConfigMirrormaker\x12j\n\x18\x63onnector_config_s3_sink\x18\x0b \x01(\x0b\x32/.doublecloud.kafka.v1.ConnectorConfigS3SinkSpecH\x00R\x15\x63onnectorConfigS3Sink\x1a=\n\x0fPropertiesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x12\n\x10\x63onnector_configJ\x04\x08\x04\x10\n\"\xf7\x04\n\x13UpdateConnectorSpec\x12\x38\n\ttasks_max\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x08tasksMax\x12Z\n\nproperties\x18\x02 \x01(\x0b\x32:.doublecloud.kafka.v1.UpdateConnectorSpec.UpdatePropertiesR\nproperties\x12~\n\x1c\x63onnector_config_mirrormaker\x18\n \x01(\x0b\x32:.doublecloud.kafka.v1.UpdateConnectorConfigMirrorMakerSpecH\x00R\x1a\x63onnectorConfigMirrormaker\x12p\n\x18\x63onnector_config_s3_sink\x18\x0b \x01(\x0b\x32\x35.doublecloud.kafka.v1.UpdateConnectorConfigS3SinkSpecH\x00R\x15\x63onnectorConfigS3Sink\x1a\xbd\x01\n\x10UpdateProperties\x12j\n\nproperties\x18\x01 \x03(\x0b\x32J.doublecloud.kafka.v1.UpdateConnectorSpec.UpdateProperties.PropertiesEntryR\nproperties\x1a=\n\x0fPropertiesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x12\n\x10\x63onnector_configJ\x04\x08\x03\x10\n\"\xac\x02\n\x1e\x43onnectorConfigMirrorMakerSpec\x12R\n\x0esource_cluster\x18\x01 \x01(\x0b\x32+.doublecloud.kafka.v1.ClusterConnectionSpecR\rsourceCluster\x12R\n\x0etarget_cluster\x18\x02 \x01(\x0b\x32+.doublecloud.kafka.v1.ClusterConnectionSpecR\rtargetCluster\x12\x16\n\x06topics\x18\x03 \x01(\tR\x06topics\x12J\n\x12replication_factor\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x11replicationFactor\"\x8b\x02\n\x15\x43lusterConnectionSpec\x12\x32\n\x05\x61lias\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x05\x61lias\x12\x46\n\x0cthis_cluster\x18\x02 \x01(\x0b\x32!.doublecloud.kafka.v1.ThisClusterH\x00R\x0bthisCluster\x12`\n\x10\x65xternal_cluster\x18\x03 \x01(\x0b\x32\x33.doublecloud.kafka.v1.ExternalClusterConnectionSpecH\x00R\x0f\x65xternalClusterB\x14\n\x12\x63luster_connection\"\xde\x03\n\x1d\x45xternalClusterConnectionSpec\x12I\n\x11\x62ootstrap_servers\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x10\x62ootstrapServers\x12\x41\n\rsasl_username\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x0csaslUsername\x12\x41\n\rsasl_password\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x0csaslPassword\x12\x43\n\x0esasl_mechanism\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\rsaslMechanism\x12I\n\x11security_protocol\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x10securityProtocol\x12\\\n\x1bssl_truststore_certificates\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x19sslTruststoreCertificates\"\xfb\x01\n\x19\x43onnectorConfigS3SinkSpec\x12\x16\n\x06topics\x18\x01 \x01(\tR\x06topics\x12\x32\n\x15\x66ile_compression_type\x18\x02 \x01(\tR\x13\x66ileCompressionType\x12\x45\n\x10\x66ile_max_records\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0e\x66ileMaxRecords\x12K\n\rs3_connection\x18\x04 \x01(\x0b\x32&.doublecloud.kafka.v1.S3ConnectionSpecR\x0cs3Connection\"\xd0\x02\n$UpdateConnectorConfigMirrorMakerSpec\x12R\n\x0esource_cluster\x18\x01 \x01(\x0b\x32+.doublecloud.kafka.v1.ClusterConnectionSpecR\rsourceCluster\x12R\n\x0etarget_cluster\x18\x02 \x01(\x0b\x32+.doublecloud.kafka.v1.ClusterConnectionSpecR\rtargetCluster\x12\x34\n\x06topics\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x06topics\x12J\n\x12replication_factor\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x11replicationFactor\"\xeb\x01\n\x1fUpdateConnectorConfigS3SinkSpec\x12\x34\n\x06topics\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x06topics\x12\x45\n\x10\x66ile_max_records\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0e\x66ileMaxRecords\x12K\n\rs3_connection\x18\x03 \x01(\x0b\x32&.doublecloud.kafka.v1.S3ConnectionSpecR\x0cs3Connection\"\xcd\x02\n\x10S3ConnectionSpec\x12=\n\x0b\x62ucket_name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\nbucketName\x12@\n\raccess_key_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x0b\x61\x63\x63\x65ssKeyId\x12H\n\x11secret_access_key\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x0fsecretAccessKey\x12\x38\n\x08\x65ndpoint\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x08\x65ndpoint\x12\x34\n\x06region\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x06region\"\x98\x06\n\tConnector\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x38\n\ttasks_max\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x08tasksMax\x12O\n\nproperties\x18\x03 \x03(\x0b\x32/.doublecloud.kafka.v1.Connector.PropertiesEntryR\nproperties\x12>\n\x06health\x18\x04 \x01(\x0e\x32&.doublecloud.kafka.v1.Connector.HealthR\x06health\x12>\n\x06status\x18\x05 \x01(\x0e\x32&.doublecloud.kafka.v1.Connector.StatusR\x06status\x12\x1d\n\ncluster_id\x18\x06 \x01(\tR\tclusterId\x12t\n\x1c\x63onnector_config_mirrormaker\x18\n \x01(\x0b\x32\x30.doublecloud.kafka.v1.ConnectorConfigMirrorMakerH\x00R\x1a\x63onnectorConfigMirrormaker\x12\x66\n\x18\x63onnector_config_s3_sink\x18\x0b \x01(\x0b\x32+.doublecloud.kafka.v1.ConnectorConfigS3SinkH\x00R\x15\x63onnectorConfigS3Sink\x1a=\n\x0fPropertiesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"?\n\x06Health\x12\x12\n\x0eHEALTH_INVALID\x10\x00\x12\x10\n\x0cHEALTH_ALIVE\x10\x01\x12\x0f\n\x0bHEALTH_DEAD\x10\x02\"U\n\x06Status\x12\x12\n\x0eSTATUS_INVALID\x10\x00\x12\x12\n\x0eSTATUS_RUNNING\x10\x01\x12\x10\n\x0cSTATUS_ERROR\x10\x02\x12\x11\n\rSTATUS_PAUSED\x10\x03\x42\x12\n\x10\x63onnector_configJ\x04\x08\x07\x10\n\"\xa0\x02\n\x1a\x43onnectorConfigMirrorMaker\x12N\n\x0esource_cluster\x18\x01 \x01(\x0b\x32\'.doublecloud.kafka.v1.ClusterConnectionR\rsourceCluster\x12N\n\x0etarget_cluster\x18\x02 \x01(\x0b\x32\'.doublecloud.kafka.v1.ClusterConnectionR\rtargetCluster\x12\x16\n\x06topics\x18\x03 \x01(\tR\x06topics\x12J\n\x12replication_factor\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x11replicationFactor\"\xe5\x01\n\x11\x43lusterConnection\x12\x14\n\x05\x61lias\x18\x01 \x01(\tR\x05\x61lias\x12\x46\n\x0cthis_cluster\x18\x02 \x01(\x0b\x32!.doublecloud.kafka.v1.ThisClusterH\x00R\x0bthisCluster\x12\\\n\x10\x65xternal_cluster\x18\x03 \x01(\x0b\x32/.doublecloud.kafka.v1.ExternalClusterConnectionH\x00R\x0f\x65xternalClusterB\x14\n\x12\x63luster_connection\"\r\n\x0bThisCluster\"\xc1\x01\n\x19\x45xternalClusterConnection\x12+\n\x11\x62ootstrap_servers\x18\x01 \x01(\tR\x10\x62ootstrapServers\x12#\n\rsasl_username\x18\x02 \x01(\tR\x0csaslUsername\x12%\n\x0esasl_mechanism\x18\x03 \x01(\tR\rsaslMechanism\x12+\n\x11security_protocol\x18\x04 \x01(\tR\x10securityProtocol\"\xf3\x01\n\x15\x43onnectorConfigS3Sink\x12\x16\n\x06topics\x18\x01 \x01(\tR\x06topics\x12\x32\n\x15\x66ile_compression_type\x18\x02 \x01(\tR\x13\x66ileCompressionType\x12\x45\n\x10\x66ile_max_records\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0e\x66ileMaxRecords\x12G\n\rs3_connection\x18\x04 \x01(\x0b\x32\".doublecloud.kafka.v1.S3ConnectionR\x0cs3Connection\"\x87\x01\n\x0cS3Connection\x12\x1f\n\x0b\x62ucket_name\x18\x01 \x01(\tR\nbucketName\x12\"\n\raccess_key_id\x18\x02 \x01(\tR\x0b\x61\x63\x63\x65ssKeyId\x12\x1a\n\x08\x65ndpoint\x18\x03 \x01(\tR\x08\x65ndpoint\x12\x16\n\x06region\x18\x04 \x01(\tR\x06regionB?Z=github.com/doublecloud/go-genproto/doublecloud/kafka/v1;kafkab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.kafka.v1.connector_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/doublecloud/go-genproto/doublecloud/kafka/v1;kafka'
  _globals['_CONNECTORSPEC_PROPERTIESENTRY']._loaded_options = None
  _globals['_CONNECTORSPEC_PROPERTIESENTRY']._serialized_options = b'8\001'
  _globals['_UPDATECONNECTORSPEC_UPDATEPROPERTIES_PROPERTIESENTRY']._loaded_options = None
  _globals['_UPDATECONNECTORSPEC_UPDATEPROPERTIES_PROPERTIESENTRY']._serialized_options = b'8\001'
  _globals['_CONNECTOR_PROPERTIESENTRY']._loaded_options = None
  _globals['_CONNECTOR_PROPERTIESENTRY']._serialized_options = b'8\001'
  _globals['_CONNECTORSPEC']._serialized_start=95
  _globals['_CONNECTORSPEC']._serialized_end=592
  _globals['_CONNECTORSPEC_PROPERTIESENTRY']._serialized_start=505
  _globals['_CONNECTORSPEC_PROPERTIESENTRY']._serialized_end=566
  _globals['_UPDATECONNECTORSPEC']._serialized_start=595
  _globals['_UPDATECONNECTORSPEC']._serialized_end=1226
  _globals['_UPDATECONNECTORSPEC_UPDATEPROPERTIES']._serialized_start=1011
  _globals['_UPDATECONNECTORSPEC_UPDATEPROPERTIES']._serialized_end=1200
  _globals['_UPDATECONNECTORSPEC_UPDATEPROPERTIES_PROPERTIESENTRY']._serialized_start=505
  _globals['_UPDATECONNECTORSPEC_UPDATEPROPERTIES_PROPERTIESENTRY']._serialized_end=566
  _globals['_CONNECTORCONFIGMIRRORMAKERSPEC']._serialized_start=1229
  _globals['_CONNECTORCONFIGMIRRORMAKERSPEC']._serialized_end=1529
  _globals['_CLUSTERCONNECTIONSPEC']._serialized_start=1532
  _globals['_CLUSTERCONNECTIONSPEC']._serialized_end=1799
  _globals['_EXTERNALCLUSTERCONNECTIONSPEC']._serialized_start=1802
  _globals['_EXTERNALCLUSTERCONNECTIONSPEC']._serialized_end=2280
  _globals['_CONNECTORCONFIGS3SINKSPEC']._serialized_start=2283
  _globals['_CONNECTORCONFIGS3SINKSPEC']._serialized_end=2534
  _globals['_UPDATECONNECTORCONFIGMIRRORMAKERSPEC']._serialized_start=2537
  _globals['_UPDATECONNECTORCONFIGMIRRORMAKERSPEC']._serialized_end=2873
  _globals['_UPDATECONNECTORCONFIGS3SINKSPEC']._serialized_start=2876
  _globals['_UPDATECONNECTORCONFIGS3SINKSPEC']._serialized_end=3111
  _globals['_S3CONNECTIONSPEC']._serialized_start=3114
  _globals['_S3CONNECTIONSPEC']._serialized_end=3447
  _globals['_CONNECTOR']._serialized_start=3450
  _globals['_CONNECTOR']._serialized_end=4242
  _globals['_CONNECTOR_PROPERTIESENTRY']._serialized_start=505
  _globals['_CONNECTOR_PROPERTIESENTRY']._serialized_end=566
  _globals['_CONNECTOR_HEALTH']._serialized_start=4066
  _globals['_CONNECTOR_HEALTH']._serialized_end=4129
  _globals['_CONNECTOR_STATUS']._serialized_start=4131
  _globals['_CONNECTOR_STATUS']._serialized_end=4216
  _globals['_CONNECTORCONFIGMIRRORMAKER']._serialized_start=4245
  _globals['_CONNECTORCONFIGMIRRORMAKER']._serialized_end=4533
  _globals['_CLUSTERCONNECTION']._serialized_start=4536
  _globals['_CLUSTERCONNECTION']._serialized_end=4765
  _globals['_THISCLUSTER']._serialized_start=4767
  _globals['_THISCLUSTER']._serialized_end=4780
  _globals['_EXTERNALCLUSTERCONNECTION']._serialized_start=4783
  _globals['_EXTERNALCLUSTERCONNECTION']._serialized_end=4976
  _globals['_CONNECTORCONFIGS3SINK']._serialized_start=4979
  _globals['_CONNECTORCONFIGS3SINK']._serialized_end=5222
  _globals['_S3CONNECTION']._serialized_start=5225
  _globals['_S3CONNECTION']._serialized_end=5360
# @@protoc_insertion_point(module_scope)
