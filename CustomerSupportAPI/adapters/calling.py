
from CustomerSupportAPI.models.calling import CallingModel
from CustomerSupportAPI.schemas.calling import CallingBase, Calling, Callings


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

    @classmethod
    def from_req(cls, schema: CallingBase):
        """
        Return a CallingModel instance(django) from an CallingBase instance(fastapi schema).
        => convert fastapi schema to Django instance.
        """
        return CallingModel(
            name=schema.name,
            phone_number=schema.phone_number,
            affiliation=schema.affiliation,
        )

    # def from_multi_req():

    @classmethod
    def validate_calling_id(cls, schema: Calling) -> CallingModel:
        """
        もしidがなければ，Django側でIDをインクリメントする（ために，idを削除する）
        あれば，フロント側でIDを指定してPOSTしてきたことになる（からなにもしない）
        """
        calling_dict = schema.dict()
        if calling_dict['id'] is None:
            del calling_dict['id']
            inst = CallingModel(**calling_dict)
            inst.save()  # 未登録のデータを保存
        else:
            inst = CallingModel(**calling_dict)
        return inst
