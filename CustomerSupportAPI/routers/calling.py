from typing import List
from fastapi import APIRouter, Depends

from CustomerSupportAPI.crud import calling as crud
from CustomerSupportAPI.models.calling import CallingModel
from CustomerSupportAPI.schemas.calling import Calling, Callings
from CustomerSupportAPI.adapters.calling import CallingAdapter


router = APIRouter()


@router.get("/")
def get_callings(
    callings: List[CallingModel] = Depends(crud.retrieve_all_callings),
) -> Callings:
    return CallingAdapter.from_multi_model(callings)


@router.get("/{calling_id}")
def get_calling(
    calling: CallingModel = Depends(crud.retrieve_calling_by_id),
) -> Calling:
    return CallingAdapter.from_model(calling)

# routerはadapterが取ってきた「django」modelのインスタンスの依存性を検証し，
# args: , return: None(or message)
# @router.post("/create")
# def post_calling(calling: CallingModel = Depends(adapter.retrieve_calling_by_id)  ):
#     return
