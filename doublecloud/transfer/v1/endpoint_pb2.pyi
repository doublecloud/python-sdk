from doublecloud.transfer.v1.endpoint import clickhouse_pb2 as _clickhouse_pb2
from doublecloud.transfer.v1.endpoint import common_pb2 as _common_pb2
from doublecloud.transfer.v1.endpoint import kafka_pb2 as _kafka_pb2
from doublecloud.transfer.v1.endpoint import kinesis_pb2 as _kinesis_pb2
from doublecloud.transfer.v1.endpoint import mongo_pb2 as _mongo_pb2
from doublecloud.transfer.v1.endpoint import mysql_pb2 as _mysql_pb2
from doublecloud.transfer.v1.endpoint import object_storage_pb2 as _object_storage_pb2
from doublecloud.transfer.v1.endpoint import metrica_pb2 as _metrica_pb2
from doublecloud.transfer.v1.endpoint import postgres_pb2 as _postgres_pb2
from doublecloud.transfer.v1.endpoint import datadog_pb2 as _datadog_pb2
from doublecloud.transfer.v1.endpoint import coralogix_pb2 as _coralogix_pb2
from doublecloud.transfer.v1.endpoint import bigquery_pb2 as _bigquery_pb2
from doublecloud.transfer.v1.endpoint.airbyte import s3_source_pb2 as _s3_source_pb2
from doublecloud.transfer.v1.endpoint.airbyte import redshift_source_pb2 as _redshift_source_pb2
from doublecloud.transfer.v1.endpoint.airbyte import aws_cloud_trail_source_pb2 as _aws_cloud_trail_source_pb2
from doublecloud.transfer.v1.endpoint.airbyte import bigquery_source_pb2 as _bigquery_source_pb2
from doublecloud.transfer.v1.endpoint.airbyte import dynamodb_source_pb2 as _dynamodb_source_pb2
from doublecloud.transfer.v1.endpoint.airbyte import mssql_source_pb2 as _mssql_source_pb2
from doublecloud.transfer.v1.endpoint.airbyte import amazon_ads_source_pb2 as _amazon_ads_source_pb2
from doublecloud.transfer.v1.endpoint.airbyte import facebook_marketing_source_pb2 as _facebook_marketing_source_pb2
from doublecloud.transfer.v1.endpoint.airbyte import linkedin_ads_source_pb2 as _linkedin_ads_source_pb2
from doublecloud.transfer.v1.endpoint.airbyte import instagram_source_pb2 as _instagram_source_pb2
from doublecloud.transfer.v1.endpoint.airbyte import google_ads_source_pb2 as _google_ads_source_pb2
from doublecloud.transfer.v1.endpoint.airbyte import snowflake_source_pb2 as _snowflake_source_pb2
from doublecloud.transfer.v1.endpoint.airbyte import jira_source_pb2 as _jira_source_pb2
from doublecloud.transfer.v1.endpoint.airbyte import hubspot_source_pb2 as _hubspot_source_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Endpoint(_message.Message):
    __slots__ = ("id", "project_id", "name", "description", "labels", "settings")
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
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    project_id: str
    name: str
    description: str
    labels: _containers.ScalarMap[str, str]
    settings: EndpointSettings
    def __init__(self, id: _Optional[str] = ..., project_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., settings: _Optional[_Union[EndpointSettings, _Mapping]] = ...) -> None: ...

