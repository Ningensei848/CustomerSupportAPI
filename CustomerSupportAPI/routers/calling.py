from typing import List

from fastapi import APIRouter
from fastapi import Depends


from CustomerSupportAPI.adapters import calling as adapter
from CustomerSupportAPI.models.calling import CallingModel

from CustomerSupportAPI.schemas.calling import Calling, Callings

router = APIRouter()

# MEMO: schemaを経由するのはあくまでも型付けのため => CURDが働いているわけではない
# i. e., adapterをCURDに変えるべき


@router.get("/")
def get_callings(
    callings: List[CallingModel] = Depends(adapter.retrieve_all_callings),
) -> Callings:
    return Callings.from_model_multiple(callings)


@router.get("/{calling_id}")
def get_calling(
    calling: CallingModel = Depends(adapter.retrieve_calling_by_id),
) -> Calling:
    """
    calling: Django model
    return( Calling.from_model(calling) ): FastAPI instance
    """
    return Calling.from_model(calling)

# routerはadapterが取ってきた「django」modelのインスタンスの依存性を検証し，
# args: , return: None(or message)
# @router.post("/create")
# def post_calling(calling: CallingModel = Depends(adapter.retrieve_calling_by_id)  ):
#     return
