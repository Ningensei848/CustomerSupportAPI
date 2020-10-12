from typing import List

from fastapi import APIRouter
from fastapi import Depends


from CustomerSupportAPI.adapters import matter as adapter
from CustomerSupportAPI.models.matter import MatterModel
from CustomerSupportAPI.schemas.matter import Matter, Matters

router = APIRouter()


@router.get("/")
def get_matters(
    matters: List[MatterModel] = Depends(adapter.retrieve_all_matters),
) -> Matters:
    return Matters.from_model_multiple(matters)


@router.get("/{matter_id}")
def get_matter(
    matter: MatterModel = Depends(adapter.retrieve_matter),
) -> Matter:
    return Matter.from_model(matter)
