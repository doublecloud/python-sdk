# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/transfer/v1/endpoint/airbyte/facebook_marketing_source.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHdoublecloud/transfer/v1/endpoint/airbyte/facebook_marketing_source.proto\x12(doublecloud.transfer.v1.endpoint.airbyte\"\x9d\'\n\x17\x46\x61\x63\x65\x62ookMarketingSource\x12\x1d\n\nstart_date\x18\x01 \x01(\tR\tstartDate\x12\x19\n\x08\x65nd_date\x18\x02 \x01(\tR\x07\x65ndDate\x12\x1d\n\naccount_id\x18\x03 \x01(\tR\taccountId\x12!\n\x0c\x61\x63\x63\x65ss_token\x18\x04 \x01(\tR\x0b\x61\x63\x63\x65ssToken\x12\'\n\x0finclude_deleted\x18\x05 \x01(\x08R\x0eincludeDeleted\x12\x34\n\x16\x66\x65tch_thumbnail_images\x18\x06 \x01(\x08R\x14\x66\x65tchThumbnailImages\x12x\n\x0f\x63ustom_insights\x18\x07 \x03(\x0b\x32O.doublecloud.transfer.v1.endpoint.airbyte.FacebookMarketingSource.InsightConfigR\x0e\x63ustomInsights\x1a\xf1\x02\n\rInsightConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12_\n\x06\x66ields\x18\x02 \x03(\x0e\x32G.doublecloud.transfer.v1.endpoint.airbyte.FacebookMarketingSource.FieldR\x06\x66ields\x12k\n\nbreakdowns\x18\x03 \x03(\x0e\x32K.doublecloud.transfer.v1.endpoint.airbyte.FacebookMarketingSource.BreakdownR\nbreakdowns\x12~\n\x11\x61\x63tion_breakdowns\x18\x04 \x03(\x0e\x32Q.doublecloud.transfer.v1.endpoint.airbyte.FacebookMarketingSource.ActionBreakdownR\x10\x61\x63tionBreakdowns\"\xf3\x1a\n\x05\x46ield\x12\x15\n\x11\x46IELD_UNSPECIFIED\x10\x00\x12\x14\n\x10\x41\x43\x43OUNT_CURRENCY\x10\x01\x12\x0e\n\nACCOUNT_ID\x10\x02\x12\x10\n\x0c\x41\x43\x43OUNT_NAME\x10\x03\x12\x11\n\rACTION_VALUES\x10\x04\x12\x0b\n\x07\x41\x43TIONS\x10\x05\x12\x10\n\x0c\x41\x44_BID_VALUE\x10\x06\x12\x14\n\x10\x41\x44_CLICK_ACTIONS\x10\x07\x12\t\n\x05\x41\x44_ID\x10\x08\x12\x19\n\x15\x41\x44_IMPRESSION_ACTIONS\x10\t\x12\x0b\n\x07\x41\x44_NAME\x10\n\x12\x13\n\x0f\x41\x44SET_BID_VALUE\x10\x0b\x12\r\n\tADSET_END\x10\x0c\x12\x0c\n\x08\x41\x44SET_ID\x10\r\x12\x0e\n\nADSET_NAME\x10\x0e\x12\x0f\n\x0b\x41\x44SET_START\x10\x0f\x12\x11\n\rAGE_TARGETING\x10\x10\x12\x17\n\x13\x41TTRIBUTION_SETTING\x10\x11\x12\x0f\n\x0b\x41UCTION_BID\x10\x12\x12\x1b\n\x17\x41UCTION_COMPETITIVENESS\x10\x13\x12\x1e\n\x1a\x41UCTION_MAX_COMPETITOR_BID\x10\x14\x12\x0f\n\x0b\x42UYING_TYPE\x10\x15\x12\x0f\n\x0b\x43\x41MPAIGN_ID\x10\x16\x12\x11\n\rCAMPAIGN_NAME\x10\x17\x12\x1b\n\x17\x43\x41NVAS_AVG_VIEW_PERCENT\x10\x18\x12\x18\n\x14\x43\x41NVAS_AVG_VIEW_TIME\x10\x19\x12\x1b\n\x17\x43\x41TALOG_SEGMENT_ACTIONS\x10\x1a\x12\x19\n\x15\x43\x41TALOG_SEGMENT_VALUE\x10\x1b\x12.\n*CATALOG_SEGMENT_VALUE_MOBILE_PURCHASE_ROAS\x10\x1c\x12,\n(CATALOG_SEGMENT_VALUE_OMNI_PURCHASE_ROAS\x10\x1d\x12/\n+CATALOG_SEGMENT_VALUE_WEBSITE_PURCHASE_ROAS\x10\x1e\x12\n\n\x06\x43LICKS\x10\x1f\x12\x1b\n\x17\x43ONVERSION_RATE_RANKING\x10 \x12\x15\n\x11\x43ONVERSION_VALUES\x10!\x12\x0f\n\x0b\x43ONVERSIONS\x10\"\x12\x1e\n\x1a\x43ONVERTED_PRODUCT_QUANTITY\x10#\x12\x1b\n\x17\x43ONVERTED_PRODUCT_VALUE\x10$\x12\x1e\n\x1a\x43OST_PER_15_SEC_VIDEO_VIEW\x10%\x12(\n$COST_PER_2_SEC_CONTINUOUS_VIDEO_VIEW\x10&\x12\x18\n\x14\x43OST_PER_ACTION_TYPE\x10\'\x12\x15\n\x11\x43OST_PER_AD_CLICK\x10(\x12\x17\n\x13\x43OST_PER_CONVERSION\x10)\x12\x1e\n\x1a\x43OST_PER_DDA_COUNTBY_CONVS\x10*\x12#\n\x1f\x43OST_PER_ESTIMATED_AD_RECALLERS\x10+\x12\x1e\n\x1a\x43OST_PER_INLINE_LINK_CLICK\x10,\x12#\n\x1f\x43OST_PER_INLINE_POST_ENGAGEMENT\x10-\x12\'\n#COST_PER_ONE_THOUSAND_AD_IMPRESSION\x10.\x12\x1b\n\x17\x43OST_PER_OUTBOUND_CLICK\x10/\x12\x15\n\x11\x43OST_PER_THRUPLAY\x10\x30\x12\x1f\n\x1b\x43OST_PER_UNIQUE_ACTION_TYPE\x10\x31\x12\x19\n\x15\x43OST_PER_UNIQUE_CLICK\x10\x32\x12\x1e\n\x1a\x43OST_PER_UNIQUE_CONVERSION\x10\x33\x12%\n!COST_PER_UNIQUE_INLINE_LINK_CLICK\x10\x34\x12\"\n\x1e\x43OST_PER_UNIQUE_OUTBOUND_CLICK\x10\x35\x12\x07\n\x03\x43PC\x10\x36\x12\x07\n\x03\x43PM\x10\x37\x12\x07\n\x03\x43PP\x10\x38\x12\x10\n\x0c\x43REATED_TIME\x10\x39\x12\x07\n\x03\x43TR\x10:\x12\x0e\n\nDATE_START\x10;\x12\r\n\tDATE_STOP\x10<\x12\x15\n\x11\x44\x44\x41_COUNTBY_CONVS\x10=\x12\x0f\n\x0b\x44\x44\x41_RESULTS\x10>\x12\x1b\n\x17\x45NGAGEMENT_RATE_RANKING\x10?\x12\x1c\n\x18\x45STIMATED_AD_RECALL_RATE\x10@\x12(\n$ESTIMATED_AD_RECALL_RATE_LOWER_BOUND\x10\x41\x12(\n$ESTIMATED_AD_RECALL_RATE_UPPER_BOUND\x10\x42\x12\x1a\n\x16\x45STIMATED_AD_RECALLERS\x10\x43\x12&\n\"ESTIMATED_AD_RECALLERS_LOWER_BOUND\x10\x44\x12&\n\"ESTIMATED_AD_RECALLERS_UPPER_BOUND\x10\x45\x12\r\n\tFREQUENCY\x10\x46\x12\x19\n\x15\x46ULL_VIEW_IMPRESSIONS\x10G\x12\x13\n\x0f\x46ULL_VIEW_REACH\x10H\x12\x14\n\x10GENDER_TARGETING\x10I\x12\x0f\n\x0bIMPRESSIONS\x10J\x12\x19\n\x15INLINE_LINK_CLICK_CTR\x10K\x12\x16\n\x12INLINE_LINK_CLICKS\x10L\x12\x1a\n\x16INLINE_POST_ENGAGEMENT\x10M\x12%\n!INSTANT_EXPERIENCE_CLICKS_TO_OPEN\x10N\x12&\n\"INSTANT_EXPERIENCE_CLICKS_TO_START\x10O\x12&\n\"INSTANT_EXPERIENCE_OUTBOUND_CLICKS\x10P\x12\x1d\n\x19INTERACTIVE_COMPONENT_TAP\x10Q\x12\n\n\x06LABELS\x10R\x12\x0c\n\x08LOCATION\x10S\x12\x1c\n\x18MOBILE_APP_PURCHASE_ROAS\x10T\x12\r\n\tOBJECTIVE\x10U\x12\x15\n\x11OPTIMIZATION_GOAL\x10V\x12\x13\n\x0fOUTBOUND_CLICKS\x10W\x12\x17\n\x13OUTBOUND_CLICKS_CTR\x10X\x12\x13\n\x0fPLACE_PAGE_NAME\x10Y\x12\x11\n\rPURCHASE_ROAS\x10Z\x12+\n\'QUALIFYING_QUESTION_QUALIFY_ANSWER_RATE\x10[\x12\x13\n\x0fQUALITY_RANKING\x10\\\x12\x16\n\x12QUALITY_SCORE_ECTR\x10]\x12\x16\n\x12QUALITY_SCORE_ECVR\x10^\x12\x19\n\x15QUALITY_SCORE_ORGANIC\x10_\x12\t\n\x05REACH\x10`\x12\x10\n\x0cSOCIAL_SPEND\x10\x61\x12\t\n\x05SPEND\x10\x62\x12\x13\n\x0fTOTAL_POSTBACKS\x10\x63\x12\x12\n\x0eUNIQUE_ACTIONS\x10\x64\x12\x11\n\rUNIQUE_CLICKS\x10\x65\x12\x16\n\x12UNIQUE_CONVERSIONS\x10\x66\x12\x0e\n\nUNIQUE_CTR\x10g\x12 \n\x1cUNIQUE_INLINE_LINK_CLICK_CTR\x10h\x12\x1d\n\x19UNIQUE_INLINE_LINK_CLICKS\x10i\x12\x1a\n\x16UNIQUE_LINK_CLICKS_CTR\x10j\x12\x1a\n\x16UNIQUE_OUTBOUND_CLICKS\x10k\x12\x1e\n\x1aUNIQUE_OUTBOUND_CLICKS_CTR\x10l\x12\x31\n-UNIQUE_VIDEO_CONTINUOUS_2_SEC_WATCHED_ACTIONS\x10m\x12\x1c\n\x18UNIQUE_VIDEO_VIEW_15_SEC\x10n\x12\x10\n\x0cUPDATED_TIME\x10o\x12 \n\x1cVIDEO_15_SEC_WATCHED_ACTIONS\x10p\x12 \n\x1cVIDEO_30_SEC_WATCHED_ACTIONS\x10q\x12\"\n\x1eVIDEO_AVG_TIME_WATCHED_ACTIONS\x10r\x12*\n&VIDEO_CONTINUOUS_2_SEC_WATCHED_ACTIONS\x10s\x12\x1e\n\x1aVIDEO_P100_WATCHED_ACTIONS\x10t\x12\x1d\n\x19VIDEO_P25_WATCHED_ACTIONS\x10u\x12\x1d\n\x19VIDEO_P50_WATCHED_ACTIONS\x10v\x12\x1d\n\x19VIDEO_P75_WATCHED_ACTIONS\x10w\x12\x1d\n\x19VIDEO_P95_WATCHED_ACTIONS\x10x\x12\x16\n\x12VIDEO_PLAY_ACTIONS\x10y\x12\x1c\n\x18VIDEO_PLAY_CURVE_ACTIONS\x10z\x12)\n%VIDEO_PLAY_RETENTION_0_TO_15S_ACTIONS\x10{\x12*\n&VIDEO_PLAY_RETENTION_20_TO_60S_ACTIONS\x10|\x12&\n\"VIDEO_PLAY_RETENTION_GRAPH_ACTIONS\x10}\x12\"\n\x1eVIDEO_THRUPLAY_WATCHED_ACTIONS\x10~\x12\x1e\n\x1aVIDEO_TIME_WATCHED_ACTIONS\x10\x7f\x12\x10\n\x0bWEBSITE_CTR\x10\x80\x01\x12\x1a\n\x15WEBSITE_PURCHASE_ROAS\x10\x82\x01\x12\r\n\x08WISH_BID\x10\x83\x01\"\x98\x04\n\tBreakdown\x12\x19\n\x15\x42REAKDOWN_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x41\x44_FORMAT_ASSET\x10\x01\x12\x07\n\x03\x41GE\x10\x02\x12\n\n\x06\x41PP_ID\x10\x03\x12\x0e\n\nBODY_ASSET\x10\x04\x12\x18\n\x14\x43\x41LL_TO_ACTION_ASSET\x10\x05\x12\x0b\n\x07\x43OUNTRY\x10\x06\x12\x15\n\x11\x44\x45SCRIPTION_ASSET\x10\x07\x12\x13\n\x0f\x44\x45VICE_PLATFORM\x10\x08\x12\x07\n\x03\x44MA\x10\t\x12\x13\n\x0f\x46REQUENCY_VALUE\x10\n\x12\n\n\x06GENDER\x10\x0b\x12\x33\n/HOURLY_STATS_AGGREGATED_BY_ADVERTISER_TIME_ZONE\x10\x0c\x12\x31\n-HOURLY_STATS_AGGREGATED_BY_AUDIENCE_TIME_ZONE\x10\r\x12\x0f\n\x0bIMAGE_ASSET\x10\x0e\x12\x15\n\x11IMPRESSION_DEVICE\x10\x0f\x12\x12\n\x0eLINK_URL_ASSET\x10\x10\x12\x11\n\rPLACE_PAGE_ID\x10\x11\x12\x15\n\x11PLATFORM_POSITION\x10\x12\x12\x0e\n\nPRODUCT_ID\x10\x13\x12\x16\n\x12PUBLISHER_PLATFORM\x10\x14\x12\n\n\x06REGION\x10\x15\x12\x16\n\x12SKAN_CONVERSION_ID\x10\x16\x12\x0f\n\x0bTITLE_ASSET\x10\x17\x12\x0e\n\nVIDEO_ASSE\x10\x18\"\xa7\x02\n\x0f\x41\x63tionBreakdown\x12 \n\x1c\x41\x43TION_BREAKDOWN_UNSPECIFIED\x10\x00\x12 \n\x1c\x41\x43TION_CANVAS_COMPONENT_NAME\x10\x01\x12\x1b\n\x17\x41\x43TION_CAROUSEL_CARD_ID\x10\x02\x12\x1d\n\x19\x41\x43TION_CAROUSEL_CARD_NAME\x10\x03\x12\x16\n\x12\x41\x43TION_DESTINATION\x10\x04\x12\x11\n\rACTION_DEVICE\x10\x05\x12\x13\n\x0f\x41\x43TION_REACTION\x10\x06\x12\x14\n\x10\x41\x43TION_TARGET_ID\x10\x07\x12\x0f\n\x0b\x41\x43TION_TYPE\x10\x08\x12\x16\n\x12\x41\x43TION_VIDEO_SOUND\x10\t\x12\x15\n\x11\x41\x43TION_VIDEO_TYPE\x10\nB^Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyteb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.endpoint.airbyte.facebook_marketing_source_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\\github.com/doublecloud/go-genproto/doublecloud/transfer/v1/endpoint/airbyte;endpoint_airbyte'
  _globals['_FACEBOOKMARKETINGSOURCE']._serialized_start=119
  _globals['_FACEBOOKMARKETINGSOURCE']._serialized_end=5140
  _globals['_FACEBOOKMARKETINGSOURCE_INSIGHTCONFIG']._serialized_start=488
  _globals['_FACEBOOKMARKETINGSOURCE_INSIGHTCONFIG']._serialized_end=857
  _globals['_FACEBOOKMARKETINGSOURCE_FIELD']._serialized_start=860
  _globals['_FACEBOOKMARKETINGSOURCE_FIELD']._serialized_end=4303
  _globals['_FACEBOOKMARKETINGSOURCE_BREAKDOWN']._serialized_start=4306
  _globals['_FACEBOOKMARKETINGSOURCE_BREAKDOWN']._serialized_end=4842
  _globals['_FACEBOOKMARKETINGSOURCE_ACTIONBREAKDOWN']._serialized_start=4845
  _globals['_FACEBOOKMARKETINGSOURCE_ACTIONBREAKDOWN']._serialized_end=5140
# @@protoc_insertion_point(module_scope)
