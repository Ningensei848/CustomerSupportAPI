
from CustomerSupportAPI.models.calling import CallingModel  # and,  CallingBase
from CustomerSupportAPI.schemas.calling import Calling, Callings


class CallingAdapter:

    @classmethod
    def from_model(cls, instance: CallingModel):
        """
        Convert Django Model Instance To Schema instance in Pydantic
        """
        return Calling(
            id=instance.id,
            name=instance.name,
            phone_number=str(instance.phone_number),  # cf. https://github.com/stefanfoulis/django-phonenumber-field/blob/7a5d8010c182058dc8d0e1e20cf66f541860eb73/phonenumber_field/phonenumber.py#L34
            affiliation=instance.affiliation
        )

    @classmethod
    def from_qs(cls, instances):  # type of instances is `django Queryset`
        return Callings(records=[cls.from_model(inst) for inst in instances])
    # def from_req():
    # def from_multi_req():
