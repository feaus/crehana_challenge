import datetime
import uuid

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from src.database.connection import Base


class Posts(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    integration_id = Column(Integer, index=True, nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now(),
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now(),
    )
    deleted_at = Column(DateTime)