class EndpointSettings(_message.Message):
    __slots__ = ("mysql_source", "postgres_source", "kafka_source", "mongo_source", "clickhouse_source", "mysql_target", "postgres_target", "clickhouse_target", "object_storage_target", "kafka_target", "mongo_target", "s3_source", "aws_cloudtrail_source", "big_query_source", "facebook_marketing_source", "google_ads_source", "amazon_ads_source", "instagram_source", "linkedin_ads_source", "mssql_source", "redshift_source", "snowflake_source", "object_storage_source", "datadog_target", "jira_source", "hubspot_source", "coralogix_target", "bigquery_target", "metrica_source", "dynamodb_source", "kinesis_source")
    MYSQL_SOURCE_FIELD_NUMBER: _ClassVar[int]
    POSTGRES_SOURCE_FIELD_NUMBER: _ClassVar[int]
    KAFKA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    MONGO_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CLICKHOUSE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    MYSQL_TARGET_FIELD_NUMBER: _ClassVar[int]
    POSTGRES_TARGET_FIELD_NUMBER: _ClassVar[int]
    CLICKHOUSE_TARGET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STORAGE_TARGET_FIELD_NUMBER: _ClassVar[int]
    KAFKA_TARGET_FIELD_NUMBER: _ClassVar[int]
    MONGO_TARGET_FIELD_NUMBER: _ClassVar[int]
    S3_SOURCE_FIELD_NUMBER: _ClassVar[int]
    AWS_CLOUDTRAIL_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BIG_QUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    FACEBOOK_MARKETING_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_ADS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    AMAZON_ADS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    INSTAGRAM_SOURCE_FIELD_NUMBER: _ClassVar[int]
    LINKEDIN_ADS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    MSSQL_SOURCE_FIELD_NUMBER: _ClassVar[int]
    REDSHIFT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SNOWFLAKE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STORAGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DATADOG_TARGET_FIELD_NUMBER: _ClassVar[int]
    JIRA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    HUBSPOT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    CORALOGIX_TARGET_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_TARGET_FIELD_NUMBER: _ClassVar[int]
    METRICA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DYNAMODB_SOURCE_FIELD_NUMBER: _ClassVar[int]
    KINESIS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    mysql_source: _mysql_pb2.MysqlSource
    postgres_source: _postgres_pb2.PostgresSource
    kafka_source: _kafka_pb2.KafkaSource
    mongo_source: _mongo_pb2.MongoSource
    clickhouse_source: _clickhouse_pb2.ClickhouseSource
    mysql_target: _mysql_pb2.MysqlTarget
    postgres_target: _postgres_pb2.PostgresTarget
    clickhouse_target: _clickhouse_pb2.ClickhouseTarget
    object_storage_target: _object_storage_pb2.ObjectStorageTarget
    kafka_target: _kafka_pb2.KafkaTarget
    mongo_target: _mongo_pb2.MongoTarget
    s3_source: _s3_source_pb2.S3Source
    aws_cloudtrail_source: _aws_cloud_trail_source_pb2.AWSCloudTrailSource
    big_query_source: _bigquery_source_pb2.BigQuerySource
    facebook_marketing_source: _facebook_marketing_source_pb2.FacebookMarketingSource
    google_ads_source: _google_ads_source_pb2.GoogleAdsSource
    amazon_ads_source: _amazon_ads_source_pb2.AmazonAdsSource
    instagram_source: _instagram_source_pb2.InstagramSource
    linkedin_ads_source: _linkedin_ads_source_pb2.LinkedinAdsSource
    mssql_source: _mssql_source_pb2.MSSQLSource
    redshift_source: _redshift_source_pb2.RedshiftSource
    snowflake_source: _snowflake_source_pb2.SnowflakeSource
    object_storage_source: _object_storage_pb2.ObjectStorageSource
    datadog_target: _datadog_pb2.DatadogTarget
    jira_source: _jira_source_pb2.JiraSource
    hubspot_source: _hubspot_source_pb2.HubspotSource
    coralogix_target: _coralogix_pb2.CoralogixTarget
    bigquery_target: _bigquery_pb2.BigQueryTarget
    metrica_source: _metrica_pb2.MetricaSource
    dynamodb_source: _dynamodb_source_pb2.DynamodbSource
    kinesis_source: _kinesis_pb2.KinesisSource
    def __init__(self, mysql_source: _Optional[_Union[_mysql_pb2.MysqlSource, _Mapping]] = ..., postgres_source: _Optional[_Union[_postgres_pb2.PostgresSource, _Mapping]] = ..., kafka_source: _Optional[_Union[_kafka_pb2.KafkaSource, _Mapping]] = ..., mongo_source: _Optional[_Union[_mongo_pb2.MongoSource, _Mapping]] = ..., clickhouse_source: _Optional[_Union[_clickhouse_pb2.ClickhouseSource, _Mapping]] = ..., mysql_target: _Optional[_Union[_mysql_pb2.MysqlTarget, _Mapping]] = ..., postgres_target: _Optional[_Union[_postgres_pb2.PostgresTarget, _Mapping]] = ..., clickhouse_target: _Optional[_Union[_clickhouse_pb2.ClickhouseTarget, _Mapping]] = ..., object_storage_target: _Optional[_Union[_object_storage_pb2.ObjectStorageTarget, _Mapping]] = ..., kafka_target: _Optional[_Union[_kafka_pb2.KafkaTarget, _Mapping]] = ..., mongo_target: _Optional[_Union[_mongo_pb2.MongoTarget, _Mapping]] = ..., s3_source: _Optional[_Union[_s3_source_pb2.S3Source, _Mapping]] = ..., aws_cloudtrail_source: _Optional[_Union[_aws_cloud_trail_source_pb2.AWSCloudTrailSource, _Mapping]] = ..., big_query_source: _Optional[_Union[_bigquery_source_pb2.BigQuerySource, _Mapping]] = ..., facebook_marketing_source: _Optional[_Union[_facebook_marketing_source_pb2.FacebookMarketingSource, _Mapping]] = ..., google_ads_source: _Optional[_Union[_google_ads_source_pb2.GoogleAdsSource, _Mapping]] = ..., amazon_ads_source: _Optional[_Union[_amazon_ads_source_pb2.AmazonAdsSource, _Mapping]] = ..., instagram_source: _Optional[_Union[_instagram_source_pb2.InstagramSource, _Mapping]] = ..., linkedin_ads_source: _Optional[_Union[_linkedin_ads_source_pb2.LinkedinAdsSource, _Mapping]] = ..., mssql_source: _Optional[_Union[_mssql_source_pb2.MSSQLSource, _Mapping]] = ..., redshift_source: _Optional[_Union[_redshift_source_pb2.RedshiftSource, _Mapping]] = ..., snowflake_source: _Optional[_Union[_snowflake_source_pb2.SnowflakeSource, _Mapping]] = ..., object_storage_source: _Optional[_Union[_object_storage_pb2.ObjectStorageSource, _Mapping]] = ..., datadog_target: _Optional[_Union[_datadog_pb2.DatadogTarget, _Mapping]] = ..., jira_source: _Optional[_Union[_jira_source_pb2.JiraSource, _Mapping]] = ..., hubspot_source: _Optional[_Union[_hubspot_source_pb2.HubspotSource, _Mapping]] = ..., coralogix_target: _Optional[_Union[_coralogix_pb2.CoralogixTarget, _Mapping]] = ..., bigquery_target: _Optional[_Union[_bigquery_pb2.BigQueryTarget, _Mapping]] = ..., metrica_source: _Optional[_Union[_metrica_pb2.MetricaSource, _Mapping]] = ..., dynamodb_source: _Optional[_Union[_dynamodb_source_pb2.DynamodbSource, _Mapping]] = ..., kinesis_source: _Optional[_Union[_kinesis_pb2.KinesisSource, _Mapping]] = ...) -> None: ...
