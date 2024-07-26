from doublecloud.transfer.v1.endpoint import common_pb2 as _common_pb2
from doublecloud.transfer.v1.endpoint import parsers_pb2 as _parsers_pb2
from doublecloud.transfer.v1 import endpoint_pb2 as _endpoint_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransferType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSFER_TYPE_UNSPECIFIED: _ClassVar[TransferType]
    SNAPSHOT_AND_INCREMENT: _ClassVar[TransferType]
    SNAPSHOT_ONLY: _ClassVar[TransferType]
    INCREMENT_ONLY: _ClassVar[TransferType]

class TransferStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSFER_STATUS_UNSPECIFIED: _ClassVar[TransferStatus]
    CREATING: _ClassVar[TransferStatus]
    CREATED: _ClassVar[TransferStatus]
    RUNNING: _ClassVar[TransferStatus]
    STOPPING: _ClassVar[TransferStatus]
    STOPPED: _ClassVar[TransferStatus]
    ERROR: _ClassVar[TransferStatus]
    SNAPSHOTTING: _ClassVar[TransferStatus]
    DONE: _ClassVar[TransferStatus]

class RegularSnapshotScheduleInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_UNSPECIFIED: _ClassVar[RegularSnapshotScheduleInterval]
    REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_15MIN: _ClassVar[RegularSnapshotScheduleInterval]
    REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_30MIN: _ClassVar[RegularSnapshotScheduleInterval]
    REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_HOUR: _ClassVar[RegularSnapshotScheduleInterval]
    REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_2HOUR: _ClassVar[RegularSnapshotScheduleInterval]
    REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_3HOUR: _ClassVar[RegularSnapshotScheduleInterval]
    REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_6HOUR: _ClassVar[RegularSnapshotScheduleInterval]
    REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_8HOUR: _ClassVar[RegularSnapshotScheduleInterval]
    REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_12HOUR: _ClassVar[RegularSnapshotScheduleInterval]
    REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_DAY: _ClassVar[RegularSnapshotScheduleInterval]

class Flavor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FLAVOR_UNSPECIFIED: _ClassVar[Flavor]
    SMALL: _ClassVar[Flavor]
    MEDIUM: _ClassVar[Flavor]
    LARGE: _ClassVar[Flavor]
    TINY: _ClassVar[Flavor]
TRANSFER_TYPE_UNSPECIFIED: TransferType
SNAPSHOT_AND_INCREMENT: TransferType
SNAPSHOT_ONLY: TransferType
INCREMENT_ONLY: TransferType
TRANSFER_STATUS_UNSPECIFIED: TransferStatus
CREATING: TransferStatus
CREATED: TransferStatus
RUNNING: TransferStatus
STOPPING: TransferStatus
STOPPED: TransferStatus
ERROR: TransferStatus
SNAPSHOTTING: TransferStatus
DONE: TransferStatus
REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_UNSPECIFIED: RegularSnapshotScheduleInterval
REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_15MIN: RegularSnapshotScheduleInterval
REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_30MIN: RegularSnapshotScheduleInterval
REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_HOUR: RegularSnapshotScheduleInterval
REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_2HOUR: RegularSnapshotScheduleInterval
REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_3HOUR: RegularSnapshotScheduleInterval
REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_6HOUR: RegularSnapshotScheduleInterval
REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_8HOUR: RegularSnapshotScheduleInterval
REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_12HOUR: RegularSnapshotScheduleInterval
REGULAR_SNAPSHOT_SCHEDULE_INTERVAL_DAY: RegularSnapshotScheduleInterval
FLAVOR_UNSPECIFIED: Flavor
SMALL: Flavor
MEDIUM: Flavor
LARGE: Flavor
TINY: Flavor

