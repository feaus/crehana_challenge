import datetime
import uuid

from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel
from typing import Optional


class CarDealersModel(BaseModel):
    id: uuid.UUID
    name: str
    city: str
    country: str
    car_brand: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: Optional[datetime.datetime]


class CarDealersGraphQLModel(PydanticObjectType):
    class Meta:
        model = CarDealersModel


class CarDealersGraphQLInputModel(PydanticInputObjectType):
    class Meta:
        model = CarDealersModel
        exclude_fields = ('id',)
