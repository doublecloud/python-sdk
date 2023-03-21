# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: doublecloud/transfer/v1/transfer_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from doublecloud.transfer.v1 import transfer_pb2 as doublecloud_dot_transfer_dot_v1_dot_transfer__pb2
from doublecloud.v1 import operation_pb2 as doublecloud_dot_v1_dot_operation__pb2
from doublecloud.v1 import paging_pb2 as doublecloud_dot_v1_dot_paging__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.doublecloud/transfer/v1/transfer_service.proto\x12\x17\x64oublecloud.transfer.v1\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a&doublecloud/transfer/v1/transfer.proto\x1a\x1e\x64oublecloud/v1/operation.proto\x1a\x1b\x64oublecloud/v1/paging.proto\"\xf0\x02\n\x15\x43reateTransferRequest\x12\x1b\n\tsource_id\x18\x01 \x01(\tR\x08sourceId\x12\x1b\n\ttarget_id\x18\x02 \x01(\tR\x08targetId\x12\x12\n\x04name\x18\x07 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12R\n\x06labels\x18\x08 \x03(\x0b\x32:.doublecloud.transfer.v1.CreateTransferRequest.LabelsEntryR\x06labels\x12\x1d\n\nproject_id\x18\x04 \x01(\tR\tprojectId\x12\x39\n\x04type\x18\x06 \x01(\x0e\x32%.doublecloud.transfer.v1.TransferTypeR\x04type\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xfd\x01\n\x15UpdateTransferRequest\x12\x1f\n\x0btransfer_id\x18\x01 \x01(\tR\ntransferId\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12R\n\x06labels\x18\x06 \x03(\x0b\x32:.doublecloud.transfer.v1.UpdateTransferRequest.LabelsEntryR\x06labels\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"8\n\x15\x44\x65leteTransferRequest\x12\x1f\n\x0btransfer_id\x18\x01 \x01(\tR\ntransferId\"a\n\x14ListTransfersRequest\x12\x1d\n\nproject_id\x18\x02 \x01(\tR\tprojectId\x12*\n\x04page\x18\x03 \x01(\x0b\x32\x16.doublecloud.v1.PagingR\x04page\"\x80\x01\n\x15ListTransfersResponse\x12?\n\ttransfers\x18\x01 \x03(\x0b\x32!.doublecloud.transfer.v1.TransferR\ttransfers\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"5\n\x12GetTransferRequest\x12\x1f\n\x0btransfer_id\x18\x01 \x01(\tR\ntransferId\"<\n\x19\x44\x65\x61\x63tivateTransferRequest\x12\x1f\n\x0btransfer_id\x18\x01 \x01(\tR\ntransferId\":\n\x17\x41\x63tivateTransferRequest\x12\x1f\n\x0btransfer_id\x18\x01 \x01(\tR\ntransferId2\x9a\x07\n\x0fTransferService\x12l\n\x06\x43reate\x12..doublecloud.transfer.v1.CreateTransferRequest\x1a\x19.doublecloud.v1.Operation\"\x17\x82\xd3\xe4\x93\x02\x11:\x01*\"\x0c/v1/transfer\x12z\n\x06Update\x12..doublecloud.transfer.v1.UpdateTransferRequest\x1a\x19.doublecloud.v1.Operation\"%\x82\xd3\xe4\x93\x02\x1f:\x01*2\x1a/v1/transfer/{transfer_id}\x12w\n\x06\x44\x65lete\x12..doublecloud.transfer.v1.DeleteTransferRequest\x1a\x19.doublecloud.v1.Operation\"\"\x82\xd3\xe4\x93\x02\x1c*\x1a/v1/transfer/{transfer_id}\x12\x8e\x01\n\x04List\x12-.doublecloud.transfer.v1.ListTransfersRequest\x1a..doublecloud.transfer.v1.ListTransfersResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1/transfers/list/{project_id}\x12y\n\x03Get\x12+.doublecloud.transfer.v1.GetTransferRequest\x1a!.doublecloud.transfer.v1.Transfer\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1/transfer/{transfer_id}\x12\x8d\x01\n\nDeactivate\x12\x32.doublecloud.transfer.v1.DeactivateTransferRequest\x1a\x19.doublecloud.v1.Operation\"0\x82\xd3\xe4\x93\x02*:\x01*\"%/v1/transfer/{transfer_id}:deactivate\x12\x87\x01\n\x08\x41\x63tivate\x12\x30.doublecloud.transfer.v1.ActivateTransferRequest\x1a\x19.doublecloud.v1.Operation\".\x82\xd3\xe4\x93\x02(:\x01*\"#/v1/transfer/{transfer_id}:activateB=Z;github.com/doublecloud/api/doublecloud/transfer/v1;transferb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doublecloud.transfer.v1.transfer_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z;github.com/doublecloud/api/doublecloud/transfer/v1;transfer'
  _CREATETRANSFERREQUEST_LABELSENTRY._options = None
  _CREATETRANSFERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATETRANSFERREQUEST_LABELSENTRY._options = None
  _UPDATETRANSFERREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _TRANSFERSERVICE.methods_by_name['Create']._options = None
  _TRANSFERSERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\021:\001*\"\014/v1/transfer'
  _TRANSFERSERVICE.methods_by_name['Update']._options = None
  _TRANSFERSERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002\037:\001*2\032/v1/transfer/{transfer_id}'
  _TRANSFERSERVICE.methods_by_name['Delete']._options = None
  _TRANSFERSERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002\034*\032/v1/transfer/{transfer_id}'
  _TRANSFERSERVICE.methods_by_name['List']._options = None
  _TRANSFERSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002!\022\037/v1/transfers/list/{project_id}'
  _TRANSFERSERVICE.methods_by_name['Get']._options = None
  _TRANSFERSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002\034\022\032/v1/transfer/{transfer_id}'
  _TRANSFERSERVICE.methods_by_name['Deactivate']._options = None
  _TRANSFERSERVICE.methods_by_name['Deactivate']._serialized_options = b'\202\323\344\223\002*:\001*\"%/v1/transfer/{transfer_id}:deactivate'
  _TRANSFERSERVICE.methods_by_name['Activate']._options = None
  _TRANSFERSERVICE.methods_by_name['Activate']._serialized_options = b'\202\323\344\223\002(:\001*\"#/v1/transfer/{transfer_id}:activate'
  _globals['_CREATETRANSFERREQUEST']._serialized_start=241
  _globals['_CREATETRANSFERREQUEST']._serialized_end=609
  _globals['_CREATETRANSFERREQUEST_LABELSENTRY']._serialized_start=552
  _globals['_CREATETRANSFERREQUEST_LABELSENTRY']._serialized_end=609
  _globals['_UPDATETRANSFERREQUEST']._serialized_start=612
  _globals['_UPDATETRANSFERREQUEST']._serialized_end=865
  _globals['_UPDATETRANSFERREQUEST_LABELSENTRY']._serialized_start=552
  _globals['_UPDATETRANSFERREQUEST_LABELSENTRY']._serialized_end=609
  _globals['_DELETETRANSFERREQUEST']._serialized_start=867
  _globals['_DELETETRANSFERREQUEST']._serialized_end=923
  _globals['_LISTTRANSFERSREQUEST']._serialized_start=925
  _globals['_LISTTRANSFERSREQUEST']._serialized_end=1022
  _globals['_LISTTRANSFERSRESPONSE']._serialized_start=1025
  _globals['_LISTTRANSFERSRESPONSE']._serialized_end=1153
  _globals['_GETTRANSFERREQUEST']._serialized_start=1155
  _globals['_GETTRANSFERREQUEST']._serialized_end=1208
  _globals['_DEACTIVATETRANSFERREQUEST']._serialized_start=1210
  _globals['_DEACTIVATETRANSFERREQUEST']._serialized_end=1270
  _globals['_ACTIVATETRANSFERREQUEST']._serialized_start=1272
  _globals['_ACTIVATETRANSFERREQUEST']._serialized_end=1330
  _globals['_TRANSFERSERVICE']._serialized_start=1333
  _globals['_TRANSFERSERVICE']._serialized_end=2255
# @@protoc_insertion_point(module_scope)
