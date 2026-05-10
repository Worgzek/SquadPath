from sqlalchemy import Column, Float, ARRAY, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.data.base import Base

class Match(Base):
    __tablename__ = "matches"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    candidate_id = Column(UUID(as_uuid=True), nullable=False)
    score = Column(Float, nullable=False)
    reasons = Column(ARRAY(String), default=[])