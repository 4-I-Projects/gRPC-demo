from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Void(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StudentId(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GPAResponse(_message.Message):
    __slots__ = ("gpa_score",)
    GPA_SCORE_FIELD_NUMBER: _ClassVar[int]
    gpa_score: float
    def __init__(self, gpa_score: _Optional[float] = ...) -> None: ...

class GPARequest(_message.Message):
    __slots__ = ("student_id", "gpa_score")
    STUDENT_ID_FIELD_NUMBER: _ClassVar[int]
    GPA_SCORE_FIELD_NUMBER: _ClassVar[int]
    student_id: StudentId
    gpa_score: float
    def __init__(self, student_id: _Optional[_Union[StudentId, _Mapping]] = ..., gpa_score: _Optional[float] = ...) -> None: ...
