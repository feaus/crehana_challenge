import datetime
import uuid

from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel
from typing import Optional


class CarsModel(BaseModel):
    id: uuid.UUID
    brand: str
    model: str
    year: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: Optional[datetime.datetime]


class CarsGraphQLModel(PydanticObjectType):
    class Meta:
        model = CarsModel


class CarsGraphQLInputModel(PydanticInputObjectType):
    class Meta:
        model = CarsModel
        exclude_fields = ('id',)
