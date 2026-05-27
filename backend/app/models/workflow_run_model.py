from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func

from app.db.database import Base


class WorkflowRun(Base):

    __tablename__ = "workflow_runs"

    id = Column(Integer, primary_key=True, index=True)

    workflow_id = Column(
        Integer,
        ForeignKey("workflows.id")
    )

    status = Column(String)

    retry_count = Column(Integer, default=0)

    started_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    finished_at = Column(
        DateTime(timezone=True),
        nullable=True
    )