class Transfer(_message.Message):
    __slots__ = ("id", "project_id", "name", "description", "labels", "source", "target", "runtime", "status", "type", "warning", "regular_snapshot", "transformation", "data_objects")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    WARNING_FIELD_NUMBER: _ClassVar[int]
    REGULAR_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMATION_FIELD_NUMBER: _ClassVar[int]
    DATA_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    name: str
    description: str
    labels: _containers.ScalarMap[str, str]
    source: _endpoint_pb2.Endpoint
    target: _endpoint_pb2.Endpoint
    runtime: Runtime
    status: TransferStatus
    type: TransferType
    warning: str
    regular_snapshot: RegularSnapshot
    transformation: Transformation
    data_objects: DataObjects
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., source: _Optional[_Union[_endpoint_pb2.Endpoint, _Mapping]] = ..., target: _Optional[_Union[_endpoint_pb2.Endpoint, _Mapping]] = ..., runtime: _Optional[_Union[Runtime, _Mapping]] = ..., status: _Optional[_Union[TransferStatus, str]] = ..., type: _Optional[_Union[TransferType, str]] = ..., warning: _Optional[str] = ..., regular_snapshot: _Optional[_Union[RegularSnapshot, _Mapping]] = ..., transformation: _Optional[_Union[Transformation, _Mapping]] = ..., data_objects: _Optional[_Union[DataObjects, _Mapping]] = ...) -> None: ...

class Runtime(_message.Message):
    __slots__ = ("serverless_runtime", "dedicated_runtime")
    SERVERLESS_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    serverless_runtime: ServerlessRuntime
    dedicated_runtime: DedicatedRuntime
    def __init__(self, serverless_runtime: _Optional[_Union[ServerlessRuntime, _Mapping]] = ..., dedicated_runtime: _Optional[_Union[DedicatedRuntime, _Mapping]] = ...) -> None: ...

class ServerlessRuntime(_message.Message):
    __slots__ = ("job_count",)
    JOB_COUNT_FIELD_NUMBER: _ClassVar[int]
    job_count: int
    def __init__(self, job_count: _Optional[int] = ...) -> None: ...

class RegularSnapshot(_message.Message):
    __slots__ = ("settings", "disabled")
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    settings: RegularSnapshotSettings
    disabled: RegularSnapshotDisabled
    def __init__(self, settings: _Optional[_Union[RegularSnapshotSettings, _Mapping]] = ..., disabled: _Optional[_Union[RegularSnapshotDisabled, _Mapping]] = ...) -> None: ...

class RegularSnapshotDisabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RegularSnapshotSettings(_message.Message):
    __slots__ = ("schedule", "tables", "cron_expression")
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    CRON_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    schedule: RegularSnapshotScheduleInterval
    tables: _containers.RepeatedCompositeFieldContainer[IncrementalTable]
    cron_expression: str
    def __init__(self, schedule: _Optional[_Union[RegularSnapshotScheduleInterval, str]] = ..., tables: _Optional[_Iterable[_Union[IncrementalTable, _Mapping]]] = ..., cron_expression: _Optional[str] = ...) -> None: ...

class IncrementalTable(_message.Message):
    __slots__ = ("table_namespace", "table_name", "cursor_column", "initial_state")
    TABLE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    CURSOR_COLUMN_FIELD_NUMBER: _ClassVar[int]
    INITIAL_STATE_FIELD_NUMBER: _ClassVar[int]
    table_namespace: str
    table_name: str
    cursor_column: str
    initial_state: str
    def __init__(self, table_namespace: _Optional[str] = ..., table_name: _Optional[str] = ..., cursor_column: _Optional[str] = ..., initial_state: _Optional[str] = ...) -> None: ...

class DedicatedRuntime(_message.Message):
    __slots__ = ("flavor", "settings")
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    flavor: Flavor
    settings: Settings
    def __init__(self, flavor: _Optional[_Union[Flavor, str]] = ..., settings: _Optional[_Union[Settings, _Mapping]] = ...) -> None: ...

class Settings(_message.Message):
    __slots__ = ("auto_settings", "manual_settings")
    AUTO_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MANUAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    auto_settings: AutoSettings
    manual_settings: ManualSettings
    def __init__(self, auto_settings: _Optional[_Union[AutoSettings, _Mapping]] = ..., manual_settings: _Optional[_Union[ManualSettings, _Mapping]] = ...) -> None: ...

