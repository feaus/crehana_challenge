import datetime
import uuid

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from src.database.connection import Base


class Cars(Base):
    __tablename__ = "cars"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
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
