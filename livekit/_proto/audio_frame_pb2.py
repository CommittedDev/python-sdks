# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: audio_frame.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import handle_pb2 as handle__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61udio_frame.proto\x12\x07livekit\x1a\x0chandle.proto\"a\n\x17\x41llocAudioBufferRequest\x12\x13\n\x0bsample_rate\x18\x01 \x01(\r\x12\x14\n\x0cnum_channels\x18\x02 \x01(\r\x12\x1b\n\x13samples_per_channel\x18\x03 \x01(\r\"I\n\x18\x41llocAudioBufferResponse\x12-\n\x06\x62uffer\x18\x01 \x01(\x0b\x32\x1d.livekit.AudioFrameBufferInfo\"\x96\x01\n\x15NewAudioStreamRequest\x12)\n\x0broom_handle\x18\x01 \x01(\x0b\x32\x14.livekit.FFIHandleId\x12\x17\n\x0fparticipant_sid\x18\x02 \x01(\t\x12\x11\n\ttrack_sid\x18\x03 \x01(\t\x12&\n\x04type\x18\x04 \x01(\x0e\x32\x18.livekit.AudioStreamType\"B\n\x16NewAudioStreamResponse\x12(\n\x06stream\x18\x01 \x01(\x0b\x32\x18.livekit.AudioStreamInfo\"?\n\x15NewAudioSourceRequest\x12&\n\x04type\x18\x01 \x01(\x0e\x32\x18.livekit.AudioSourceType\"B\n\x16NewAudioSourceResponse\x12(\n\x06source\x18\x01 \x01(\x0b\x32\x18.livekit.AudioSourceInfo\"t\n\x18\x43\x61ptureAudioFrameRequest\x12+\n\rsource_handle\x18\x01 \x01(\x0b\x32\x14.livekit.FFIHandleId\x12+\n\rbuffer_handle\x18\x02 \x01(\x0b\x32\x14.livekit.FFIHandleId\"\x1b\n\x19\x43\x61ptureAudioFrameResponse\"\x1a\n\x18NewAudioResamplerRequest\"A\n\x19NewAudioResamplerResponse\x12$\n\x06handle\x18\x01 \x01(\x0b\x32\x14.livekit.FFIHandleId\"\xa1\x01\n\x17RemixAndResampleRequest\x12.\n\x10resampler_handle\x18\x01 \x01(\x0b\x32\x14.livekit.FFIHandleId\x12+\n\rbuffer_handle\x18\x02 \x01(\x0b\x32\x14.livekit.FFIHandleId\x12\x14\n\x0cnum_channels\x18\x03 \x01(\r\x12\x13\n\x0bsample_rate\x18\x04 \x01(\r\"I\n\x18RemixAndResampleResponse\x12-\n\x06\x62uffer\x18\x01 \x01(\x0b\x32\x1d.livekit.AudioFrameBufferInfo\"\x96\x01\n\x14\x41udioFrameBufferInfo\x12$\n\x06handle\x18\x01 \x01(\x0b\x32\x14.livekit.FFIHandleId\x12\x10\n\x08\x64\x61ta_ptr\x18\x02 \x01(\x04\x12\x14\n\x0cnum_channels\x18\x03 \x01(\r\x12\x13\n\x0bsample_rate\x18\x04 \x01(\r\x12\x1b\n\x13samples_per_channel\x18\x05 \x01(\r\"r\n\x0f\x41udioStreamInfo\x12$\n\x06handle\x18\x01 \x01(\x0b\x32\x14.livekit.FFIHandleId\x12&\n\x04type\x18\x02 \x01(\x0e\x32\x18.livekit.AudioStreamType\x12\x11\n\ttrack_sid\x18\x03 \x01(\t\"z\n\x10\x41udioStreamEvent\x12$\n\x06handle\x18\x01 \x01(\x0b\x32\x14.livekit.FFIHandleId\x12\x35\n\x0e\x66rame_received\x18\x02 \x01(\x0b\x32\x1b.livekit.AudioFrameReceivedH\x00\x42\t\n\x07message\"B\n\x12\x41udioFrameReceived\x12,\n\x05\x66rame\x18\x01 \x01(\x0b\x32\x1d.livekit.AudioFrameBufferInfo\"_\n\x0f\x41udioSourceInfo\x12$\n\x06handle\x18\x01 \x01(\x0b\x32\x14.livekit.FFIHandleId\x12&\n\x04type\x18\x02 \x01(\x0e\x32\x18.livekit.AudioSourceType*A\n\x0f\x41udioStreamType\x12\x17\n\x13\x41UDIO_STREAM_NATIVE\x10\x00\x12\x15\n\x11\x41UDIO_STREAM_HTML\x10\x01**\n\x0f\x41udioSourceType\x12\x17\n\x13\x41UDIO_SOURCE_NATIVE\x10\x00\x42\x10\xaa\x02\rLiveKit.Protob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'audio_frame_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\rLiveKit.Proto'
  _AUDIOSTREAMTYPE._serialized_start=1611
  _AUDIOSTREAMTYPE._serialized_end=1676
  _AUDIOSOURCETYPE._serialized_start=1678
  _AUDIOSOURCETYPE._serialized_end=1720
  _ALLOCAUDIOBUFFERREQUEST._serialized_start=44
  _ALLOCAUDIOBUFFERREQUEST._serialized_end=141
  _ALLOCAUDIOBUFFERRESPONSE._serialized_start=143
  _ALLOCAUDIOBUFFERRESPONSE._serialized_end=216
  _NEWAUDIOSTREAMREQUEST._serialized_start=219
  _NEWAUDIOSTREAMREQUEST._serialized_end=369
  _NEWAUDIOSTREAMRESPONSE._serialized_start=371
  _NEWAUDIOSTREAMRESPONSE._serialized_end=437
  _NEWAUDIOSOURCEREQUEST._serialized_start=439
  _NEWAUDIOSOURCEREQUEST._serialized_end=502
  _NEWAUDIOSOURCERESPONSE._serialized_start=504
  _NEWAUDIOSOURCERESPONSE._serialized_end=570
  _CAPTUREAUDIOFRAMEREQUEST._serialized_start=572
  _CAPTUREAUDIOFRAMEREQUEST._serialized_end=688
  _CAPTUREAUDIOFRAMERESPONSE._serialized_start=690
  _CAPTUREAUDIOFRAMERESPONSE._serialized_end=717
  _NEWAUDIORESAMPLERREQUEST._serialized_start=719
  _NEWAUDIORESAMPLERREQUEST._serialized_end=745
  _NEWAUDIORESAMPLERRESPONSE._serialized_start=747
  _NEWAUDIORESAMPLERRESPONSE._serialized_end=812
  _REMIXANDRESAMPLEREQUEST._serialized_start=815
  _REMIXANDRESAMPLEREQUEST._serialized_end=976
  _REMIXANDRESAMPLERESPONSE._serialized_start=978
  _REMIXANDRESAMPLERESPONSE._serialized_end=1051
  _AUDIOFRAMEBUFFERINFO._serialized_start=1054
  _AUDIOFRAMEBUFFERINFO._serialized_end=1204
  _AUDIOSTREAMINFO._serialized_start=1206
  _AUDIOSTREAMINFO._serialized_end=1320
  _AUDIOSTREAMEVENT._serialized_start=1322
  _AUDIOSTREAMEVENT._serialized_end=1444
  _AUDIOFRAMERECEIVED._serialized_start=1446
  _AUDIOFRAMERECEIVED._serialized_end=1512
  _AUDIOSOURCEINFO._serialized_start=1514
  _AUDIOSOURCEINFO._serialized_end=1609
# @@protoc_insertion_point(module_scope)
