# cf. https://github.com/daviddrysdale/python-phonenumbers
# cf. https://github.com/samuelcolvin/pydantic/issues/1551#issuecomment-700154597

from phonenumbers import (
    NumberParseException,
    PhoneNumberFormat,
    format_number,
    is_valid_number,
    parse as parse_phone_number,
)
from typing import Optional, List
from pydantic import BaseModel, constr, PositiveInt, validator


class CallingBase(BaseModel):
    name: constr(max_length=255, strip_whitespace=True)
    phone_number: constr(max_length=50, strip_whitespace=True)

    affiliation: Optional[constr(max_length=255, strip_whitespace=True)] = None

    @validator('phone_number')
    def check_phone_number(cls, v):
        try:
            n = parse_phone_number(v, 'JP')
        except NumberParseException as e:
            raise ValueError('Please provide a valid mobile phone number') from e

        if not is_valid_number(n):
            raise ValueError('Please provide a valid number')

        # 国コードが+81なら国内向けのフォーマットにして，そうでなければ国際線のフォーマットにして返す
        return format_number(n, PhoneNumberFormat.NATIONAL if n.country_code == 81 else PhoneNumberFormat.INTERNATIONAL)


class Calling(CallingBase):

    id: Optional[PositiveInt] = None  # for default django auto-incremental ID


class Callings(BaseModel):
    records: List[Calling]
