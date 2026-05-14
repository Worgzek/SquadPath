from sqlalchemy import Column, String, Integer, ARRAY
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.data.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    career_goal = Column(String, nullable=True)
    skills = Column(ARRAY(String), default=[])
    commitment_score = Column(Integer, default=0)
    avatar_url = Column(String, nullable=True)