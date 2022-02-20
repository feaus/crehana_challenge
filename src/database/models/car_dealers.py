import datetime
import uuid

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from src.database.connection import Base


class CarDealers(Base):
    __tablename__ = "car_dealers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    car_brand = Column(String, nullable=False)
    created_at = Column(
        DateTime,
        default=datetime.datetime.now(),
        nullable=False,
    )
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now(),
        nullable=False,
    )
    deleted_at = Column(DateTime)
