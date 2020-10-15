from datetime import date, datetime, time

from typing import Optional, List
from pydantic import BaseModel, constr, UUID4

from .calling import Calling


class MatterBase(BaseModel):

    # Mandatory --------------------------------------------
    responder: constr(max_length=255, strip_whitespace=True)
    caller: Calling  # from schema/calling.py
    memo: str

    # Optional ---------------------------------------------
    title: Optional[constr(max_length=255, strip_whitespace=True)] = None  # default is 'タイトル未設定 ({timestamp})'
    place: Optional[constr(max_length=255, strip_whitespace=True)] = None
    dt: Optional[date] = None
    t: Optional[time] = None
    call_back_by: Optional[datetime] = None


class Matter(MatterBase):

    id: UUID4
    timestamp: datetime


class Matters(BaseModel):
    records: List[Matter]
