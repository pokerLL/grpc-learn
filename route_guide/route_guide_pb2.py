# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: route_guide.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11route_guide.proto\x12\nrouteguide\",\n\x05Point\x12\x10\n\x08latitude\x18\x01 \x01(\x05\x12\x11\n\tlongitude\x18\x02 \x01(\x05\"I\n\tRectangle\x12\x1d\n\x02lo\x18\x01 \x01(\x0b\x32\x11.routeguide.Point\x12\x1d\n\x02hi\x18\x02 \x01(\x0b\x32\x11.routeguide.Point\"<\n\x07\x46\x65\x61ture\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x08location\x18\x02 \x01(\x0b\x32\x11.routeguide.Point\"A\n\tRouteNote\x12#\n\x08location\x18\x01 \x01(\x0b\x32\x11.routeguide.Point\x12\x0f\n\x07message\x18\x02 \x01(\t\"b\n\x0cRouteSummary\x12\x13\n\x0bpoint_count\x18\x01 \x01(\x05\x12\x15\n\rfeature_count\x18\x02 \x01(\x05\x12\x10\n\x08\x64istance\x18\x03 \x01(\x05\x12\x14\n\x0c\x65lapsed_time\x18\x04 \x01(\x05\x32\x85\x02\n\nRouteGuide\x12\x36\n\nGetFeature\x12\x11.routeguide.Point\x1a\x13.routeguide.Feature\"\x00\x12>\n\x0cListFeatures\x12\x15.routeguide.Rectangle\x1a\x13.routeguide.Feature\"\x00\x30\x01\x12>\n\x0bRecordRoute\x12\x11.routeguide.Point\x1a\x18.routeguide.RouteSummary\"\x00(\x01\x12?\n\tRouteChat\x12\x15.routeguide.RouteNote\x1a\x15.routeguide.RouteNote\"\x00(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'route_guide_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POINT._serialized_start=33
  _POINT._serialized_end=77
  _RECTANGLE._serialized_start=79
  _RECTANGLE._serialized_end=152
  _FEATURE._serialized_start=154
  _FEATURE._serialized_end=214
  _ROUTENOTE._serialized_start=216
  _ROUTENOTE._serialized_end=281
  _ROUTESUMMARY._serialized_start=283
  _ROUTESUMMARY._serialized_end=381
  _ROUTEGUIDE._serialized_start=384
  _ROUTEGUIDE._serialized_end=645
# @@protoc_insertion_point(module_scope)
