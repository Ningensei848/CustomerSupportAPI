from typing import List
from fastapi import APIRouter, Depends

from CustomerSupportAPI.crud import matter as crud
from CustomerSupportAPI.models.matter import MatterModel
from CustomerSupportAPI.schemas.matter import MatterBase, Matter, Matters
from CustomerSupportAPI.adapters.matter import MatterAdapter


router = APIRouter()


# POST --------------------------------------------------------------
@router.post("/create")
def post_calling(matter: MatterBase) -> Matter:
    instance = crud.create_object(MatterAdapter.from_req(matter))
    return MatterAdapter.from_model(instance)


# GET ---------------------------------------------------------------
@router.get("/")
def get_matters(
    matters: List[MatterModel] = Depends(crud.retrieve_all_matters),
) -> Matters:
    return MatterAdapter.from_qs(matters)


@router.get("/{matter_id}")
def get_matter(
    matter: MatterModel = Depends(crud.retrieve_matter_by_id),
) -> Matter:
    return MatterAdapter.from_model(matter)
