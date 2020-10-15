
# cf. https://github.com/daviddrysdale/python-phonenumbers
# cf. https://github.com/samuelcolvin/pydantic/issues/1551#issuecomment-700154597

from phonenumbers import (
    NumberParseException,
    PhoneNumberFormat,
    PhoneNumberType,
    format_number,
    is_valid_number,
    number_type,
    parse as parse_phone_number,
)
from typing import Optional, List
from pydantic import BaseModel, constr, PositiveInt, validator

MOBILE_NUMBER_TYPES = PhoneNumberType.MOBILE, PhoneNumberType.FIXED_LINE_OR_MOBILE

from CustomerSupportAPI.models.calling import CallingModel


class Calling(BaseModel):

    id: PositiveInt  # for default django auto-incremental ID
    name: constr(max_length=255, strip_whitespace=True)
    phone_number: constr(max_length=50, strip_whitespace=True)

    affiliation: Optional[constr(max_length=255, strip_whitespace=True)] = None

    @validator('phone_number')
    def check_phone_number(cls, v):
        try:
            n = parse_phone_number(v, 'JP')
        except NumberParseException as e:
            raise ValueError('Please provide a valid mobile phone number') from e

        if not is_valid_number(n) or number_type(n) not in MOBILE_NUMBER_TYPES:
            raise ValueError('Please provide a valid mobile phone number')

        return format_number(n, PhoneNumberFormat.NATIONAL if n.country_code == 81 else PhoneNumberFormat.INTERNATIONAL)

    @classmethod
    def from_model(cls, instance: CallingModel):
        return cls(
            id=instance.id,
            name=instance.name,
            phone_number=str(instance.phone_number),  # cf. https://github.com/stefanfoulis/django-phonenumber-field/blob/7a5d8010c182058dc8d0e1e20cf66f541860eb73/phonenumber_field/phonenumber.py#L34
            affiliation=instance.affiliation
        )


class Callings(BaseModel):
    records: List[Calling]

    @ classmethod
    def from_model_multiple(cls, instances):
        return cls(records=[Calling.from_model(inst) for inst in instances])
