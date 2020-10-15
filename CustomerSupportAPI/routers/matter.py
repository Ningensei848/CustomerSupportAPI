from typing import List
from fastapi import APIRouter, Depends

from CustomerSupportAPI.crud import matter as crud
from CustomerSupportAPI.models.matter import MatterModel
from CustomerSupportAPI.schemas.matter import Matter, Matters
from CustomerSupportAPI.adapters.matter import MatterAdapter


router = APIRouter()


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
