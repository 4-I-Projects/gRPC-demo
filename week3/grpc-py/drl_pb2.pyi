import gpa_pb2 as _gpa_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DRLRequest(_message.Message):
    __slots__ = ("student_id", "drl_score")
    STUDENT_ID_FIELD_NUMBER: _ClassVar[int]
    DRL_SCORE_FIELD_NUMBER: _ClassVar[int]
    student_id: _gpa_pb2.StudentId
    drl_score: float
    def __init__(self, student_id: _Optional[_Union[_gpa_pb2.StudentId, _Mapping]] = ..., drl_score: _Optional[float] = ...) -> None: ...

class DRLResponse(_message.Message):
    __slots__ = ("drl_score",)
    DRL_SCORE_FIELD_NUMBER: _ClassVar[int]
    drl_score: float
    def __init__(self, drl_score: _Optional[float] = ...) -> None: ...
