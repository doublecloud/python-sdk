from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("name", "cluster_id", "default_roles", "grantees", "privileges", "settings", "quota_names", "assigned_roles")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ROLES_FIELD_NUMBER: _ClassVar[int]
    GRANTEES_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    QUOTA_NAMES_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_ROLES_FIELD_NUMBER: _ClassVar[int]
    name: str
    cluster_id: str
    default_roles: DefaultRoles
    grantees: Grantees
    privileges: Privileges
    settings: Settings
    quota_names: QuotaNames
    assigned_roles: AssignedRoles
    def __init__(self, name: _Optional[str] = ..., cluster_id: _Optional[str] = ..., default_roles: _Optional[_Union[DefaultRoles, _Mapping]] = ..., grantees: _Optional[_Union[Grantees, _Mapping]] = ..., privileges: _Optional[_Union[Privileges, _Mapping]] = ..., settings: _Optional[_Union[Settings, _Mapping]] = ..., quota_names: _Optional[_Union[QuotaNames, _Mapping]] = ..., assigned_roles: _Optional[_Union[AssignedRoles, _Mapping]] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ("name", "cluster_id", "privileges", "settings", "quota_names")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGES_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    QUOTA_NAMES_FIELD_NUMBER: _ClassVar[int]
    name: str
    cluster_id: str
    privileges: Privileges
    settings: Settings
    quota_names: QuotaNames
    def __init__(self, name: _Optional[str] = ..., cluster_id: _Optional[str] = ..., privileges: _Optional[_Union[Privileges, _Mapping]] = ..., settings: _Optional[_Union[Settings, _Mapping]] = ..., quota_names: _Optional[_Union[QuotaNames, _Mapping]] = ...) -> None: ...

class Authentication(_message.Message):
    __slots__ = ("type", "password")
    class IdentificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IDENTIFICATION_TYPE_INVALID: _ClassVar[Authentication.IdentificationType]
        IDENTIFICATION_TYPE_SHA256_PASSWORD: _ClassVar[Authentication.IdentificationType]
        IDENTIFICATION_TYPE_DOUBLE_SHA1_PASSWORD: _ClassVar[Authentication.IdentificationType]
        IDENTIFICATION_TYPE_BCRYPT_PASSWORD: _ClassVar[Authentication.IdentificationType]
    IDENTIFICATION_TYPE_INVALID: Authentication.IdentificationType
    IDENTIFICATION_TYPE_SHA256_PASSWORD: Authentication.IdentificationType
    IDENTIFICATION_TYPE_DOUBLE_SHA1_PASSWORD: Authentication.IdentificationType
    IDENTIFICATION_TYPE_BCRYPT_PASSWORD: Authentication.IdentificationType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    type: Authentication.IdentificationType
    password: _wrappers_pb2.StringValue
    def __init__(self, type: _Optional[_Union[Authentication.IdentificationType, str]] = ..., password: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class DefaultRoles(_message.Message):
    __slots__ = ("all", "list")
    ALL_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    EXCEPT_FIELD_NUMBER: _ClassVar[int]
    all: bool
    list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, all: bool = ..., list: _Optional[_Iterable[str]] = ..., **kwargs) -> None: ...

class AssignedRoles(_message.Message):
    __slots__ = ("roles",)
    ROLES_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, roles: _Optional[_Iterable[str]] = ...) -> None: ...

class Grantees(_message.Message):
    __slots__ = ("any", "list")
    ANY_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    EXCEPT_FIELD_NUMBER: _ClassVar[int]
    any: bool
    list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, any: bool = ..., list: _Optional[_Iterable[str]] = ..., **kwargs) -> None: ...

class Privileges(_message.Message):
    __slots__ = ("grants",)
    GRANTS_FIELD_NUMBER: _ClassVar[int]
    grants: _containers.RepeatedCompositeFieldContainer[Grant]
    def __init__(self, grants: _Optional[_Iterable[_Union[Grant, _Mapping]]] = ...) -> None: ...

class QuotaNames(_message.Message):
    __slots__ = ("names",)
    NAMES_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, names: _Optional[_Iterable[str]] = ...) -> None: ...

