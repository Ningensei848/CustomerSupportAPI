from datetime import date, datetime, time
from typing import Optional, List
from pydantic import BaseModel, constr

from CustomerSupportAPI.models.matter import MatterModel

from .calling import Calling


class Matter(BaseModel):

    responder: constr(max_length=255, strip_whitespace=True)
    caller: Calling
    memo: str

    title: Optional[constr(max_length=255, strip_whitespace=True)] = None
    place: Optional[constr(max_length=255, strip_whitespace=True)] = None
    dt: Optional[date] = None
    t: Optional[time] = None
    call_back_by: Optional[datetime] = None

    @classmethod
    def from_model(cls, instance: MatterModel):
        return cls(
            id=instance.id_,
            timestamp=instance.timestamp,
            responder=instance.responder,
            caller=instance.caller,
            memo=instance.memo,
            title=instance.title,
            place=instance.place,
            dt=instance.date,
            t=instance.time,
            call_back_by=instance.call_back_by
        )


class Matters(BaseModel):
    records: List[Matter]

    @classmethod
    def from_model_multiple(cls, instances):
        return cls(records=[Matter.from_model(inst) for inst in instances])
