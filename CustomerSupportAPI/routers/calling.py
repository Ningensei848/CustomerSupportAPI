from typing import List

from fastapi import APIRouter
from fastapi import Depends


from CustomerSupportAPI.adapters import calling as adapter
from CustomerSupportAPI.models.calling import CallingModel
from CustomerSupportAPI.schemas.calling import Calling, Callings

router = APIRouter()


@router.get("/")
def get_callings(
    callings: List[CallingModel] = Depends(adapter.retrieve_all_callings),
) -> Callings:
    return Callings.from_model_multiple(callings)


@router.get("/{calling_id}")
def get_calling(
    calling: CallingModel = Depends(adapter.retrieve_calling),
) -> Calling:
    return Calling.from_model(calling)
