from typing import Type, TypeVar
from pydantic import UUID4
from fastapi import HTTPException, Path
from django.db import models

from CustomerSupportAPI.models.matter import MatterModel

modelType = TypeVar("modelType", bound=models.Model)


def retieve_object(model_class: Type[modelType], id: UUID4) -> modelType:
    instance = model_class.objects.filter(pk=id).first()
    if not instance:
        raise HTTPException(status_code=404, detail="Object not found.")
    return instance


def retrieve_matter(
    matter_id: UUID4 = Path(..., description="retrive matter from db")
) -> MatterModel:
    return retieve_object(MatterModel, matter_id)


def retrieve_all_matters():
    return MatterModel.objects.all()
