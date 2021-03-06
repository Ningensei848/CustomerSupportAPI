from django.db import models
from typing import Type, TypeVar
from pydantic import UUID4
from fastapi import HTTPException, Path

from CustomerSupportAPI.models.matter import MatterModel


modelType = TypeVar("modelType", bound=models.Model)

# ----------------------------------------------------------------------------------
# CREATE object(s) -----------------------------------------------------------------


def create_object(instance: MatterModel) -> MatterModel:
    instance.save()
    return instance

# RETRIEVE object(s) ---------------------------------------------------------------


def retrieve_object_by_id(model_class: Type[modelType], id: UUID4) -> modelType:
    instance = model_class.objects.filter(pk=id).first()
    if not instance:
        raise HTTPException(status_code=404, detail="Object not found.")
    return instance


def retrieve_matter_by_id(
    matter_id: UUID4 = Path(..., description="retrive matter from db")
) -> MatterModel:
    return retrieve_object_by_id(MatterModel, matter_id)


def retrieve_all_matters():
    return MatterModel.objects.all()