class AutoSettings(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ManualSettings(_message.Message):
    __slots__ = ("network_id",)
    NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    network_id: str
    def __init__(self, network_id: _Optional[str] = ...) -> None: ...

class MaskFunction(_message.Message):
    __slots__ = ("mask_function_hash",)
    MASK_FUNCTION_HASH_FIELD_NUMBER: _ClassVar[int]
    mask_function_hash: MaskFunctionHash
    def __init__(self, mask_function_hash: _Optional[_Union[MaskFunctionHash, _Mapping]] = ...) -> None: ...

class MaskFunctionHash(_message.Message):
    __slots__ = ("user_defined_salt",)
    USER_DEFINED_SALT_FIELD_NUMBER: _ClassVar[int]
    user_defined_salt: str
    def __init__(self, user_defined_salt: _Optional[str] = ...) -> None: ...

class TablesFilter(_message.Message):
    __slots__ = ("include_tables", "exclude_tables")
    INCLUDE_TABLES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_TABLES_FIELD_NUMBER: _ClassVar[int]
    include_tables: _containers.RepeatedScalarFieldContainer[str]
    exclude_tables: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, include_tables: _Optional[_Iterable[str]] = ..., exclude_tables: _Optional[_Iterable[str]] = ...) -> None: ...

class ColumnsFilter(_message.Message):
    __slots__ = ("include_columns", "exclude_columns")
    INCLUDE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    include_columns: _containers.RepeatedScalarFieldContainer[str]
    exclude_columns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, include_columns: _Optional[_Iterable[str]] = ..., exclude_columns: _Optional[_Iterable[str]] = ...) -> None: ...

class MaskFieldTransformer(_message.Message):
    __slots__ = ("tables", "columns", "function")
    TABLES_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    tables: TablesFilter
    columns: _containers.RepeatedScalarFieldContainer[str]
    function: MaskFunction
    def __init__(self, tables: _Optional[_Union[TablesFilter, _Mapping]] = ..., columns: _Optional[_Iterable[str]] = ..., function: _Optional[_Union[MaskFunction, _Mapping]] = ...) -> None: ...

class FilterColumnsTransformer(_message.Message):
    __slots__ = ("tables", "columns")
    TABLES_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    tables: TablesFilter
    columns: ColumnsFilter
    def __init__(self, tables: _Optional[_Union[TablesFilter, _Mapping]] = ..., columns: _Optional[_Union[ColumnsFilter, _Mapping]] = ...) -> None: ...

class Table(_message.Message):
    __slots__ = ("name_space", "name")
    NAME_SPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name_space: str
    name: str
    def __init__(self, name_space: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class RenameTable(_message.Message):
    __slots__ = ("original_name", "new_name")
    ORIGINAL_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    original_name: Table
    new_name: Table
    def __init__(self, original_name: _Optional[_Union[Table, _Mapping]] = ..., new_name: _Optional[_Union[Table, _Mapping]] = ...) -> None: ...

class RenameTablesTransformer(_message.Message):
    __slots__ = ("rename_tables",)
    RENAME_TABLES_FIELD_NUMBER: _ClassVar[int]
    rename_tables: _containers.RepeatedCompositeFieldContainer[RenameTable]
    def __init__(self, rename_tables: _Optional[_Iterable[_Union[RenameTable, _Mapping]]] = ...) -> None: ...

class SkipEventsTransformer(_message.Message):
    __slots__ = ("tables",)
    TABLES_FIELD_NUMBER: _ClassVar[int]
    tables: TablesFilter
    def __init__(self, tables: _Optional[_Union[TablesFilter, _Mapping]] = ...) -> None: ...

class ReplacePrimaryKeyTransformer(_message.Message):
    __slots__ = ("tables", "keys")
    TABLES_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    tables: TablesFilter
    keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tables: _Optional[_Union[TablesFilter, _Mapping]] = ..., keys: _Optional[_Iterable[str]] = ...) -> None: ...

class ToStringTransformer(_message.Message):
    __slots__ = ("tables", "columns")
    TABLES_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    tables: TablesFilter
    columns: ColumnsFilter
    def __init__(self, tables: _Optional[_Union[TablesFilter, _Mapping]] = ..., columns: _Optional[_Union[ColumnsFilter, _Mapping]] = ...) -> None: ...

class SharderTransformer(_message.Message):
    __slots__ = ("tables", "columns", "shards_count")
    TABLES_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    SHARDS_COUNT_FIELD_NUMBER: _ClassVar[int]
    tables: TablesFilter
    columns: ColumnsFilter
    shards_count: int
    def __init__(self, tables: _Optional[_Union[TablesFilter, _Mapping]] = ..., columns: _Optional[_Union[ColumnsFilter, _Mapping]] = ..., shards_count: _Optional[int] = ...) -> None: ...

