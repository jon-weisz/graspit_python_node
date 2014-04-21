# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import grasp_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='execute_grasp.proto',
  package='graspit_rpcz',
  serialized_pb='\n\x13\x65xecute_grasp.proto\x12\x0cgraspit_rpcz\x1a\x0bgrasp.proto\"<\n\x13\x45xecuteGraspRequest\x12%\n\x05grasp\x18\x02 \x02(\x0b\x32\x16.graspit_rpcz.GraspMsg\">\n\x14\x45xecuteGraspResponse\x12\x14\n\x0cisSuccessful\x18\x01 \x02(\x08\x12\x10\n\x08\x65rrorMsg\x18\x02 \x01(\t2c\n\x13\x45xecuteGraspService\x12L\n\x03run\x12!.graspit_rpcz.ExecuteGraspRequest\x1a\".graspit_rpcz.ExecuteGraspResponse')




_EXECUTEGRASPREQUEST = descriptor.Descriptor(
  name='ExecuteGraspRequest',
  full_name='graspit_rpcz.ExecuteGraspRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='grasp', full_name='graspit_rpcz.ExecuteGraspRequest.grasp', index=0,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=50,
  serialized_end=110,
)


_EXECUTEGRASPRESPONSE = descriptor.Descriptor(
  name='ExecuteGraspResponse',
  full_name='graspit_rpcz.ExecuteGraspResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='isSuccessful', full_name='graspit_rpcz.ExecuteGraspResponse.isSuccessful', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='errorMsg', full_name='graspit_rpcz.ExecuteGraspResponse.errorMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=112,
  serialized_end=174,
)

_EXECUTEGRASPREQUEST.fields_by_name['grasp'].message_type = grasp_pb2._GRASPMSG
DESCRIPTOR.message_types_by_name['ExecuteGraspRequest'] = _EXECUTEGRASPREQUEST
DESCRIPTOR.message_types_by_name['ExecuteGraspResponse'] = _EXECUTEGRASPRESPONSE

class ExecuteGraspRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXECUTEGRASPREQUEST
  
  # @@protoc_insertion_point(class_scope:graspit_rpcz.ExecuteGraspRequest)

class ExecuteGraspResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXECUTEGRASPRESPONSE
  
  # @@protoc_insertion_point(class_scope:graspit_rpcz.ExecuteGraspResponse)

# @@protoc_insertion_point(module_scope)