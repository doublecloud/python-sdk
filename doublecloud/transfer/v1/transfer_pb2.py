# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doublecloud/transfer/v1/transfer.proto
# Protobuf Python Version: 5.27.2
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
    2,
    '',
    'doublecloud/transfer/v1/transfer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doublecloud.transfer.v1.endpoint import common_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_common__pb2
from doublecloud.transfer.v1.endpoint import parsers_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint_dot_parsers__pb2
from doublecloud.transfer.v1 import endpoint_pb2 as doublecloud_dot_transfer_dot_v1_dot_endpoint__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&doublecloud/transfer/v1/transfer.proto\x12\x17\x64oublecloud.transfer.v1\x1a-doublecloud/transfer/v1/endpoint/common.proto\x1a.doublecloud/transfer/v1/endpoint/parsers.proto\x1a&doublecloud/transfer/v1/endpoint.proto\"\xc0\x06\n\x08Transfer\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\nproject_id\x18\x02 \x01(\tR\tprojectId\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12\x45\n\x06labels\x18\x06 \x03(\x0b\x32-.doublecloud.transfer.v1.Transfer.LabelsEntryR\x06labels\x12\x39\n\x06source\x18\x07 \x01(\x0b\x32!.doublecloud.transfer.v1.EndpointR\x06source\x12\x39\n\x06target\x18\x08 \x01(\x0b\x32!.doublecloud.transfer.v1.EndpointR\x06target\x12:\n\x07runtime\x18\t \x01(\x0b\x32 .doublecloud.transfer.v1.RuntimeR\x07runtime\x12?\n\x06status\x18\n \x01(\x0e\x32\'.doublecloud.transfer.v1.TransferStatusR\x06status\x12\x39\n\x04type\x18\x0c \x01(\x0e\x32%.doublecloud.transfer.v1.TransferTypeR\x04type\x12\x18\n\x07warning\x18\x0f \x01(\tR\x07warning\x12S\n\x10regular_snapshot\x18\x10 \x01(\x0b\x32(.doublecloud.transfer.v1.RegularSnapshotR\x0fregularSnapshot\x12O\n\x0etransformation\x18\x11 \x01(\x0b\x32\'.doublecloud.transfer.v1.TransformationR\x0etransformation\x12G\n\x0c\x64\x61ta_objects\x18\x13 \x01(\x0b\x32$.doublecloud.transfer.v1.DataObjectsR\x0b\x64\x61taObjects\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01J\x04\x08\x03\x10\x04J\x04\x08\x0b\x10\x0cJ\x04\x08\r\x10\x0fJ\x04\x08\x12\x10\x13\"\xd1\x01\n\x07Runtime\x12[\n\x12serverless_runtime\x18\x05 \x01(\x0b\x32*.doublecloud.transfer.v1.ServerlessRuntimeH\x00R\x11serverlessRuntime\x12X\n\x11\x64\x65\x64icated_runtime\x18\x06 \x01(\x0b\x32).doublecloud.transfer.v1.DedicatedRuntimeH\x00R\x10\x64\x65\x64icatedRuntimeB\t\n\x07runtimeJ\x04\x08\x01\x10\x05\"6\n\x11ServerlessRuntime\x12\x1b\n\tjob_count\x18\x02 \x01(\x03R\x08jobCountJ\x04\x08\x01\x10\x02\"\xbf\x01\n\x0fRegularSnapshot\x12N\n\x08settings\x18\x03 \x01(\x0b\x32\x30.doublecloud.transfer.v1.RegularSnapshotSettingsH\x00R\x08settings\x12N\n\x08\x64isabled\x18\x04 \x01(\x0b\x32\x30.doublecloud.transfer.v1.RegularSnapshotDisabledH\x00R\x08\x64isabledB\x06\n\x04modeJ\x04\x08\x01\x10\x03\"\x19\n\x17RegularSnapshotDisabled\"\xdb\x01\n\x17RegularSnapshotSettings\x12T\n\x08schedule\x18\x01 \x01(\x0e\x32\x38.doublecloud.transfer.v1.RegularSnapshotScheduleIntervalR\x08schedule\x12\x41\n\x06tables\x18\x02 \x03(\x0b\x32).doublecloud.transfer.v1.IncrementalTableR\x06tables\x12\'\n\x0f\x63ron_expression\x18\x03 \x01(\tR\x0e\x63ronExpression\"\xa4\x01\n\x10IncrementalTable\x12\'\n\x0ftable_namespace\x18\x01 \x01(\tR\x0etableNamespace\x12\x1d\n\ntable_name\x18\x02 \x01(\tR\ttableName\x12#\n\rcursor_column\x18\x03 \x01(\tR\x0c\x63ursorColumn\x12#\n\rinitial_state\x18\x04 \x01(\tR\x0cinitialState\"\x96\x01\n\x10\x44\x65\x64icatedRuntime\x12\x37\n\x06\x66lavor\x18\x02 \x01(\x0e\x32\x1f.doublecloud.transfer.v1.FlavorR\x06\x66lavor\x12=\n\x08settings\x18\x08 \x01(\x0b\x32!.doublecloud.transfer.v1.SettingsR\x08settingsJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x08\"\xb8\x01\n\x08Settings\x12L\n\rauto_settings\x18\x01 \x01(\x0b\x32%.doublecloud.transfer.v1.AutoSettingsH\x00R\x0c\x61utoSettings\x12R\n\x0fmanual_settings\x18\x02 \x01(\x0b\x32\'.doublecloud.transfer.v1.ManualSettingsH\x00R\x0emanualSettingsB\n\n\x08settings\"\x0e\n\x0c\x41utoSettings\"5\n\x0eManualSettings\x12\x1d\n\nnetwork_id\x18\x04 \x01(\tR\tnetworkIdJ\x04\x08\x01\x10\x04\"z\n\x0cMaskFunction\x12Y\n\x12mask_function_hash\x18\x01 \x01(\x0b\x32).doublecloud.transfer.v1.MaskFunctionHashH\x00R\x10maskFunctionHashB\x0f\n\rmask_function\">\n\x10MaskFunctionHash\x12*\n\x11user_defined_salt\x18\x01 \x01(\tR\x0fuserDefinedSalt\"\\\n\x0cTablesFilter\x12%\n\x0einclude_tables\x18\x01 \x03(\tR\rincludeTables\x12%\n\x0e\x65xclude_tables\x18\x02 \x03(\tR\rexcludeTables\"a\n\rColumnsFilter\x12\'\n\x0finclude_columns\x18\x01 \x03(\tR\x0eincludeColumns\x12\'\n\x0f\x65xclude_columns\x18\x02 \x03(\tR\x0e\x65xcludeColumns\"\xb2\x01\n\x14MaskFieldTransformer\x12=\n\x06tables\x18\x01 \x01(\x0b\x32%.doublecloud.transfer.v1.TablesFilterR\x06tables\x12\x18\n\x07\x63olumns\x18\x02 \x03(\tR\x07\x63olumns\x12\x41\n\x08\x66unction\x18\x03 \x01(\x0b\x32%.doublecloud.transfer.v1.MaskFunctionR\x08\x66unction\"\x9b\x01\n\x18\x46ilterColumnsTransformer\x12=\n\x06tables\x18\x01 \x01(\x0b\x32%.doublecloud.transfer.v1.TablesFilterR\x06tables\x12@\n\x07\x63olumns\x18\x02 \x01(\x0b\x32&.doublecloud.transfer.v1.ColumnsFilterR\x07\x63olumns\":\n\x05Table\x12\x1d\n\nname_space\x18\x01 \x01(\tR\tnameSpace\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"\x8d\x01\n\x0bRenameTable\x12\x43\n\roriginal_name\x18\x01 \x01(\x0b\x32\x1e.doublecloud.transfer.v1.TableR\x0coriginalName\x12\x39\n\x08new_name\x18\x02 \x01(\x0b\x32\x1e.doublecloud.transfer.v1.TableR\x07newName\"d\n\x17RenameTablesTransformer\x12I\n\rrename_tables\x18\x01 \x03(\x0b\x32$.doublecloud.transfer.v1.RenameTableR\x0crenameTables\"V\n\x15SkipEventsTransformer\x12=\n\x06tables\x18\x01 \x01(\x0b\x32%.doublecloud.transfer.v1.TablesFilterR\x06tables\"q\n\x1cReplacePrimaryKeyTransformer\x12=\n\x06tables\x18\x01 \x01(\x0b\x32%.doublecloud.transfer.v1.TablesFilterR\x06tables\x12\x12\n\x04keys\x18\x02 \x03(\tR\x04keys\"\x96\x01\n\x13ToStringTransformer\x12=\n\x06tables\x18\x01 \x01(\x0b\x32%.doublecloud.transfer.v1.TablesFilterR\x06tables\x12@\n\x07\x63olumns\x18\x02 \x01(\x0b\x32&.doublecloud.transfer.v1.ColumnsFilterR\x07\x63olumns\"\xb8\x01\n\x12SharderTransformer\x12=\n\x06tables\x18\x01 \x01(\x0b\x32%.doublecloud.transfer.v1.TablesFilterR\x06tables\x12@\n\x07\x63olumns\x18\x02 \x01(\x0b\x32&.doublecloud.transfer.v1.ColumnsFilterR\x07\x63olumns\x12!\n\x0cshards_count\x18\x03 \x01(\x03R\x0bshardsCount\"\x83\x01\n\x16RawDocGroupTransformer\x12=\n\x06tables\x18\x01 \x01(\x0b\x32%.doublecloud.transfer.v1.TablesFilterR\x06tables\x12\x12\n\x04keys\x18\x02 \x03(\tR\x04keys\x12\x16\n\x06\x66ields\x18\x03 \x03(\tR\x06\x66ields\"M\n\x19RawCdcDocGroupTransformer\x12\x12\n\x04keys\x18\x02 \x03(\tR\x04keys\x12\x16\n\x06\x66ields\x18\x03 \x03(\tR\x06\x66ieldsJ\x04\x08\x01\x10\x02\"e\n\x0eSQLTransformer\x12=\n\x06tables\x18\x01 \x01(\x0b\x32%.doublecloud.transfer.v1.TablesFilterR\x06tables\x12\x14\n\x05query\x18\x02 \x01(\tR\x05query\"\xa5\x03\n\x0e\x44\x42TTransformer\x12.\n\x13git_repository_link\x18\x01 \x01(\tR\x11gitRepositoryLink\x12\x1d\n\ngit_branch\x18\x02 \x01(\tR\tgitBranch\x12!\n\x0cprofile_name\x18\x03 \x01(\tR\x0bprofileName\x12O\n\toperation\x18\x04 \x01(\x0e\x32\x31.doublecloud.transfer.v1.DBTTransformer.OperationR\toperation\"\xcf\x01\n\tOperation\x12\x19\n\x15OPERATION_UNSPECIFIED\x10\x00\x12\x13\n\x0fOPERATION_BUILD\x10\x01\x12\x15\n\x11OPERATION_COMPILE\x10\x02\x12\x13\n\x0fOPERATION_DEBUG\x10\x03\x12\x13\n\x0fOPERATION_PARSE\x10\x04\x12\x11\n\rOPERATION_RUN\x10\x05\x12\x12\n\x0eOPERATION_SEED\x10\x06\x12\x16\n\x12OPERATION_SNAPSHOT\x10\x07\x12\x12\n\x0eOPERATION_TEST\x10\x08\"\x8f\x01\n\x18TableSplitterTransformer\x12=\n\x06tables\x18\x01 \x01(\x0b\x32%.doublecloud.transfer.v1.TablesFilterR\x06tables\x12\x18\n\x07\x63olumns\x18\x02 \x03(\tR\x07\x63olumns\x12\x1a\n\x08splitter\x18\x03 \x01(\tR\x08splitter\"n\n\x15\x46ilterRowsTransformer\x12=\n\x06tables\x18\x01 \x01(\x0b\x32%.doublecloud.transfer.v1.TablesFilterR\x06tables\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\"Y\n\x18NumberToFloatTransformer\x12=\n\x06tables\x18\x01 \x01(\x0b\x32%.doublecloud.transfer.v1.TablesFilterR\x06tables\"\xc2\n\n\x0bTransformer\x12N\n\nmask_field\x18\x01 \x01(\x0b\x32-.doublecloud.transfer.v1.MaskFieldTransformerH\x00R\tmaskField\x12Z\n\x0e\x66ilter_columns\x18\x02 \x01(\x0b\x32\x31.doublecloud.transfer.v1.FilterColumnsTransformerH\x00R\rfilterColumns\x12Q\n\x0bskip_events\x18\x03 \x01(\x0b\x32..doublecloud.transfer.v1.SkipEventsTransformerH\x00R\nskipEvents\x12W\n\rrename_tables\x18\x04 \x01(\x0b\x32\x30.doublecloud.transfer.v1.RenameTablesTransformerH\x00R\x0crenameTables\x12g\n\x13replace_primary_key\x18\x06 \x01(\x0b\x32\x35.doublecloud.transfer.v1.ReplacePrimaryKeyTransformerH\x00R\x11replacePrimaryKey\x12Z\n\x11\x63onvert_to_string\x18\x07 \x01(\x0b\x32,.doublecloud.transfer.v1.ToStringTransformerH\x00R\x0f\x63onvertToString\x12^\n\x13sharder_transformer\x18\t \x01(\x0b\x32+.doublecloud.transfer.v1.SharderTransformerH\x00R\x12sharderTransformer\x12;\n\x03sql\x18\x0b \x01(\x0b\x32\'.doublecloud.transfer.v1.SQLTransformerH\x00R\x03sql\x12;\n\x03\x64\x62t\x18\x0c \x01(\x0b\x32\'.doublecloud.transfer.v1.DBTTransformerH\x00R\x03\x64\x62t\x12q\n\x1atable_splitter_transformer\x18\r \x01(\x0b\x32\x31.doublecloud.transfer.v1.TableSplitterTransformerH\x00R\x18tableSplitterTransformer\x12Q\n\x0b\x66ilter_rows\x18\x0e \x01(\x0b\x32..doublecloud.transfer.v1.FilterRowsTransformerH\x00R\nfilterRows\x12r\n\x1bnumber_to_float_transformer\x18\x0f \x01(\x0b\x32\x31.doublecloud.transfer.v1.NumberToFloatTransformerH\x00R\x18numberToFloatTransformer\x12h\n\x17json_mapper_transformer\x18\x11 \x01(\x0b\x32..doublecloud.transfer.v1.JsonParserTransformerH\x00R\x15jsonMapperTransformer\x12q\n\x1a\x63loud_function_transformer\x18\x12 \x01(\x0b\x32\x31.doublecloud.transfer.v1.CloudFunctionTransformerH\x00R\x18\x63loudFunctionTransformerB\r\n\x0btransformerJ\x04\x08\x05\x10\x06J\x04\x08\x08\x10\tJ\x04\x08\n\x10\x0bJ\x04\x08\x10\x10\x11\"\xa4\x01\n\x18\x43loudFunctionTransformer\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\nname_space\x18\x02 \x01(\tR\tnameSpace\x12U\n\x07options\x18\x03 \x01(\x0b\x32;.doublecloud.transfer.v1.endpoint.DataTransformationOptionsR\x07options\"|\n\x15JsonParserTransformer\x12\x14\n\x05topic\x18\x01 \x01(\tR\x05topic\x12M\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x35.doublecloud.transfer.v1.endpoint.GenericParserCommonR\x06\x63onfig\"Z\n\x0eTransformation\x12H\n\x0ctransformers\x18\x01 \x03(\x0b\x32$.doublecloud.transfer.v1.TransformerR\x0ctransformers\"6\n\x0b\x44\x61taObjects\x12\'\n\x0finclude_objects\x18\x01 \x03(\tR\x0eincludeObjects*p\n\x0cTransferType\x12\x1d\n\x19TRANSFER_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16SNAPSHOT_AND_INCREMENT\x10\x01\x12\x11\n\rSNAPSHOT_ONLY\x10\x02\x12\x12\n\x0eINCREMENT_ONLY\x10\x03*\x9b\x01\n\x0eTransferStatus\x12\x1f\n\x1bTRANSFER_STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0b\n\x07\x43REATED\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\x0c\n\x08STOPPING\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\t\n\x05\x45RROR\x10\x06\x12\x10\n\x0cSNAPSHOTTING\x10\x07\x12\x08\n\x04\x44ONE\x10\x08*\xf1\x03\n\x1fRegularSnapshotScheduleInterval\x12\x32\n.REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_UNSPECIFIED\x10\x00\x12,\n(REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_15MIN\x10\x02\x12,\n(REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_30MIN\x10\x03\x12+\n\'REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_HOUR\x10\x04\x12,\n(REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_2HOUR\x10\x05\x12,\n(REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_3HOUR\x10\x06\x12,\n(REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_6HOUR\x10\x07\x12,\n(REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_8HOUR\x10\x08\x12-\n)REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_12HOUR\x10\t\x12*\n&REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_DAY\x10\n*L\n\x06\x46lavor\x12\x16\n\x12\x46LAVOR_UNSPECIFIED\x10\x00\x12\t\n\x05SMALL\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\t\n\x05LARGE\x10\x03\x12\x08\n\x04TINY\x10\x04\x42\x45ZCgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1;transferb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.transfer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZCgithub.com/doublecloud/go-genproto/doublecloud/transfer/v1;transfer'
  _globals['_TRANSFER_LABELSENTRY']._loaded_options = None
  _globals['_TRANSFER_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_TRANSFERTYPE']._serialized_start=6774
  _globals['_TRANSFERTYPE']._serialized_end=6886
  _globals['_TRANSFERSTATUS']._serialized_start=6889
  _globals['_TRANSFERSTATUS']._serialized_end=7044
  _globals['_REGULARSNAPSHOTSCHEDULEINTERVAL']._serialized_start=7047
  _globals['_REGULARSNAPSHOTSCHEDULEINTERVAL']._serialized_end=7544
  _globals['_FLAVOR']._serialized_start=7546
  _globals['_FLAVOR']._serialized_end=7622
  _globals['_TRANSFER']._serialized_start=203
  _globals['_TRANSFER']._serialized_end=1035
  _globals['_TRANSFER_LABELSENTRY']._serialized_start=954
  _globals['_TRANSFER_LABELSENTRY']._serialized_end=1011
  _globals['_RUNTIME']._serialized_start=1038
  _globals['_RUNTIME']._serialized_end=1247
  _globals['_SERVERLESSRUNTIME']._serialized_start=1249
  _globals['_SERVERLESSRUNTIME']._serialized_end=1303
  _globals['_REGULARSNAPSHOT']._serialized_start=1306
  _globals['_REGULARSNAPSHOT']._serialized_end=1497
  _globals['_REGULARSNAPSHOTDISABLED']._serialized_start=1499
  _globals['_REGULARSNAPSHOTDISABLED']._serialized_end=1524
  _globals['_REGULARSNAPSHOTSETTINGS']._serialized_start=1527
  _globals['_REGULARSNAPSHOTSETTINGS']._serialized_end=1746
  _globals['_INCREMENTALTABLE']._serialized_start=1749
  _globals['_INCREMENTALTABLE']._serialized_end=1913
  _globals['_DEDICATEDRUNTIME']._serialized_start=1916
  _globals['_DEDICATEDRUNTIME']._serialized_end=2066
  _globals['_SETTINGS']._serialized_start=2069
  _globals['_SETTINGS']._serialized_end=2253
  _globals['_AUTOSETTINGS']._serialized_start=2255
  _globals['_AUTOSETTINGS']._serialized_end=2269
  _globals['_MANUALSETTINGS']._serialized_start=2271
  _globals['_MANUALSETTINGS']._serialized_end=2324
  _globals['_MASKFUNCTION']._serialized_start=2326
  _globals['_MASKFUNCTION']._serialized_end=2448
  _globals['_MASKFUNCTIONHASH']._serialized_start=2450
  _globals['_MASKFUNCTIONHASH']._serialized_end=2512
  _globals['_TABLESFILTER']._serialized_start=2514
  _globals['_TABLESFILTER']._serialized_end=2606
  _globals['_COLUMNSFILTER']._serialized_start=2608
  _globals['_COLUMNSFILTER']._serialized_end=2705
  _globals['_MASKFIELDTRANSFORMER']._serialized_start=2708
  _globals['_MASKFIELDTRANSFORMER']._serialized_end=2886
  _globals['_FILTERCOLUMNSTRANSFORMER']._serialized_start=2889
  _globals['_FILTERCOLUMNSTRANSFORMER']._serialized_end=3044
  _globals['_TABLE']._serialized_start=3046
  _globals['_TABLE']._serialized_end=3104
  _globals['_RENAMETABLE']._serialized_start=3107
  _globals['_RENAMETABLE']._serialized_end=3248
  _globals['_RENAMETABLESTRANSFORMER']._serialized_start=3250
  _globals['_RENAMETABLESTRANSFORMER']._serialized_end=3350
  _globals['_SKIPEVENTSTRANSFORMER']._serialized_start=3352
  _globals['_SKIPEVENTSTRANSFORMER']._serialized_end=3438
  _globals['_REPLACEPRIMARYKEYTRANSFORMER']._serialized_start=3440
  _globals['_REPLACEPRIMARYKEYTRANSFORMER']._serialized_end=3553
  _globals['_TOSTRINGTRANSFORMER']._serialized_start=3556
  _globals['_TOSTRINGTRANSFORMER']._serialized_end=3706
  _globals['_SHARDERTRANSFORMER']._serialized_start=3709
  _globals['_SHARDERTRANSFORMER']._serialized_end=3893
  _globals['_RAWDOCGROUPTRANSFORMER']._serialized_start=3896
  _globals['_RAWDOCGROUPTRANSFORMER']._serialized_end=4027
  _globals['_RAWCDCDOCGROUPTRANSFORMER']._serialized_start=4029
  _globals['_RAWCDCDOCGROUPTRANSFORMER']._serialized_end=4106
  _globals['_SQLTRANSFORMER']._serialized_start=4108
  _globals['_SQLTRANSFORMER']._serialized_end=4209
  _globals['_DBTTRANSFORMER']._serialized_start=4212
  _globals['_DBTTRANSFORMER']._serialized_end=4633
  _globals['_DBTTRANSFORMER_OPERATION']._serialized_start=4426
  _globals['_DBTTRANSFORMER_OPERATION']._serialized_end=4633
  _globals['_TABLESPLITTERTRANSFORMER']._serialized_start=4636
  _globals['_TABLESPLITTERTRANSFORMER']._serialized_end=4779
  _globals['_FILTERROWSTRANSFORMER']._serialized_start=4781
  _globals['_FILTERROWSTRANSFORMER']._serialized_end=4891
  _globals['_NUMBERTOFLOATTRANSFORMER']._serialized_start=4893
  _globals['_NUMBERTOFLOATTRANSFORMER']._serialized_end=4982
  _globals['_TRANSFORMER']._serialized_start=4985
  _globals['_TRANSFORMER']._serialized_end=6331
  _globals['_CLOUDFUNCTIONTRANSFORMER']._serialized_start=6334
  _globals['_CLOUDFUNCTIONTRANSFORMER']._serialized_end=6498
  _globals['_JSONPARSERTRANSFORMER']._serialized_start=6500
  _globals['_JSONPARSERTRANSFORMER']._serialized_end=6624
  _globals['_TRANSFORMATION']._serialized_start=6626
  _globals['_TRANSFORMATION']._serialized_end=6716
  _globals['_DATAOBJECTS']._serialized_start=6718
  _globals['_DATAOBJECTS']._serialized_end=6772
# @@protoc_insertion_point(module_scope)
