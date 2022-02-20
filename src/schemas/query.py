import datetime

import graphene

from src.database.connection import SessionLocal
from src.database.models.car_dealers import CarDealers
from src.database.models.cars import Cars
from src.serializers.cars import CarsGraphQLInputModel, CarsGraphQLModel
from src.serializers.car_dealers import (
    CarDealersGraphQLInputModel,
    CarDealersGraphQLModel,
)


db = SessionLocal()


class Query(graphene.ObjectType):
    list_cars = graphene.List(CarsGraphQLModel)
    list_dealers = graphene.List(CarDealersGraphQLModel)
    get_car = graphene.Field(
        CarsGraphQLModel,
        car_id=graphene.NonNull(graphene.UUID),
    )
    get_car_dealer = graphene.Field(
        CarDealersGraphQLModel,
        dealer_id=graphene.NonNull(graphene.UUID),
    )

    @staticmethod
    def resolve_list_cars(parent, info):
        return db.query(Cars).filter(Cars.deleted_at == None).all()

    @staticmethod
    def resolve_list_dealers(parent, info):
        return db.query(CarDealers).filter(CarDealers.deleted_at == None).all()

    @staticmethod
    def resolve_get_car(parent, info, car_id):
        return db.query(Cars).filter(
            Cars.id == car_id,
            Cars.deleted_at == None,
        ).first()

    @staticmethod
    def resolve_get_car_dealer(parent, info, dealer_id):
        return db.query(CarDealers).filter(
            CarDealers.id == dealer_id,
            CarDealers.deleted_at == None,
        ).first()


class CreateCar(graphene.Mutation):
    class Arguments:
        car_details = CarsGraphQLInputModel()

    Output = CarsGraphQLModel

    @staticmethod
    def mutate(parent, info, car_details):
        car = Cars()
        car.brand = car_details.brand
        car.model = car_details.model
        car.year = car_details.year

        db.add(car)
        db.commit()

        return car


class CreateCarDealer(graphene.Mutation):
    class Arguments:
        dealer_details = CarDealersGraphQLInputModel()

    Output = CarDealersGraphQLModel

    @staticmethod
    def mutate(parent, info, dealer_details):
        dealer = CarDealers()
        dealer.name = dealer_details.name
        dealer.city = dealer_details.city
        dealer.country = dealer_details.country
        dealer.car_brand = dealer_details.car_brand

        db.add(dealer)
        db.commit()

        return dealer


class EditCar(graphene.Mutation):
    class Arguments:
        car_id = graphene.UUID(required=True)
        car_details = CarsGraphQLInputModel()

    Output = CarsGraphQLModel

    @staticmethod
    def mutate(parent, info, car_id, car_details):
        car: Cars = db.query(Cars).filter(
            Cars.id == car_id,
            Cars.deleted_at == None
        ).first()

        if car is None:
            return

        for key, value in car_details.items():
            if value is not None:
                setattr(car, key, value)

        db.commit()

        return car


class EditCarDealer(graphene.Mutation):
    class Arguments:
        dealer_id = graphene.UUID(required=True)
        dealer_details = CarDealersGraphQLInputModel()

    Output = CarDealersGraphQLModel

    @staticmethod
    def mutate(parent, info, dealer_id, dealer_details):
        dealer: CarDealers = db.query(CarDealers).filter(
            CarDealers.id == dealer_id,
            CarDealers.deleted_at == None
        ).first()

        if dealer is None:
            return

        for key, value in dealer_details.items():
            if value is not None:
                setattr(dealer, key, value)

        db.commit()

        return dealer


class DeleteCar(graphene.Mutation):
    class Arguments:
        car_id = graphene.UUID(required=True)

    Output = CarsGraphQLModel

    @staticmethod
    def mutate(parent, info, car_id):
        car: Cars = db.query(Cars).filter(Cars.id == car_id).first()
        car.deleted_at = datetime.datetime.now()
        db.commit()
        return


class DeleteCarDealer(graphene.Mutation):
    class Arguments:
        dealer_id = graphene.UUID(required=True)

    Output = CarDealersGraphQLModel

    @staticmethod
    def mutate(parent, info, dealer_id):
        dealer: CarDealers = db.query(CarDealers).filter(
            CarDealers.id == dealer_id).first()
        dealer.deleted_at = datetime.datetime.now()
        db.commit()
        return


class Mutation(graphene.ObjectType):
    create_car = CreateCar.Field()
    create_car_dealer = CreateCarDealer.Field()
    edit_car = EditCar.Field()
    edit_car_dealer = EditCarDealer.Field()
    delete_car = DeleteCar.Field()
    delete_dealer = DeleteCarDealer.Field()