class RawDocGroupTransformer(_message.Message):
    __slots__ = ("tables", "keys", "fields")
    TABLES_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    tables: TablesFilter
    keys: _containers.RepeatedScalarFieldContainer[str]
    fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tables: _Optional[_Union[TablesFilter, _Mapping]] = ..., keys: _Optional[_Iterable[str]] = ..., fields: _Optional[_Iterable[str]] = ...) -> None: ...

class RawCdcDocGroupTransformer(_message.Message):
    __slots__ = ("keys", "fields")
    KEYS_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[str]
    fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, keys: _Optional[_Iterable[str]] = ..., fields: _Optional[_Iterable[str]] = ...) -> None: ...

class SQLTransformer(_message.Message):
    __slots__ = ("tables", "query")
    TABLES_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    tables: TablesFilter
    query: str
    def __init__(self, tables: _Optional[_Union[TablesFilter, _Mapping]] = ..., query: _Optional[str] = ...) -> None: ...

class DBTTransformer(_message.Message):
    __slots__ = ("git_repository_link", "git_branch", "profile_name", "operation")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_UNSPECIFIED: _ClassVar[DBTTransformer.Operation]
        OPERATION_BUILD: _ClassVar[DBTTransformer.Operation]
        OPERATION_COMPILE: _ClassVar[DBTTransformer.Operation]
        OPERATION_DEBUG: _ClassVar[DBTTransformer.Operation]
        OPERATION_PARSE: _ClassVar[DBTTransformer.Operation]
        OPERATION_RUN: _ClassVar[DBTTransformer.Operation]
        OPERATION_SEED: _ClassVar[DBTTransformer.Operation]
        OPERATION_SNAPSHOT: _ClassVar[DBTTransformer.Operation]
        OPERATION_TEST: _ClassVar[DBTTransformer.Operation]
    OPERATION_UNSPECIFIED: DBTTransformer.Operation
    OPERATION_BUILD: DBTTransformer.Operation
    OPERATION_COMPILE: DBTTransformer.Operation
    OPERATION_DEBUG: DBTTransformer.Operation
    OPERATION_PARSE: DBTTransformer.Operation
    OPERATION_RUN: DBTTransformer.Operation
    OPERATION_SEED: DBTTransformer.Operation
    OPERATION_SNAPSHOT: DBTTransformer.Operation
    OPERATION_TEST: DBTTransformer.Operation
    GIT_REPOSITORY_LINK_FIELD_NUMBER: _ClassVar[int]
    GIT_BRANCH_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    git_repository_link: str
    git_branch: str
    profile_name: str
    operation: DBTTransformer.Operation
    def __init__(self, git_repository_link: _Optional[str] = ..., git_branch: _Optional[str] = ..., profile_name: _Optional[str] = ..., operation: _Optional[_Union[DBTTransformer.Operation, str]] = ...) -> None: ...

class TableSplitterTransformer(_message.Message):
    __slots__ = ("tables", "columns", "splitter")
    TABLES_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    SPLITTER_FIELD_NUMBER: _ClassVar[int]
    tables: TablesFilter
    columns: _containers.RepeatedScalarFieldContainer[str]
    splitter: str
    def __init__(self, tables: _Optional[_Union[TablesFilter, _Mapping]] = ..., columns: _Optional[_Iterable[str]] = ..., splitter: _Optional[str] = ...) -> None: ...

class FilterRowsTransformer(_message.Message):
    __slots__ = ("tables", "filter")
    TABLES_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    tables: TablesFilter
    filter: str
    def __init__(self, tables: _Optional[_Union[TablesFilter, _Mapping]] = ..., filter: _Optional[str] = ...) -> None: ...

class NumberToFloatTransformer(_message.Message):
    __slots__ = ("tables",)
    TABLES_FIELD_NUMBER: _ClassVar[int]
    tables: TablesFilter
    def __init__(self, tables: _Optional[_Union[TablesFilter, _Mapping]] = ...) -> None: ...

