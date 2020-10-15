
from CustomerSupportAPI.models.matter import MatterModel, title_default
from CustomerSupportAPI.schemas.matter import MatterBase, Matter, Matters

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

    @classmethod
    def from_req(cls, schema: MatterBase):
        """
        Return a MatterModel instance(django) from an MatterBase instance(fastapi schema).
        => convert fastapi schema to Django instance.
        """
        return MatterModel(
            responder=schema.responder,
            # TODO: Cannot assign "Calling(name='sato', phone_number='03-9876-3546', affiliation=None, id=None)":
            # "MatterModel.caller" must be a "CallingModel" instance.
            caller=CallingAdapter.validate_calling_id(schema.caller),
            memo=schema.memo,
            title=title_default() if schema.title is None else schema.title,  # cf. https://note.nkmk.me/python-if-conditional-expressions/
            place=schema.place,
            date=schema.dt,
            time=schema.t,
            call_back_by=schema.call_back_by
        )
    # def from_multi_req():
    # @classmethod
    # def validate_matter_title(cls, schema: MatterBase):
