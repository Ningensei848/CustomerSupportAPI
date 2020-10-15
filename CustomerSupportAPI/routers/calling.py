from typing import List
from fastapi import APIRouter, Depends

from CustomerSupportAPI.crud import calling as crud
from CustomerSupportAPI.models.calling import CallingModel
from CustomerSupportAPI.schemas.calling import CallingBase, Calling, Callings
from CustomerSupportAPI.adapters.calling import CallingAdapter


router = APIRouter()


@router.get("/")
def get_callings(
    callings: List[CallingModel] = Depends(crud.retrieve_all_callings),
) -> Callings:
    return CallingAdapter.from_qs(callings)


@router.get("/{calling_id}")
def get_calling(
    calling: CallingModel = Depends(crud.retrieve_calling_by_id),
) -> Calling:
    return CallingAdapter.from_model(calling)


@router.post("/create")
def post_calling(calling: CallingBase) -> Calling:
    instance = crud.create_object(CallingAdapter.from_req(calling))
    return CallingAdapter.from_model(instance)

# delete
# update