class Transformer(_message.Message):
    __slots__ = ("mask_field", "filter_columns", "skip_events", "rename_tables", "replace_primary_key", "convert_to_string", "sharder_transformer", "sql", "dbt", "table_splitter_transformer", "filter_rows", "number_to_float_transformer", "json_mapper_transformer", "cloud_function_transformer")
    MASK_FIELD_FIELD_NUMBER: _ClassVar[int]
    FILTER_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    SKIP_EVENTS_FIELD_NUMBER: _ClassVar[int]
    RENAME_TABLES_FIELD_NUMBER: _ClassVar[int]
    REPLACE_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    CONVERT_TO_STRING_FIELD_NUMBER: _ClassVar[int]
    SHARDER_TRANSFORMER_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    DBT_FIELD_NUMBER: _ClassVar[int]
    TABLE_SPLITTER_TRANSFORMER_FIELD_NUMBER: _ClassVar[int]
    FILTER_ROWS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_TO_FLOAT_TRANSFORMER_FIELD_NUMBER: _ClassVar[int]
    JSON_MAPPER_TRANSFORMER_FIELD_NUMBER: _ClassVar[int]
    CLOUD_FUNCTION_TRANSFORMER_FIELD_NUMBER: _ClassVar[int]
    mask_field: MaskFieldTransformer
    filter_columns: FilterColumnsTransformer
    skip_events: SkipEventsTransformer
    rename_tables: RenameTablesTransformer
    replace_primary_key: ReplacePrimaryKeyTransformer
    convert_to_string: ToStringTransformer
    sharder_transformer: SharderTransformer
    sql: SQLTransformer
    dbt: DBTTransformer
    table_splitter_transformer: TableSplitterTransformer
    filter_rows: FilterRowsTransformer
    number_to_float_transformer: NumberToFloatTransformer
    json_mapper_transformer: JsonParserTransformer
    cloud_function_transformer: CloudFunctionTransformer
    def __init__(self, mask_field: _Optional[_Union[MaskFieldTransformer, _Mapping]] = ..., filter_columns: _Optional[_Union[FilterColumnsTransformer, _Mapping]] = ..., skip_events: _Optional[_Union[SkipEventsTransformer, _Mapping]] = ..., rename_tables: _Optional[_Union[RenameTablesTransformer, _Mapping]] = ..., replace_primary_key: _Optional[_Union[ReplacePrimaryKeyTransformer, _Mapping]] = ..., convert_to_string: _Optional[_Union[ToStringTransformer, _Mapping]] = ..., sharder_transformer: _Optional[_Union[SharderTransformer, _Mapping]] = ..., sql: _Optional[_Union[SQLTransformer, _Mapping]] = ..., dbt: _Optional[_Union[DBTTransformer, _Mapping]] = ..., table_splitter_transformer: _Optional[_Union[TableSplitterTransformer, _Mapping]] = ..., filter_rows: _Optional[_Union[FilterRowsTransformer, _Mapping]] = ..., number_to_float_transformer: _Optional[_Union[NumberToFloatTransformer, _Mapping]] = ..., json_mapper_transformer: _Optional[_Union[JsonParserTransformer, _Mapping]] = ..., cloud_function_transformer: _Optional[_Union[CloudFunctionTransformer, _Mapping]] = ...) -> None: ...

class CloudFunctionTransformer(_message.Message):
    __slots__ = ("name", "name_space", "options")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_SPACE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    name_space: str
    options: _common_pb2.DataTransformationOptions
    def __init__(self, name: _Optional[str] = ..., name_space: _Optional[str] = ..., options: _Optional[_Union[_common_pb2.DataTransformationOptions, _Mapping]] = ...) -> None: ...

class JsonParserTransformer(_message.Message):
    __slots__ = ("topic", "config")
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    topic: str
    config: _parsers_pb2.GenericParserCommon
    def __init__(self, topic: _Optional[str] = ..., config: _Optional[_Union[_parsers_pb2.GenericParserCommon, _Mapping]] = ...) -> None: ...

class Transformation(_message.Message):
    __slots__ = ("transformers",)
    TRANSFORMERS_FIELD_NUMBER: _ClassVar[int]
    transformers: _containers.RepeatedCompositeFieldContainer[Transformer]
    def __init__(self, transformers: _Optional[_Iterable[_Union[Transformer, _Mapping]]] = ...) -> None: ...

class DataObjects(_message.Message):
    __slots__ = ("include_objects",)
    INCLUDE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    include_objects: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, include_objects: _Optional[_Iterable[str]] = ...) -> None: ...
