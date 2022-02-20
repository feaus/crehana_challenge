import random
import uuid

import graphene
import pytest
from graphene.test import Client

from src.database.connection import SessionLocal
from src.database.models.car_dealers import CarDealers
from src.database.models.cars import Cars
from src.schemas.query_and_mutations import Mutation, Query


db = SessionLocal()


@pytest.fixture(scope='module')
def client():
    client = Client(schema=graphene.Schema(query=Query, mutation=Mutation))
    return client


@pytest.fixture(scope='function')
def car():
    car = Cars()
    car.brand = f'Test brand {random.randint(1, 1000)}'
    car.model = f'Test model {random.randint(1, 1000)}'
    car.year = random.randint(1900, 2022)

    db.add(car)
    db.commit()
    yield car
    db.delete(car)


@pytest.fixture(scope='function')
def car_dealer():
    dealer = CarDealers()
    dealer.name = f'Test name {random.randint(1, 1000)}'
    dealer.city = f'Test city {random.randint(1, 1000)}'
    dealer.country = f'Test country {random.randint(1, 1000)}'
    dealer.car_brand = f'Test car_brand {random.randint(1, 1000)}'

    db.add(dealer)
    db.commit()
    yield dealer
    db.delete(dealer)


def test_create_car(client):
    query = f"""
    mutation createCar {{
        createCar(carDetails: {{
            brand: "Test brand",
            model: "Test model",
            year: {random.randint(1900, 2022)}
        }})
        {{
            id
            brand
            model
            year
        }}
    }}
    """

    result = client.execute(query)

    assert 'id' in result['data']['createCar']

    try:
        received_id = uuid.UUID(result['data']['createCar']['id'])
    except (AttributeError, ValueError):
        assert False

    assert isinstance(received_id, uuid.UUID)
    assert result['data']['createCar']['brand'] == "Test brand"
    assert result['data']['createCar']['model'] == "Test model"
    assert 1900 <= result['data']['createCar']['year'] <= 2022


def test_create_car_dealer(client):
    query = f"""
    mutation createCarDealer {{
        createCarDealer(dealerDetails: {{
            name: "Test name",
            city: "Test city",
            country: "Test country",
            carBrand: "Test carBrand"
        }})
        {{
            id
            name
            city
            country
            carBrand
        }}
    }}
    """

    result = client.execute(query)

    assert 'id' in result['data']['createCarDealer']

    try:
        received_id = uuid.UUID(result['data']['createCarDealer']['id'])
    except (AttributeError, ValueError):
        assert False

    assert isinstance(received_id, uuid.UUID)
    assert result['data']['createCarDealer']['name'] == "Test name"
    assert result['data']['createCarDealer']['city'] == "Test city"
    assert result['data']['createCarDealer']['country'] == "Test country"
    assert result['data']['createCarDealer']['carBrand'] == "Test carBrand"
