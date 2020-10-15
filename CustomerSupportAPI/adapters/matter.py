
from CustomerSupportAPI.models.matter import MatterModel  # and,  MatterBase
from CustomerSupportAPI.schemas.matter import Matter, Matters

from .calling import CallingAdapter


class MatterAdapter:

    @classmethod
    def from_model(cls, instance: MatterModel):
        """
        Convert Django Model Instance To Schema instance in Pydantic
        """
        return Matter(
            id=instance.id,
            timestamp=instance.timestamp,
            responder=instance.responder,
            caller=CallingAdapter.from_model(instance.caller),  # for ForeignKey
            memo=instance.memo,
            title=instance.title,
            place=instance.place,
            dt=instance.date,
            t=instance.time,
            call_back_by=instance.call_back_by
        )

    @classmethod
    def from_qs(cls, instances):  # type of instances is `django Queryset`
        return Matters(records=[cls.from_model(inst) for inst in instances])
    # def from_req():
    # def from_multi_req():