class Grant(_message.Message):
    __slots__ = ("access_type", "database", "table", "columns", "is_partial_revoke", "grant_option")
    class AccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACCESS_TYPE_INVALID: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SHOW_DATABASES: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SHOW_TABLES: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SHOW_COLUMNS: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SHOW_DICTIONARIES: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SHOW: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SHOW_FILESYSTEM_CACHES: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SELECT: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_INSERT: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_UPDATE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_DELETE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_ADD_COLUMN: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_MODIFY_COLUMN: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_DROP_COLUMN: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_COMMENT_COLUMN: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_CLEAR_COLUMN: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_RENAME_COLUMN: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_MATERIALIZE_COLUMN: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_COLUMN: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_MODIFY_COMMENT: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_ORDER_BY: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_SAMPLE_BY: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_ADD_INDEX: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_DROP_INDEX: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_MATERIALIZE_INDEX: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_CLEAR_INDEX: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_INDEX: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_ADD_PROJECTION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_DROP_PROJECTION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_MATERIALIZE_PROJECTION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_CLEAR_PROJECTION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_PROJECTION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_ADD_CONSTRAINT: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_DROP_CONSTRAINT: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_CONSTRAINT: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_TTL: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_MATERIALIZE_TTL: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_SETTINGS: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_MOVE_PARTITION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_FETCH_PARTITION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_FREEZE_PARTITION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_DATABASE_SETTINGS: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_NAMED_COLLECTION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_TABLE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_DATABASE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_VIEW_REFRESH: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_VIEW_MODIFY_QUERY: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_VIEW: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_CREATE_DATABASE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_CREATE_TABLE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_CREATE_VIEW: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_CREATE_DICTIONARY: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_CREATE_TEMPORARY_TABLE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_CREATE_ARBITRARY_TEMPORARY_TABLE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_CREATE_FUNCTION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_CREATE_NAMED_COLLECTION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_CREATE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_DROP_DATABASE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_DROP_TABLE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_DROP_VIEW: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_DROP_DICTIONARY: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_DROP_FUNCTION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_DROP_NAMED_COLLECTION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_DROP: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_UNDROP_TABLE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_TRUNCATE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_OPTIMIZE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_BACKUP: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_KILL_QUERY: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_KILL_TRANSACTION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_MOVE_PARTITION_BETWEEN_SHARDS: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_CREATE_USER: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_USER: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_DROP_USER: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_CREATE_ROLE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_ROLE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_DROP_ROLE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ROLE_ADMIN: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_CREATE_ROW_POLICY: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_ROW_POLICY: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_DROP_ROW_POLICY: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_CREATE_QUOTA: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_QUOTA: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_DROP_QUOTA: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_CREATE_SETTINGS_PROFILE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALTER_SETTINGS_PROFILE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_DROP_SETTINGS_PROFILE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SHOW_USERS: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SHOW_ROLES: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SHOW_ROW_POLICIES: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SHOW_QUOTAS: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SHOW_SETTINGS_PROFILES: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SHOW_ACCESS: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ACCESS_MANAGEMENT: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_NAMED_COLLECTION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SYSTEM_DROP_CACHE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SYSTEM_RELOAD: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SYSTEM_MERGES: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SYSTEM_TTL_MERGES: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SYSTEM_FETCHES: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SYSTEM_MOVES: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SYSTEM_SENDS: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SYSTEM_REPLICATION_QUEUES: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SYSTEM_DROP_REPLICA: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SYSTEM_SYNC_REPLICA: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SYSTEM_RESTART_REPLICA: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SYSTEM_RESTORE_REPLICA: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_SYSTEM_FLUSH: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_DICT_GET: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_INTROSPECTION: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_URL: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_REMOTE: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_MONGO: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_MYSQL: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_POSTGRES: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ODBC: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_JDBC: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_HDFS: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_S3: _ClassVar[Grant.AccessType]
        ACCESS_TYPE_ALL: _ClassVar[Grant.AccessType]
    ACCESS_TYPE_INVALID: Grant.AccessType
    ACCESS_TYPE_SHOW_DATABASES: Grant.AccessType
    ACCESS_TYPE_SHOW_TABLES: Grant.AccessType
    ACCESS_TYPE_SHOW_COLUMNS: Grant.AccessType
    ACCESS_TYPE_SHOW_DICTIONARIES: Grant.AccessType
    ACCESS_TYPE_SHOW: Grant.AccessType
    ACCESS_TYPE_SHOW_FILESYSTEM_CACHES: Grant.AccessType
    ACCESS_TYPE_SELECT: Grant.AccessType
    ACCESS_TYPE_INSERT: Grant.AccessType
    ACCESS_TYPE_ALTER_UPDATE: Grant.AccessType
    ACCESS_TYPE_ALTER_DELETE: Grant.AccessType
    ACCESS_TYPE_ALTER_ADD_COLUMN: Grant.AccessType
    ACCESS_TYPE_ALTER_MODIFY_COLUMN: Grant.AccessType
    ACCESS_TYPE_ALTER_DROP_COLUMN: Grant.AccessType
    ACCESS_TYPE_ALTER_COMMENT_COLUMN: Grant.AccessType
    ACCESS_TYPE_ALTER_CLEAR_COLUMN: Grant.AccessType
    ACCESS_TYPE_ALTER_RENAME_COLUMN: Grant.AccessType
    ACCESS_TYPE_ALTER_MATERIALIZE_COLUMN: Grant.AccessType
    ACCESS_TYPE_ALTER_COLUMN: Grant.AccessType
    ACCESS_TYPE_ALTER_MODIFY_COMMENT: Grant.AccessType
    ACCESS_TYPE_ALTER_ORDER_BY: Grant.AccessType
    ACCESS_TYPE_ALTER_SAMPLE_BY: Grant.AccessType
    ACCESS_TYPE_ALTER_ADD_INDEX: Grant.AccessType
    ACCESS_TYPE_ALTER_DROP_INDEX: Grant.AccessType
    ACCESS_TYPE_ALTER_MATERIALIZE_INDEX: Grant.AccessType
    ACCESS_TYPE_ALTER_CLEAR_INDEX: Grant.AccessType
    ACCESS_TYPE_ALTER_INDEX: Grant.AccessType
    ACCESS_TYPE_ALTER_ADD_PROJECTION: Grant.AccessType
    ACCESS_TYPE_ALTER_DROP_PROJECTION: Grant.AccessType
    ACCESS_TYPE_ALTER_MATERIALIZE_PROJECTION: Grant.AccessType
    ACCESS_TYPE_ALTER_CLEAR_PROJECTION: Grant.AccessType
    ACCESS_TYPE_ALTER_PROJECTION: Grant.AccessType
    ACCESS_TYPE_ALTER_ADD_CONSTRAINT: Grant.AccessType
    ACCESS_TYPE_ALTER_DROP_CONSTRAINT: Grant.AccessType
    ACCESS_TYPE_ALTER_CONSTRAINT: Grant.AccessType
    ACCESS_TYPE_ALTER_TTL: Grant.AccessType
    ACCESS_TYPE_ALTER_MATERIALIZE_TTL: Grant.AccessType
    ACCESS_TYPE_ALTER_SETTINGS: Grant.AccessType
    ACCESS_TYPE_ALTER_MOVE_PARTITION: Grant.AccessType
    ACCESS_TYPE_ALTER_FETCH_PARTITION: Grant.AccessType
    ACCESS_TYPE_ALTER_FREEZE_PARTITION: Grant.AccessType
    ACCESS_TYPE_ALTER_DATABASE_SETTINGS: Grant.AccessType
    ACCESS_TYPE_ALTER_NAMED_COLLECTION: Grant.AccessType
    ACCESS_TYPE_ALTER_TABLE: Grant.AccessType
    ACCESS_TYPE_ALTER_DATABASE: Grant.AccessType
    ACCESS_TYPE_ALTER_VIEW_REFRESH: Grant.AccessType
    ACCESS_TYPE_ALTER_VIEW_MODIFY_QUERY: Grant.AccessType
    ACCESS_TYPE_ALTER_VIEW: Grant.AccessType
    ACCESS_TYPE_ALTER: Grant.AccessType
    ACCESS_TYPE_CREATE_DATABASE: Grant.AccessType
    ACCESS_TYPE_CREATE_TABLE: Grant.AccessType
    ACCESS_TYPE_CREATE_VIEW: Grant.AccessType
    ACCESS_TYPE_CREATE_DICTIONARY: Grant.AccessType
    ACCESS_TYPE_CREATE_TEMPORARY_TABLE: Grant.AccessType
    ACCESS_TYPE_CREATE_ARBITRARY_TEMPORARY_TABLE: Grant.AccessType
    ACCESS_TYPE_CREATE_FUNCTION: Grant.AccessType
    ACCESS_TYPE_CREATE_NAMED_COLLECTION: Grant.AccessType
    ACCESS_TYPE_CREATE: Grant.AccessType
    ACCESS_TYPE_DROP_DATABASE: Grant.AccessType
    ACCESS_TYPE_DROP_TABLE: Grant.AccessType
    ACCESS_TYPE_DROP_VIEW: Grant.AccessType
    ACCESS_TYPE_DROP_DICTIONARY: Grant.AccessType
    ACCESS_TYPE_DROP_FUNCTION: Grant.AccessType
    ACCESS_TYPE_DROP_NAMED_COLLECTION: Grant.AccessType
    ACCESS_TYPE_DROP: Grant.AccessType
    ACCESS_TYPE_UNDROP_TABLE: Grant.AccessType
    ACCESS_TYPE_TRUNCATE: Grant.AccessType
    ACCESS_TYPE_OPTIMIZE: Grant.AccessType
    ACCESS_TYPE_BACKUP: Grant.AccessType
    ACCESS_TYPE_KILL_QUERY: Grant.AccessType
    ACCESS_TYPE_KILL_TRANSACTION: Grant.AccessType
    ACCESS_TYPE_MOVE_PARTITION_BETWEEN_SHARDS: Grant.AccessType
    ACCESS_TYPE_CREATE_USER: Grant.AccessType
    ACCESS_TYPE_ALTER_USER: Grant.AccessType
    ACCESS_TYPE_DROP_USER: Grant.AccessType
    ACCESS_TYPE_CREATE_ROLE: Grant.AccessType
    ACCESS_TYPE_ALTER_ROLE: Grant.AccessType
    ACCESS_TYPE_DROP_ROLE: Grant.AccessType
    ACCESS_TYPE_ROLE_ADMIN: Grant.AccessType
    ACCESS_TYPE_CREATE_ROW_POLICY: Grant.AccessType
    ACCESS_TYPE_ALTER_ROW_POLICY: Grant.AccessType
    ACCESS_TYPE_DROP_ROW_POLICY: Grant.AccessType
    ACCESS_TYPE_CREATE_QUOTA: Grant.AccessType
    ACCESS_TYPE_ALTER_QUOTA: Grant.AccessType
    ACCESS_TYPE_DROP_QUOTA: Grant.AccessType
    ACCESS_TYPE_CREATE_SETTINGS_PROFILE: Grant.AccessType
    ACCESS_TYPE_ALTER_SETTINGS_PROFILE: Grant.AccessType
    ACCESS_TYPE_DROP_SETTINGS_PROFILE: Grant.AccessType
    ACCESS_TYPE_SHOW_USERS: Grant.AccessType
    ACCESS_TYPE_SHOW_ROLES: Grant.AccessType
    ACCESS_TYPE_SHOW_ROW_POLICIES: Grant.AccessType
    ACCESS_TYPE_SHOW_QUOTAS: Grant.AccessType
    ACCESS_TYPE_SHOW_SETTINGS_PROFILES: Grant.AccessType
    ACCESS_TYPE_SHOW_ACCESS: Grant.AccessType
    ACCESS_TYPE_ACCESS_MANAGEMENT: Grant.AccessType
    ACCESS_TYPE_NAMED_COLLECTION: Grant.AccessType
    ACCESS_TYPE_SYSTEM_DROP_CACHE: Grant.AccessType
    ACCESS_TYPE_SYSTEM_RELOAD: Grant.AccessType
    ACCESS_TYPE_SYSTEM_MERGES: Grant.AccessType
    ACCESS_TYPE_SYSTEM_TTL_MERGES: Grant.AccessType
    ACCESS_TYPE_SYSTEM_FETCHES: Grant.AccessType
    ACCESS_TYPE_SYSTEM_MOVES: Grant.AccessType
    ACCESS_TYPE_SYSTEM_SENDS: Grant.AccessType
    ACCESS_TYPE_SYSTEM_REPLICATION_QUEUES: Grant.AccessType
    ACCESS_TYPE_SYSTEM_DROP_REPLICA: Grant.AccessType
    ACCESS_TYPE_SYSTEM_SYNC_REPLICA: Grant.AccessType
    ACCESS_TYPE_SYSTEM_RESTART_REPLICA: Grant.AccessType
    ACCESS_TYPE_SYSTEM_RESTORE_REPLICA: Grant.AccessType
    ACCESS_TYPE_SYSTEM_FLUSH: Grant.AccessType
    ACCESS_TYPE_DICT_GET: Grant.AccessType
    ACCESS_TYPE_INTROSPECTION: Grant.AccessType
    ACCESS_TYPE_URL: Grant.AccessType
    ACCESS_TYPE_REMOTE: Grant.AccessType
    ACCESS_TYPE_MONGO: Grant.AccessType
    ACCESS_TYPE_MYSQL: Grant.AccessType
    ACCESS_TYPE_POSTGRES: Grant.AccessType
    ACCESS_TYPE_ODBC: Grant.AccessType
    ACCESS_TYPE_JDBC: Grant.AccessType
    ACCESS_TYPE_HDFS: Grant.AccessType
    ACCESS_TYPE_S3: Grant.AccessType
    ACCESS_TYPE_ALL: Grant.AccessType
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    IS_PARTIAL_REVOKE_FIELD_NUMBER: _ClassVar[int]
    GRANT_OPTION_FIELD_NUMBER: _ClassVar[int]
    access_type: Grant.AccessType
    database: str
    table: str
    columns: _containers.RepeatedScalarFieldContainer[str]
    is_partial_revoke: bool
    grant_option: bool
    def __init__(self, access_type: _Optional[_Union[Grant.AccessType, str]] = ..., database: _Optional[str] = ..., table: _Optional[str] = ..., columns: _Optional[_Iterable[str]] = ..., is_partial_revoke: bool = ..., grant_option: bool = ...) -> None: ...

