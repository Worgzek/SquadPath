from sqlalchemy import Column, String, ARRAY
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.data.base import Base

class Squad(Base):
    __tablename__ = "squads"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    path = Column(String, nullable=False)
    member_ids = Column(ARRAY(UUID(as_uuid=True)), default=[])
    project_brief = Column(String, nullable=True)
    status = Column(String, default="forming")