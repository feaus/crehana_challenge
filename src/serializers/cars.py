import uuid

from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel


class CarsModel(BaseModel):
    id: uuid.UUID
    brand: str
    model: str
    year: int


class CarDealersModel(BaseModel):
    id: uuid.UUID
    name: str
    city: str
    country: str
    car_brand: str


class CarsGraphQLModel(PydanticObjectType):
    class Meta:
        model = CarsModel


class CarDealersGraphQLModel(PydanticObjectType):
    class Meta:
        model = CarDealersModel


class CarsGraphQLInputModel(PydanticInputObjectType):
    class Meta:
        model = CarsModel
        exclude_fields = ('id',)


class CarDealersGraphQLInputModel(PydanticInputObjectType):
    class Meta:
        model = CarDealersModel
        exclude_fields = ('id',)
