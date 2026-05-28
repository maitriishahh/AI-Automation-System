from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    JSON,
    DateTime,
    ForeignKey
)

from sqlalchemy.sql import func

from app.db.database import Base


class Workflow(Base):

    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    description = Column(String, nullable=True)

    workflow_json = Column(JSON, nullable=False)

    is_active = Column(Boolean, default=True)

    workspace_id = Column(
        Integer,
        ForeignKey("workspaces.id")
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )