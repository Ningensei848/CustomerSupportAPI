from typing import Type, TypeVar
from fastapi import HTTPException, Path
from django.db import models

from CustomerSupportAPI.models.calling import CallingModel


modelType = TypeVar("modelType", bound=models.Model)

# `->` is type annotation of return value(s)


def retieve_object_by_id(model_class: Type[modelType], id: int) -> modelType:
    instance = model_class.objects.filter(pk=id).first()
    if not instance:
        raise HTTPException(status_code=404, detail="Object not found.")
    return instance


def retrieve_calling_by_id(
    calling_id: int = Path(..., description="retrive calling from db")
) -> CallingModel:
    return retieve_object_by_id(CallingModel, calling_id)  # return `Django model` instance


def retrieve_all_callings():
    return CallingModel.objects.all()
