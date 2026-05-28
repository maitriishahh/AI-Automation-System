from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    JSON
)

from sqlalchemy.sql import func

from app.db.database import Base


class WorkflowRun(Base):

    __tablename__ = "workflow_runs"

    id = Column(Integer, primary_key=True, index=True)

    workflow_name = Column(String, nullable=False)

    status = Column(String, nullable=False)

    workspace_id = Column(Integer)

    started_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    finished_at = Column(
        DateTime(timezone=True),
        nullable=True
    )

    execution_results = Column(
        JSON,
        nullable=True
    )

    error_message = Column(
        String,
        nullable=True
    )