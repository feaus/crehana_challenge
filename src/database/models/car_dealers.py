import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from src.database.connection import Base


class CarDealers(Base):
    __tablename__ = "car_dealers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    city = Column(String)
    country = Column(String)
    car_brand = Column(String)