class Settings(_message.Message):
    __slots__ = ("readonly", "allow_ddl", "insert_quorum", "insert_quorum_timeout", "select_sequential_consistency", "max_replica_delay_for_distributed_queries", "fallback_to_stale_replicas_for_distributed_queries", "max_threads", "max_block_size", "max_insert_block_size", "max_memory_usage", "max_memory_usage_for_user", "max_rows_to_read", "max_bytes_to_read", "read_overflow_mode", "max_rows_to_group_by", "group_by_overflow_mode", "max_rows_to_sort", "max_bytes_to_sort", "sort_overflow_mode", "max_result_rows", "max_result_bytes", "result_overflow_mode", "max_rows_in_distinct", "max_bytes_in_distinct", "distinct_overflow_mode", "max_rows_to_transfer", "max_bytes_to_transfer", "transfer_overflow_mode", "max_execution_time", "timeout_overflow_mode", "max_columns_to_read", "max_temporary_columns", "max_temporary_non_const_columns", "max_query_size", "max_ast_depth", "max_ast_elements", "max_expanded_ast_elements", "connect_timeout", "receive_timeout", "send_timeout", "replication_alter_partitions_sync", "distributed_product_mode", "compile_expressions", "min_count_to_compile_expression", "min_insert_block_size_rows", "min_insert_block_size_bytes", "min_bytes_to_use_direct_io", "use_uncompressed_cache", "merge_tree_max_rows_to_use_cache", "merge_tree_max_bytes_to_use_cache", "merge_tree_min_rows_for_concurrent_read", "merge_tree_min_bytes_for_concurrent_read", "priority", "max_network_bandwidth", "max_network_bandwidth_for_user", "force_index_by_date", "force_primary_key", "input_format_values_interpret_expressions", "input_format_defaults_for_omitted_fields", "output_format_json_quote_64bit_integers", "output_format_json_quote_denormals", "http_connection_timeout", "http_receive_timeout", "http_send_timeout", "enable_http_compression", "send_progress_in_http_headers", "http_headers_progress_interval", "add_http_cors_header", "distributed_aggregation_memory_efficient", "distributed_ddl_task_timeout", "max_bytes_before_external_group_by", "max_bytes_before_external_sort", "group_by_two_level_threshold", "group_by_two_level_threshold_bytes", "low_cardinality_allow_in_native_format", "empty_result_for_aggregation_by_empty_set", "skip_unavailable_shards", "min_execution_speed", "min_execution_speed_bytes", "count_distinct_implementation", "max_rows_in_set", "max_bytes_in_set", "set_overflow_mode", "max_rows_in_join", "max_bytes_in_join", "join_overflow_mode", "joined_subquery_requires_alias", "join_use_nulls", "transform_null_in", "allow_introspection_functions", "connect_timeout_with_failover", "timeout_before_checking_execution_speed", "insert_quorum_parallel", "insert_null_as_default", "deduplicate_blocks_in_dependent_materialized_views", "max_partitions_per_insert_block", "max_concurrent_queries_for_user", "join_algorithm", "any_join_distinct_right_table_keys", "input_format_null_as_default", "date_time_input_format", "input_format_with_names_use_header", "date_time_output_format", "allow_suspicious_low_cardinality_types", "cancel_http_readonly_queries_on_client_close", "max_http_get_redirects", "flatten_nested", "format_regexp", "format_regexp_escaping_rule", "format_regexp_skip_unmatched", "async_insert", "async_insert_threads", "wait_for_async_insert", "wait_for_async_insert_timeout", "async_insert_max_data_size", "async_insert_busy_timeout", "async_insert_stale_timeout", "memory_profiler_step", "memory_profiler_sample_probability", "max_final_threads", "input_format_parallel_parsing", "input_format_import_nested_json", "local_filesystem_read_method", "max_read_buffer_size", "insert_keeper_max_retries", "max_temporary_data_on_disk_size_for_user", "max_temporary_data_on_disk_size_for_query", "max_parser_depth", "remote_filesystem_read_method", "memory_overcommit_ratio_denominator", "memory_overcommit_ratio_denominator_for_user", "memory_usage_overcommit_max_wait_microseconds")
    class Writability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WRITABILITY_INVALID: _ClassVar[Settings.Writability]
        WRITABILITY_CONST: _ClassVar[Settings.Writability]
        WRITABILITY_WRITABLE: _ClassVar[Settings.Writability]
        WRITABILITY_CHANGEABLE_IN_READONLY: _ClassVar[Settings.Writability]
    WRITABILITY_INVALID: Settings.Writability
    WRITABILITY_CONST: Settings.Writability
    WRITABILITY_WRITABLE: Settings.Writability
    WRITABILITY_CHANGEABLE_IN_READONLY: Settings.Writability
    class OverflowMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OVERFLOW_MODE_INVALID: _ClassVar[Settings.OverflowMode]
        OVERFLOW_MODE_THROW: _ClassVar[Settings.OverflowMode]
        OVERFLOW_MODE_BREAK: _ClassVar[Settings.OverflowMode]
    OVERFLOW_MODE_INVALID: Settings.OverflowMode
    OVERFLOW_MODE_THROW: Settings.OverflowMode
    OVERFLOW_MODE_BREAK: Settings.OverflowMode
    class GroupByOverflowMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GROUP_BY_OVERFLOW_MODE_INVALID: _ClassVar[Settings.GroupByOverflowMode]
        GROUP_BY_OVERFLOW_MODE_THROW: _ClassVar[Settings.GroupByOverflowMode]
        GROUP_BY_OVERFLOW_MODE_BREAK: _ClassVar[Settings.GroupByOverflowMode]
        GROUP_BY_OVERFLOW_MODE_ANY: _ClassVar[Settings.GroupByOverflowMode]
    GROUP_BY_OVERFLOW_MODE_INVALID: Settings.GroupByOverflowMode
    GROUP_BY_OVERFLOW_MODE_THROW: Settings.GroupByOverflowMode
    GROUP_BY_OVERFLOW_MODE_BREAK: Settings.GroupByOverflowMode
    GROUP_BY_OVERFLOW_MODE_ANY: Settings.GroupByOverflowMode
    class DistributedProductMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISTRIBUTED_PRODUCT_MODE_INVALID: _ClassVar[Settings.DistributedProductMode]
        DISTRIBUTED_PRODUCT_MODE_DENY: _ClassVar[Settings.DistributedProductMode]
        DISTRIBUTED_PRODUCT_MODE_LOCAL: _ClassVar[Settings.DistributedProductMode]
        DISTRIBUTED_PRODUCT_MODE_GLOBAL: _ClassVar[Settings.DistributedProductMode]
        DISTRIBUTED_PRODUCT_MODE_ALLOW: _ClassVar[Settings.DistributedProductMode]
    DISTRIBUTED_PRODUCT_MODE_INVALID: Settings.DistributedProductMode
    DISTRIBUTED_PRODUCT_MODE_DENY: Settings.DistributedProductMode
    DISTRIBUTED_PRODUCT_MODE_LOCAL: Settings.DistributedProductMode
    DISTRIBUTED_PRODUCT_MODE_GLOBAL: Settings.DistributedProductMode
    DISTRIBUTED_PRODUCT_MODE_ALLOW: Settings.DistributedProductMode
    class CountDistinctImplementation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COUNT_DISTINCT_IMPLEMENTATION_INVALID: _ClassVar[Settings.CountDistinctImplementation]
        COUNT_DISTINCT_IMPLEMENTATION_UNIQ: _ClassVar[Settings.CountDistinctImplementation]
        COUNT_DISTINCT_IMPLEMENTATION_UNIQ_COMBINED: _ClassVar[Settings.CountDistinctImplementation]
        COUNT_DISTINCT_IMPLEMENTATION_UNIQ_COMBINED_64: _ClassVar[Settings.CountDistinctImplementation]
        COUNT_DISTINCT_IMPLEMENTATION_UNIQ_HLL_12: _ClassVar[Settings.CountDistinctImplementation]
        COUNT_DISTINCT_IMPLEMENTATION_UNIQ_EXACT: _ClassVar[Settings.CountDistinctImplementation]
    COUNT_DISTINCT_IMPLEMENTATION_INVALID: Settings.CountDistinctImplementation
    COUNT_DISTINCT_IMPLEMENTATION_UNIQ: Settings.CountDistinctImplementation
    COUNT_DISTINCT_IMPLEMENTATION_UNIQ_COMBINED: Settings.CountDistinctImplementation
    COUNT_DISTINCT_IMPLEMENTATION_UNIQ_COMBINED_64: Settings.CountDistinctImplementation
    COUNT_DISTINCT_IMPLEMENTATION_UNIQ_HLL_12: Settings.CountDistinctImplementation
    COUNT_DISTINCT_IMPLEMENTATION_UNIQ_EXACT: Settings.CountDistinctImplementation
    class JoinAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        JOIN_ALGORITHM_INVALID: _ClassVar[Settings.JoinAlgorithm]
        JOIN_ALGORITHM_HASH: _ClassVar[Settings.JoinAlgorithm]
        JOIN_ALGORITHM_PARALLEL_HASH: _ClassVar[Settings.JoinAlgorithm]
        JOIN_ALGORITHM_PARTIAL_MERGE: _ClassVar[Settings.JoinAlgorithm]
        JOIN_ALGORITHM_DIRECT: _ClassVar[Settings.JoinAlgorithm]
        JOIN_ALGORITHM_AUTO: _ClassVar[Settings.JoinAlgorithm]
        JOIN_ALGORITHM_FULL_SORTING_MERGE: _ClassVar[Settings.JoinAlgorithm]
        JOIN_ALGORITHM_PREFER_PARTIAL_MERGE: _ClassVar[Settings.JoinAlgorithm]
    JOIN_ALGORITHM_INVALID: Settings.JoinAlgorithm
    JOIN_ALGORITHM_HASH: Settings.JoinAlgorithm
    JOIN_ALGORITHM_PARALLEL_HASH: Settings.JoinAlgorithm
    JOIN_ALGORITHM_PARTIAL_MERGE: Settings.JoinAlgorithm
    JOIN_ALGORITHM_DIRECT: Settings.JoinAlgorithm
    JOIN_ALGORITHM_AUTO: Settings.JoinAlgorithm
    JOIN_ALGORITHM_FULL_SORTING_MERGE: Settings.JoinAlgorithm
    JOIN_ALGORITHM_PREFER_PARTIAL_MERGE: Settings.JoinAlgorithm
    class FormatRegexpEscapingRule(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_REGEXP_ESCAPING_RULE_INVALID: _ClassVar[Settings.FormatRegexpEscapingRule]
        FORMAT_REGEXP_ESCAPING_RULE_ESCAPED: _ClassVar[Settings.FormatRegexpEscapingRule]
        FORMAT_REGEXP_ESCAPING_RULE_QUOTED: _ClassVar[Settings.FormatRegexpEscapingRule]
        FORMAT_REGEXP_ESCAPING_RULE_CSV: _ClassVar[Settings.FormatRegexpEscapingRule]
        FORMAT_REGEXP_ESCAPING_RULE_JSON: _ClassVar[Settings.FormatRegexpEscapingRule]
        FORMAT_REGEXP_ESCAPING_RULE_XML: _ClassVar[Settings.FormatRegexpEscapingRule]
        FORMAT_REGEXP_ESCAPING_RULE_RAW: _ClassVar[Settings.FormatRegexpEscapingRule]
    FORMAT_REGEXP_ESCAPING_RULE_INVALID: Settings.FormatRegexpEscapingRule
    FORMAT_REGEXP_ESCAPING_RULE_ESCAPED: Settings.FormatRegexpEscapingRule
    FORMAT_REGEXP_ESCAPING_RULE_QUOTED: Settings.FormatRegexpEscapingRule
    FORMAT_REGEXP_ESCAPING_RULE_CSV: Settings.FormatRegexpEscapingRule
    FORMAT_REGEXP_ESCAPING_RULE_JSON: Settings.FormatRegexpEscapingRule
    FORMAT_REGEXP_ESCAPING_RULE_XML: Settings.FormatRegexpEscapingRule
    FORMAT_REGEXP_ESCAPING_RULE_RAW: Settings.FormatRegexpEscapingRule
    class DateTimeInputFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATE_TIME_INPUT_FORMAT_INVALID: _ClassVar[Settings.DateTimeInputFormat]
        DATE_TIME_INPUT_FORMAT_BEST_EFFORT: _ClassVar[Settings.DateTimeInputFormat]
        DATE_TIME_INPUT_FORMAT_BASIC: _ClassVar[Settings.DateTimeInputFormat]
        DATE_TIME_INPUT_FORMAT_BEST_EFFORT_US: _ClassVar[Settings.DateTimeInputFormat]
    DATE_TIME_INPUT_FORMAT_INVALID: Settings.DateTimeInputFormat
    DATE_TIME_INPUT_FORMAT_BEST_EFFORT: Settings.DateTimeInputFormat
    DATE_TIME_INPUT_FORMAT_BASIC: Settings.DateTimeInputFormat
    DATE_TIME_INPUT_FORMAT_BEST_EFFORT_US: Settings.DateTimeInputFormat
    class DateTimeOutputFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATE_TIME_OUTPUT_FORMAT_INVALID: _ClassVar[Settings.DateTimeOutputFormat]
        DATE_TIME_OUTPUT_FORMAT_SIMPLE: _ClassVar[Settings.DateTimeOutputFormat]
        DATE_TIME_OUTPUT_FORMAT_ISO: _ClassVar[Settings.DateTimeOutputFormat]
        DATE_TIME_OUTPUT_FORMAT_UNIX_TIMESTAMP: _ClassVar[Settings.DateTimeOutputFormat]
    DATE_TIME_OUTPUT_FORMAT_INVALID: Settings.DateTimeOutputFormat
    DATE_TIME_OUTPUT_FORMAT_SIMPLE: Settings.DateTimeOutputFormat
    DATE_TIME_OUTPUT_FORMAT_ISO: Settings.DateTimeOutputFormat
    DATE_TIME_OUTPUT_FORMAT_UNIX_TIMESTAMP: Settings.DateTimeOutputFormat
    class LocalFilesystemReadMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCAL_FILESYSTEM_READ_METHOD_INVALID: _ClassVar[Settings.LocalFilesystemReadMethod]
        LOCAL_FILESYSTEM_READ_METHOD_READ: _ClassVar[Settings.LocalFilesystemReadMethod]
        LOCAL_FILESYSTEM_READ_METHOD_PREAD_THREADPOOL: _ClassVar[Settings.LocalFilesystemReadMethod]
        LOCAL_FILESYSTEM_READ_METHOD_PREAD: _ClassVar[Settings.LocalFilesystemReadMethod]
        LOCAL_FILESYSTEM_READ_METHOD_NMAP: _ClassVar[Settings.LocalFilesystemReadMethod]
    LOCAL_FILESYSTEM_READ_METHOD_INVALID: Settings.LocalFilesystemReadMethod
    LOCAL_FILESYSTEM_READ_METHOD_READ: Settings.LocalFilesystemReadMethod
    LOCAL_FILESYSTEM_READ_METHOD_PREAD_THREADPOOL: Settings.LocalFilesystemReadMethod
    LOCAL_FILESYSTEM_READ_METHOD_PREAD: Settings.LocalFilesystemReadMethod
    LOCAL_FILESYSTEM_READ_METHOD_NMAP: Settings.LocalFilesystemReadMethod
    class RemoteFilesystemReadMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REMOTE_FILESYSTEM_READ_METHOD_INVALID: _ClassVar[Settings.RemoteFilesystemReadMethod]
        REMOTE_FILESYSTEM_READ_METHOD_READ: _ClassVar[Settings.RemoteFilesystemReadMethod]
        REMOTE_FILESYSTEM_READ_METHOD_THREADPOOL: _ClassVar[Settings.RemoteFilesystemReadMethod]
    REMOTE_FILESYSTEM_READ_METHOD_INVALID: Settings.RemoteFilesystemReadMethod
    REMOTE_FILESYSTEM_READ_METHOD_READ: Settings.RemoteFilesystemReadMethod
    REMOTE_FILESYSTEM_READ_METHOD_THREADPOOL: Settings.RemoteFilesystemReadMethod
    class WritabilityConstraint(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: Settings.Writability
        def __init__(self, value: _Optional[_Union[Settings.Writability, str]] = ...) -> None: ...
    class Int64Setting(_message.Message):
        __slots__ = ("value", "min", "max", "writability")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        WRITABILITY_FIELD_NUMBER: _ClassVar[int]
        value: _wrappers_pb2.Int64Value
        min: _wrappers_pb2.Int64Value
        max: _wrappers_pb2.Int64Value
        writability: Settings.WritabilityConstraint
        def __init__(self, value: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., min: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., max: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., writability: _Optional[_Union[Settings.WritabilityConstraint, _Mapping]] = ...) -> None: ...
    class DoubleSetting(_message.Message):
        __slots__ = ("value", "min", "max", "writability")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        WRITABILITY_FIELD_NUMBER: _ClassVar[int]
        value: _wrappers_pb2.DoubleValue
        min: _wrappers_pb2.DoubleValue
        max: _wrappers_pb2.DoubleValue
        writability: Settings.WritabilityConstraint
        def __init__(self, value: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., min: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., max: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., writability: _Optional[_Union[Settings.WritabilityConstraint, _Mapping]] = ...) -> None: ...
    class BoolSetting(_message.Message):
        __slots__ = ("value", "writability")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        WRITABILITY_FIELD_NUMBER: _ClassVar[int]
        value: _wrappers_pb2.BoolValue
        writability: Settings.WritabilityConstraint
        def __init__(self, value: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., writability: _Optional[_Union[Settings.WritabilityConstraint, _Mapping]] = ...) -> None: ...
    class StringSetting(_message.Message):
        __slots__ = ("value", "writability")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        WRITABILITY_FIELD_NUMBER: _ClassVar[int]
        value: _wrappers_pb2.StringValue
        writability: Settings.WritabilityConstraint
        def __init__(self, value: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., writability: _Optional[_Union[Settings.WritabilityConstraint, _Mapping]] = ...) -> None: ...
    class OverflowModeSetting(_message.Message):
        __slots__ = ("value", "writability")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        WRITABILITY_FIELD_NUMBER: _ClassVar[int]
        value: Settings.OverflowMode
        writability: Settings.WritabilityConstraint
        def __init__(self, value: _Optional[_Union[Settings.OverflowMode, str]] = ..., writability: _Optional[_Union[Settings.WritabilityConstraint, _Mapping]] = ...) -> None: ...
    class GroupByOverflowModeSetting(_message.Message):
        __slots__ = ("value", "writability")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        WRITABILITY_FIELD_NUMBER: _ClassVar[int]
        value: Settings.GroupByOverflowMode
        writability: Settings.WritabilityConstraint
        def __init__(self, value: _Optional[_Union[Settings.GroupByOverflowMode, str]] = ..., writability: _Optional[_Union[Settings.WritabilityConstraint, _Mapping]] = ...) -> None: ...
    class DistributedProductModeSetting(_message.Message):
        __slots__ = ("value", "writability")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        WRITABILITY_FIELD_NUMBER: _ClassVar[int]
        value: Settings.DistributedProductMode
        writability: Settings.WritabilityConstraint
        def __init__(self, value: _Optional[_Union[Settings.DistributedProductMode, str]] = ..., writability: _Optional[_Union[Settings.WritabilityConstraint, _Mapping]] = ...) -> None: ...
    class CountDistinctImplementationSetting(_message.Message):
        __slots__ = ("value", "writability")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        WRITABILITY_FIELD_NUMBER: _ClassVar[int]
        value: Settings.CountDistinctImplementation
        writability: Settings.WritabilityConstraint
        def __init__(self, value: _Optional[_Union[Settings.CountDistinctImplementation, str]] = ..., writability: _Optional[_Union[Settings.WritabilityConstraint, _Mapping]] = ...) -> None: ...
    class JoinAlgorithmSetting(_message.Message):
        __slots__ = ("value", "writability")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        WRITABILITY_FIELD_NUMBER: _ClassVar[int]
        value: _containers.RepeatedScalarFieldContainer[Settings.JoinAlgorithm]
        writability: Settings.WritabilityConstraint
        def __init__(self, value: _Optional[_Iterable[_Union[Settings.JoinAlgorithm, str]]] = ..., writability: _Optional[_Union[Settings.WritabilityConstraint, _Mapping]] = ...) -> None: ...
    class FormatRegexpEscapingRuleSetting(_message.Message):
        __slots__ = ("value", "writability")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        WRITABILITY_FIELD_NUMBER: _ClassVar[int]
        value: Settings.FormatRegexpEscapingRule
        writability: Settings.WritabilityConstraint
        def __init__(self, value: _Optional[_Union[Settings.FormatRegexpEscapingRule, str]] = ..., writability: _Optional[_Union[Settings.WritabilityConstraint, _Mapping]] = ...) -> None: ...
    class DateTimeInputFormatSetting(_message.Message):
        __slots__ = ("value", "writability")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        WRITABILITY_FIELD_NUMBER: _ClassVar[int]
        value: Settings.DateTimeInputFormat
        writability: Settings.WritabilityConstraint
        def __init__(self, value: _Optional[_Union[Settings.DateTimeInputFormat, str]] = ..., writability: _Optional[_Union[Settings.WritabilityConstraint, _Mapping]] = ...) -> None: ...
    class DateTimeOutputFormatSetting(_message.Message):
        __slots__ = ("value", "writability")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        WRITABILITY_FIELD_NUMBER: _ClassVar[int]
        value: Settings.DateTimeOutputFormat
        writability: Settings.WritabilityConstraint
        def __init__(self, value: _Optional[_Union[Settings.DateTimeOutputFormat, str]] = ..., writability: _Optional[_Union[Settings.WritabilityConstraint, _Mapping]] = ...) -> None: ...
    class LocalFilesystemReadMethodSetting(_message.Message):
        __slots__ = ("value", "writability")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        WRITABILITY_FIELD_NUMBER: _ClassVar[int]
        value: Settings.LocalFilesystemReadMethod
        writability: Settings.WritabilityConstraint
        def __init__(self, value: _Optional[_Union[Settings.LocalFilesystemReadMethod, str]] = ..., writability: _Optional[_Union[Settings.WritabilityConstraint, _Mapping]] = ...) -> None: ...
    class RemoteFilesystemReadMethodSetting(_message.Message):
        __slots__ = ("value", "writability")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        WRITABILITY_FIELD_NUMBER: _ClassVar[int]
        value: Settings.RemoteFilesystemReadMethod
        writability: Settings.WritabilityConstraint
        def __init__(self, value: _Optional[_Union[Settings.RemoteFilesystemReadMethod, str]] = ..., writability: _Optional[_Union[Settings.WritabilityConstraint, _Mapping]] = ...) -> None: ...
    READONLY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_DDL_FIELD_NUMBER: _ClassVar[int]
    INSERT_QUORUM_FIELD_NUMBER: _ClassVar[int]
    INSERT_QUORUM_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SELECT_SEQUENTIAL_CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    MAX_REPLICA_DELAY_FOR_DISTRIBUTED_QUERIES_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_TO_STALE_REPLICAS_FOR_DISTRIBUTED_QUERIES_FIELD_NUMBER: _ClassVar[int]
    MAX_THREADS_FIELD_NUMBER: _ClassVar[int]
    MAX_BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_INSERT_BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMORY_USAGE_FOR_USER_FIELD_NUMBER: _ClassVar[int]
    MAX_ROWS_TO_READ_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_TO_READ_FIELD_NUMBER: _ClassVar[int]
    READ_OVERFLOW_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_ROWS_TO_GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_OVERFLOW_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_ROWS_TO_SORT_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_TO_SORT_FIELD_NUMBER: _ClassVar[int]
    SORT_OVERFLOW_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULT_ROWS_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULT_BYTES_FIELD_NUMBER: _ClassVar[int]
    RESULT_OVERFLOW_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_ROWS_IN_DISTINCT_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_IN_DISTINCT_FIELD_NUMBER: _ClassVar[int]
    DISTINCT_OVERFLOW_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_ROWS_TO_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_TO_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_OVERFLOW_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_OVERFLOW_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_COLUMNS_TO_READ_FIELD_NUMBER: _ClassVar[int]
    MAX_TEMPORARY_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    MAX_TEMPORARY_NON_CONST_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    MAX_QUERY_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_AST_DEPTH_FIELD_NUMBER: _ClassVar[int]
    MAX_AST_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    MAX_EXPANDED_AST_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    CONNECT_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SEND_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_ALTER_PARTITIONS_SYNC_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTED_PRODUCT_MODE_FIELD_NUMBER: _ClassVar[int]
    COMPILE_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    MIN_COUNT_TO_COMPILE_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    MIN_INSERT_BLOCK_SIZE_ROWS_FIELD_NUMBER: _ClassVar[int]
    MIN_INSERT_BLOCK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MIN_BYTES_TO_USE_DIRECT_IO_FIELD_NUMBER: _ClassVar[int]
    USE_UNCOMPRESSED_CACHE_FIELD_NUMBER: _ClassVar[int]
    MERGE_TREE_MAX_ROWS_TO_USE_CACHE_FIELD_NUMBER: _ClassVar[int]
    MERGE_TREE_MAX_BYTES_TO_USE_CACHE_FIELD_NUMBER: _ClassVar[int]
    MERGE_TREE_MIN_ROWS_FOR_CONCURRENT_READ_FIELD_NUMBER: _ClassVar[int]
    MERGE_TREE_MIN_BYTES_FOR_CONCURRENT_READ_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    MAX_NETWORK_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    MAX_NETWORK_BANDWIDTH_FOR_USER_FIELD_NUMBER: _ClassVar[int]
    FORCE_INDEX_BY_DATE_FIELD_NUMBER: _ClassVar[int]
    FORCE_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    INPUT_FORMAT_VALUES_INTERPRET_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
    INPUT_FORMAT_DEFAULTS_FOR_OMITTED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FORMAT_JSON_QUOTE_64BIT_INTEGERS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FORMAT_JSON_QUOTE_DENORMALS_FIELD_NUMBER: _ClassVar[int]
    HTTP_CONNECTION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    HTTP_RECEIVE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    HTTP_SEND_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HTTP_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    SEND_PROGRESS_IN_HTTP_HEADERS_FIELD_NUMBER: _ClassVar[int]
    HTTP_HEADERS_PROGRESS_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    ADD_HTTP_CORS_HEADER_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTED_AGGREGATION_MEMORY_EFFICIENT_FIELD_NUMBER: _ClassVar[int]
    DISTRIBUTED_DDL_TASK_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_BEFORE_EXTERNAL_GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_BEFORE_EXTERNAL_SORT_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_TWO_LEVEL_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_TWO_LEVEL_THRESHOLD_BYTES_FIELD_NUMBER: _ClassVar[int]
    LOW_CARDINALITY_ALLOW_IN_NATIVE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    EMPTY_RESULT_FOR_AGGREGATION_BY_EMPTY_SET_FIELD_NUMBER: _ClassVar[int]
    SKIP_UNAVAILABLE_SHARDS_FIELD_NUMBER: _ClassVar[int]
    MIN_EXECUTION_SPEED_FIELD_NUMBER: _ClassVar[int]
    MIN_EXECUTION_SPEED_BYTES_FIELD_NUMBER: _ClassVar[int]
    COUNT_DISTINCT_IMPLEMENTATION_FIELD_NUMBER: _ClassVar[int]
    MAX_ROWS_IN_SET_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_IN_SET_FIELD_NUMBER: _ClassVar[int]
    SET_OVERFLOW_MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_ROWS_IN_JOIN_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_IN_JOIN_FIELD_NUMBER: _ClassVar[int]
    JOIN_OVERFLOW_MODE_FIELD_NUMBER: _ClassVar[int]
    JOINED_SUBQUERY_REQUIRES_ALIAS_FIELD_NUMBER: _ClassVar[int]
    JOIN_USE_NULLS_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_NULL_IN_FIELD_NUMBER: _ClassVar[int]
    ALLOW_INTROSPECTION_FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    CONNECT_TIMEOUT_WITH_FAILOVER_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_BEFORE_CHECKING_EXECUTION_SPEED_FIELD_NUMBER: _ClassVar[int]
    INSERT_QUORUM_PARALLEL_FIELD_NUMBER: _ClassVar[int]
    INSERT_NULL_AS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    DEDUPLICATE_BLOCKS_IN_DEPENDENT_MATERIALIZED_VIEWS_FIELD_NUMBER: _ClassVar[int]
    MAX_PARTITIONS_PER_INSERT_BLOCK_FIELD_NUMBER: _ClassVar[int]
    MAX_CONCURRENT_QUERIES_FOR_USER_FIELD_NUMBER: _ClassVar[int]
    JOIN_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    ANY_JOIN_DISTINCT_RIGHT_TABLE_KEYS_FIELD_NUMBER: _ClassVar[int]
    INPUT_FORMAT_NULL_AS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    DATE_TIME_INPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    INPUT_FORMAT_WITH_NAMES_USE_HEADER_FIELD_NUMBER: _ClassVar[int]
    DATE_TIME_OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SUSPICIOUS_LOW_CARDINALITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    CANCEL_HTTP_READONLY_QUERIES_ON_CLIENT_CLOSE_FIELD_NUMBER: _ClassVar[int]
    MAX_HTTP_GET_REDIRECTS_FIELD_NUMBER: _ClassVar[int]
    FLATTEN_NESTED_FIELD_NUMBER: _ClassVar[int]
    FORMAT_REGEXP_FIELD_NUMBER: _ClassVar[int]
    FORMAT_REGEXP_ESCAPING_RULE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_REGEXP_SKIP_UNMATCHED_FIELD_NUMBER: _ClassVar[int]
    ASYNC_INSERT_FIELD_NUMBER: _ClassVar[int]
    ASYNC_INSERT_THREADS_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_ASYNC_INSERT_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_ASYNC_INSERT_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    ASYNC_INSERT_MAX_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    ASYNC_INSERT_BUSY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    ASYNC_INSERT_STALE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_PROFILER_STEP_FIELD_NUMBER: _ClassVar[int]
    MEMORY_PROFILER_SAMPLE_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    MAX_FINAL_THREADS_FIELD_NUMBER: _ClassVar[int]
    INPUT_FORMAT_PARALLEL_PARSING_FIELD_NUMBER: _ClassVar[int]
    INPUT_FORMAT_IMPORT_NESTED_JSON_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FILESYSTEM_READ_METHOD_FIELD_NUMBER: _ClassVar[int]
    MAX_READ_BUFFER_SIZE_FIELD_NUMBER: _ClassVar[int]
    INSERT_KEEPER_MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    MAX_TEMPORARY_DATA_ON_DISK_SIZE_FOR_USER_FIELD_NUMBER: _ClassVar[int]
    MAX_TEMPORARY_DATA_ON_DISK_SIZE_FOR_QUERY_FIELD_NUMBER: _ClassVar[int]
    MAX_PARSER_DEPTH_FIELD_NUMBER: _ClassVar[int]
    REMOTE_FILESYSTEM_READ_METHOD_FIELD_NUMBER: _ClassVar[int]
    MEMORY_OVERCOMMIT_RATIO_DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    MEMORY_OVERCOMMIT_RATIO_DENOMINATOR_FOR_USER_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_OVERCOMMIT_MAX_WAIT_MICROSECONDS_FIELD_NUMBER: _ClassVar[int]
    readonly: Settings.Int64Setting
    allow_ddl: Settings.BoolSetting
    insert_quorum: Settings.Int64Setting
    insert_quorum_timeout: Settings.Int64Setting
    select_sequential_consistency: Settings.BoolSetting
    max_replica_delay_for_distributed_queries: Settings.Int64Setting
    fallback_to_stale_replicas_for_distributed_queries: Settings.BoolSetting
    max_threads: Settings.Int64Setting
    max_block_size: Settings.Int64Setting
    max_insert_block_size: Settings.Int64Setting
    max_memory_usage: Settings.Int64Setting
    max_memory_usage_for_user: Settings.Int64Setting
    max_rows_to_read: Settings.Int64Setting
    max_bytes_to_read: Settings.Int64Setting
    read_overflow_mode: Settings.OverflowModeSetting
    max_rows_to_group_by: Settings.Int64Setting
    group_by_overflow_mode: Settings.GroupByOverflowModeSetting
    max_rows_to_sort: Settings.Int64Setting
    max_bytes_to_sort: Settings.Int64Setting
    sort_overflow_mode: Settings.OverflowModeSetting
    max_result_rows: Settings.Int64Setting
    max_result_bytes: Settings.Int64Setting
    result_overflow_mode: Settings.OverflowModeSetting
    max_rows_in_distinct: Settings.Int64Setting
    max_bytes_in_distinct: Settings.Int64Setting
    distinct_overflow_mode: Settings.OverflowModeSetting
    max_rows_to_transfer: Settings.Int64Setting
    max_bytes_to_transfer: Settings.Int64Setting
    transfer_overflow_mode: Settings.OverflowModeSetting
    max_execution_time: Settings.Int64Setting
    timeout_overflow_mode: Settings.OverflowModeSetting
    max_columns_to_read: Settings.Int64Setting
    max_temporary_columns: Settings.Int64Setting
    max_temporary_non_const_columns: Settings.Int64Setting
    max_query_size: Settings.Int64Setting
    max_ast_depth: Settings.Int64Setting
    max_ast_elements: Settings.Int64Setting
    max_expanded_ast_elements: Settings.Int64Setting
    connect_timeout: Settings.Int64Setting
    receive_timeout: Settings.Int64Setting
    send_timeout: Settings.Int64Setting
    replication_alter_partitions_sync: Settings.Int64Setting
    distributed_product_mode: Settings.DistributedProductModeSetting
    compile_expressions: Settings.BoolSetting
    min_count_to_compile_expression: Settings.Int64Setting
    min_insert_block_size_rows: Settings.Int64Setting
    min_insert_block_size_bytes: Settings.Int64Setting
    min_bytes_to_use_direct_io: Settings.Int64Setting
    use_uncompressed_cache: Settings.BoolSetting
    merge_tree_max_rows_to_use_cache: Settings.Int64Setting
    merge_tree_max_bytes_to_use_cache: Settings.Int64Setting
    merge_tree_min_rows_for_concurrent_read: Settings.Int64Setting
    merge_tree_min_bytes_for_concurrent_read: Settings.Int64Setting
    priority: Settings.Int64Setting
    max_network_bandwidth: Settings.Int64Setting
    max_network_bandwidth_for_user: Settings.Int64Setting
    force_index_by_date: Settings.BoolSetting
    force_primary_key: Settings.BoolSetting
    input_format_values_interpret_expressions: Settings.BoolSetting
    input_format_defaults_for_omitted_fields: Settings.BoolSetting
    output_format_json_quote_64bit_integers: Settings.BoolSetting
    output_format_json_quote_denormals: Settings.BoolSetting
    http_connection_timeout: Settings.Int64Setting
    http_receive_timeout: Settings.Int64Setting
    http_send_timeout: Settings.Int64Setting
    enable_http_compression: Settings.BoolSetting
    send_progress_in_http_headers: Settings.BoolSetting
    http_headers_progress_interval: Settings.Int64Setting
    add_http_cors_header: Settings.BoolSetting
    distributed_aggregation_memory_efficient: Settings.BoolSetting
    distributed_ddl_task_timeout: Settings.Int64Setting
    max_bytes_before_external_group_by: Settings.Int64Setting
    max_bytes_before_external_sort: Settings.Int64Setting
    group_by_two_level_threshold: Settings.Int64Setting
    group_by_two_level_threshold_bytes: Settings.Int64Setting
    low_cardinality_allow_in_native_format: Settings.BoolSetting
    empty_result_for_aggregation_by_empty_set: Settings.BoolSetting
    skip_unavailable_shards: Settings.BoolSetting
    min_execution_speed: Settings.Int64Setting
    min_execution_speed_bytes: Settings.Int64Setting
    count_distinct_implementation: Settings.CountDistinctImplementationSetting
    max_rows_in_set: Settings.Int64Setting
    max_bytes_in_set: Settings.Int64Setting
    set_overflow_mode: Settings.OverflowModeSetting
    max_rows_in_join: Settings.Int64Setting
    max_bytes_in_join: Settings.Int64Setting
    join_overflow_mode: Settings.OverflowModeSetting
    joined_subquery_requires_alias: Settings.BoolSetting
    join_use_nulls: Settings.BoolSetting
    transform_null_in: Settings.BoolSetting
    allow_introspection_functions: Settings.BoolSetting
    connect_timeout_with_failover: Settings.Int64Setting
    timeout_before_checking_execution_speed: Settings.Int64Setting
    insert_quorum_parallel: Settings.BoolSetting
    insert_null_as_default: Settings.BoolSetting
    deduplicate_blocks_in_dependent_materialized_views: Settings.BoolSetting
    max_partitions_per_insert_block: Settings.Int64Setting
    max_concurrent_queries_for_user: Settings.Int64Setting
    join_algorithm: Settings.JoinAlgorithmSetting
    any_join_distinct_right_table_keys: Settings.BoolSetting
    input_format_null_as_default: Settings.BoolSetting
    date_time_input_format: Settings.DateTimeInputFormatSetting
    input_format_with_names_use_header: Settings.BoolSetting
    date_time_output_format: Settings.DateTimeOutputFormatSetting
    allow_suspicious_low_cardinality_types: Settings.BoolSetting
    cancel_http_readonly_queries_on_client_close: Settings.BoolSetting
    max_http_get_redirects: Settings.Int64Setting
    flatten_nested: Settings.BoolSetting
    format_regexp: Settings.StringSetting
    format_regexp_escaping_rule: Settings.FormatRegexpEscapingRuleSetting
    format_regexp_skip_unmatched: Settings.BoolSetting
    async_insert: Settings.BoolSetting
    async_insert_threads: Settings.Int64Setting
    wait_for_async_insert: Settings.BoolSetting
    wait_for_async_insert_timeout: Settings.Int64Setting
    async_insert_max_data_size: Settings.Int64Setting
    async_insert_busy_timeout: Settings.Int64Setting
    async_insert_stale_timeout: Settings.Int64Setting
    memory_profiler_step: Settings.Int64Setting
    memory_profiler_sample_probability: Settings.DoubleSetting
    max_final_threads: Settings.Int64Setting
    input_format_parallel_parsing: Settings.BoolSetting
    input_format_import_nested_json: Settings.BoolSetting
    local_filesystem_read_method: Settings.LocalFilesystemReadMethodSetting
    max_read_buffer_size: Settings.Int64Setting
    insert_keeper_max_retries: Settings.Int64Setting
    max_temporary_data_on_disk_size_for_user: Settings.Int64Setting
    max_temporary_data_on_disk_size_for_query: Settings.Int64Setting
    max_parser_depth: Settings.Int64Setting
    remote_filesystem_read_method: Settings.RemoteFilesystemReadMethodSetting
    memory_overcommit_ratio_denominator: Settings.Int64Setting
    memory_overcommit_ratio_denominator_for_user: Settings.Int64Setting
    memory_usage_overcommit_max_wait_microseconds: Settings.Int64Setting
    def __init__(self, readonly: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., allow_ddl: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., insert_quorum: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., insert_quorum_timeout: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., select_sequential_consistency: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., max_replica_delay_for_distributed_queries: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., fallback_to_stale_replicas_for_distributed_queries: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., max_threads: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_block_size: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_insert_block_size: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_memory_usage: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_memory_usage_for_user: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_rows_to_read: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_bytes_to_read: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., read_overflow_mode: _Optional[_Union[Settings.OverflowModeSetting, _Mapping]] = ..., max_rows_to_group_by: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., group_by_overflow_mode: _Optional[_Union[Settings.GroupByOverflowModeSetting, _Mapping]] = ..., max_rows_to_sort: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_bytes_to_sort: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., sort_overflow_mode: _Optional[_Union[Settings.OverflowModeSetting, _Mapping]] = ..., max_result_rows: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_result_bytes: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., result_overflow_mode: _Optional[_Union[Settings.OverflowModeSetting, _Mapping]] = ..., max_rows_in_distinct: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_bytes_in_distinct: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., distinct_overflow_mode: _Optional[_Union[Settings.OverflowModeSetting, _Mapping]] = ..., max_rows_to_transfer: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_bytes_to_transfer: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., transfer_overflow_mode: _Optional[_Union[Settings.OverflowModeSetting, _Mapping]] = ..., max_execution_time: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., timeout_overflow_mode: _Optional[_Union[Settings.OverflowModeSetting, _Mapping]] = ..., max_columns_to_read: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_temporary_columns: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_temporary_non_const_columns: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_query_size: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_ast_depth: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_ast_elements: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_expanded_ast_elements: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., connect_timeout: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., receive_timeout: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., send_timeout: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., replication_alter_partitions_sync: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., distributed_product_mode: _Optional[_Union[Settings.DistributedProductModeSetting, _Mapping]] = ..., compile_expressions: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., min_count_to_compile_expression: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., min_insert_block_size_rows: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., min_insert_block_size_bytes: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., min_bytes_to_use_direct_io: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., use_uncompressed_cache: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., merge_tree_max_rows_to_use_cache: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., merge_tree_max_bytes_to_use_cache: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., merge_tree_min_rows_for_concurrent_read: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., merge_tree_min_bytes_for_concurrent_read: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., priority: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_network_bandwidth: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_network_bandwidth_for_user: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., force_index_by_date: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., force_primary_key: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., input_format_values_interpret_expressions: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., input_format_defaults_for_omitted_fields: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., output_format_json_quote_64bit_integers: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., output_format_json_quote_denormals: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., http_connection_timeout: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., http_receive_timeout: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., http_send_timeout: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., enable_http_compression: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., send_progress_in_http_headers: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., http_headers_progress_interval: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., add_http_cors_header: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., distributed_aggregation_memory_efficient: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., distributed_ddl_task_timeout: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_bytes_before_external_group_by: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_bytes_before_external_sort: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., group_by_two_level_threshold: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., group_by_two_level_threshold_bytes: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., low_cardinality_allow_in_native_format: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., empty_result_for_aggregation_by_empty_set: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., skip_unavailable_shards: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., min_execution_speed: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., min_execution_speed_bytes: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., count_distinct_implementation: _Optional[_Union[Settings.CountDistinctImplementationSetting, _Mapping]] = ..., max_rows_in_set: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_bytes_in_set: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., set_overflow_mode: _Optional[_Union[Settings.OverflowModeSetting, _Mapping]] = ..., max_rows_in_join: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_bytes_in_join: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., join_overflow_mode: _Optional[_Union[Settings.OverflowModeSetting, _Mapping]] = ..., joined_subquery_requires_alias: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., join_use_nulls: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., transform_null_in: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., allow_introspection_functions: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., connect_timeout_with_failover: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., timeout_before_checking_execution_speed: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., insert_quorum_parallel: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., insert_null_as_default: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., deduplicate_blocks_in_dependent_materialized_views: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., max_partitions_per_insert_block: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_concurrent_queries_for_user: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., join_algorithm: _Optional[_Union[Settings.JoinAlgorithmSetting, _Mapping]] = ..., any_join_distinct_right_table_keys: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., input_format_null_as_default: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., date_time_input_format: _Optional[_Union[Settings.DateTimeInputFormatSetting, _Mapping]] = ..., input_format_with_names_use_header: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., date_time_output_format: _Optional[_Union[Settings.DateTimeOutputFormatSetting, _Mapping]] = ..., allow_suspicious_low_cardinality_types: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., cancel_http_readonly_queries_on_client_close: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., max_http_get_redirects: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., flatten_nested: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., format_regexp: _Optional[_Union[Settings.StringSetting, _Mapping]] = ..., format_regexp_escaping_rule: _Optional[_Union[Settings.FormatRegexpEscapingRuleSetting, _Mapping]] = ..., format_regexp_skip_unmatched: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., async_insert: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., async_insert_threads: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., wait_for_async_insert: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., wait_for_async_insert_timeout: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., async_insert_max_data_size: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., async_insert_busy_timeout: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., async_insert_stale_timeout: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., memory_profiler_step: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., memory_profiler_sample_probability: _Optional[_Union[Settings.DoubleSetting, _Mapping]] = ..., max_final_threads: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., input_format_parallel_parsing: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., input_format_import_nested_json: _Optional[_Union[Settings.BoolSetting, _Mapping]] = ..., local_filesystem_read_method: _Optional[_Union[Settings.LocalFilesystemReadMethodSetting, _Mapping]] = ..., max_read_buffer_size: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., insert_keeper_max_retries: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_temporary_data_on_disk_size_for_user: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_temporary_data_on_disk_size_for_query: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., max_parser_depth: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., remote_filesystem_read_method: _Optional[_Union[Settings.RemoteFilesystemReadMethodSetting, _Mapping]] = ..., memory_overcommit_ratio_denominator: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., memory_overcommit_ratio_denominator_for_user: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ..., memory_usage_overcommit_max_wait_microseconds: _Optional[_Union[Settings.Int64Setting, _Mapping]] = ...) -> None: ...
