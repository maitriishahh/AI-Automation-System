from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
    ForeignKey
)

from app.db.database import Base


class Workflow(Base):

    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)

    workspace_id = Column(
        Integer,
        ForeignKey("workspaces.id")
    )

    name = Column(String, nullable=False)

    workflow_json = Column(JSON)

    status = Column(String, default="draft")