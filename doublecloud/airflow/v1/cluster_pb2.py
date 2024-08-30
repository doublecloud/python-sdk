# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/airflow/v1/cluster.proto
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
    'doublecloud/airflow/v1/cluster.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from doublecloud.v1 import cluster_pb2 as doublecloud_dot_v1_dot_cluster__pb2
from doublecloud.v1 import maintenance_pb2 as doublecloud_dot_v1_dot_maintenance__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$doublecloud/airflow/v1/cluster.proto\x12\x16\x64oublecloud.airflow.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1c\x64oublecloud/v1/cluster.proto\x1a doublecloud/v1/maintenance.proto\"\xcd\x06\n\x07\x43luster\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\nproject_id\x18\x02 \x01(\tR\tprojectId\x12\x1d\n\ncloud_type\x18\x03 \x01(\tR\tcloudType\x12\x1b\n\tregion_id\x18\x04 \x01(\tR\x08regionId\x12;\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x12\n\x04name\x18\x06 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x07 \x01(\tR\x0b\x64\x65scription\x12\x35\n\x06status\x18\x08 \x01(\x0e\x32\x1d.doublecloud.v1.ClusterStatusR\x06status\x12\x46\n\tresources\x18\t \x01(\x0b\x32(.doublecloud.airflow.v1.ClusterResourcesR\tresources\x12O\n\x0f\x63onnection_info\x18\n \x01(\x0b\x32&.doublecloud.airflow.v1.ConnectionInfoR\x0e\x63onnectionInfo\x12.\n\x06\x61\x63\x63\x65ss\x18\x0b \x01(\x0b\x32\x16.doublecloud.v1.AccessR\x06\x61\x63\x63\x65ss\x12=\n\x06\x63onfig\x18\x0c \x01(\x0b\x32%.doublecloud.airflow.v1.AirflowConfigR\x06\x63onfig\x12\x1d\n\nnetwork_id\x18\r \x01(\tR\tnetworkId\x12P\n\x12maintenance_window\x18\x0e \x01(\x0b\x32!.doublecloud.v1.MaintenanceWindowR\x11maintenanceWindow\x12V\n\x12\x63r_connection_info\x18\x0f \x01(\x0b\x32(.doublecloud.airflow.v1.CrConnectionInfoR\x10\x63rConnectionInfo\x12\\\n\x14managed_image_status\x18\x10 \x01(\x0b\x32*.doublecloud.airflow.v1.ManagedImageStatusR\x12managedImageStatus\">\n\x12\x41irflowEnvVariable\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"q\n\x12ManagedImageStatus\x12!\n\x0c\x62uild_errors\x18\x01 \x01(\tR\x0b\x62uildErrors\x12\x38\n\x18\x61pplied_requirements_txt\x18\x02 \x01(\tR\x16\x61ppliedRequirementsTxt\"\xdf\x03\n\x10\x43lusterResources\x12J\n\x07\x61irflow\x18\x01 \x01(\x0b\x32\x30.doublecloud.airflow.v1.ClusterResources.AirflowR\x07\x61irflow\x1a\xfe\x02\n\x07\x41irflow\x12\x45\n\x10max_worker_count\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0emaxWorkerCount\x12-\n\x12\x65nvironment_flavor\x18\x02 \x01(\tR\x11\x65nvironmentFlavor\x12\x45\n\x10min_worker_count\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0eminWorkerCount\x12J\n\x12worker_concurrency\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x11workerConcurrency\x12\x45\n\x10worker_disk_size\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0eworkerDiskSize\x12#\n\rworker_preset\x18\x06 \x01(\tR\x0cworkerPreset\"T\n\x0e\x43onnectionInfo\x12\x12\n\x04host\x18\x01 \x01(\tR\x04host\x12\x12\n\x04user\x18\x02 \x01(\tR\x04user\x12\x1a\n\x08password\x18\x03 \x01(\tR\x08password\"n\n\x10\x43rConnectionInfo\x12*\n\x11remote_image_path\x18\x01 \x01(\tR\x0fremoteImagePath\x12\x12\n\x04user\x18\x02 \x01(\tR\x04user\x12\x1a\n\x08password\x18\x03 \x01(\tR\x08password\"\xdd\x01\n\nSyncConfig\x12\x19\n\x08repo_url\x18\x01 \x01(\tR\x07repoUrl\x12\x16\n\x06\x62ranch\x18\x02 \x01(\tR\x06\x62ranch\x12\x1a\n\x08revision\x18\x03 \x01(\tR\x08revision\x12\x1b\n\tdags_path\x18\x04 \x01(\tR\x08\x64\x61gsPath\x12T\n\x0f\x61pi_credentials\x18\x05 \x01(\x0b\x32).doublecloud.airflow.v1.GitApiCredentialsH\x00R\x0e\x61piCredentialsB\r\n\x0b\x63redentials\"K\n\x11GitApiCredentials\x12\x1a\n\x08username\x18\x01 \x01(\tR\x08username\x12\x1a\n\x08password\x18\x02 \x01(\tR\x08password\"\xd5\x02\n\rAirflowConfig\x12\x1d\n\nversion_id\x18\x01 \x01(\tR\tversionId\x12=\n\x08git_sync\x18\x02 \x01(\x0b\x32\".doublecloud.airflow.v1.SyncConfigR\x07gitSync\x12.\n\x13\x63ustom_image_digest\x18\x03 \x01(\tR\x11\x63ustomImageDigest\x12\x38\n\x18managed_requirements_txt\x18\x04 \x01(\tR\x16managedRequirementsTxt\x12\x35\n\x17user_service_account_id\x18\x05 \x01(\tR\x14userServiceAccountId\x12\x45\n\x08\x65nv_vars\x18\x06 \x03(\x0b\x32*.doublecloud.airflow.v1.AirflowEnvVariableR\x07\x65nvVarsBCZAgithub.com/doublecloud/go-genproto/doublecloud/airflow/v1;airflowb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.airflow.v1.cluster_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/doublecloud/go-genproto/doublecloud/airflow/v1;airflow'
  _globals['_CLUSTER']._serialized_start=194
  _globals['_CLUSTER']._serialized_end=1039
  _globals['_AIRFLOWENVVARIABLE']._serialized_start=1041
  _globals['_AIRFLOWENVVARIABLE']._serialized_end=1103
  _globals['_MANAGEDIMAGESTATUS']._serialized_start=1105
  _globals['_MANAGEDIMAGESTATUS']._serialized_end=1218
  _globals['_CLUSTERRESOURCES']._serialized_start=1221
  _globals['_CLUSTERRESOURCES']._serialized_end=1700
  _globals['_CLUSTERRESOURCES_AIRFLOW']._serialized_start=1318
  _globals['_CLUSTERRESOURCES_AIRFLOW']._serialized_end=1700
  _globals['_CONNECTIONINFO']._serialized_start=1702
  _globals['_CONNECTIONINFO']._serialized_end=1786
  _globals['_CRCONNECTIONINFO']._serialized_start=1788
  _globals['_CRCONNECTIONINFO']._serialized_end=1898
  _globals['_SYNCCONFIG']._serialized_start=1901
  _globals['_SYNCCONFIG']._serialized_end=2122
  _globals['_GITAPICREDENTIALS']._serialized_start=2124
  _globals['_GITAPICREDENTIALS']._serialized_end=2199
  _globals['_AIRFLOWCONFIG']._serialized_start=2202
  _globals['_AIRFLOWCONFIG']._serialized_end=2543
# @@protoc_insertion_point(module_scope)
