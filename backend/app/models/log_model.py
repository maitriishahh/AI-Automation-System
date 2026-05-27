from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func

from app.db.database import Base


class Log(Base):

    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)

    workspace_id = Column(
        Integer,
        ForeignKey("workspaces.id")
    )

    action = Column(String)

    status = Column(String)

    message = Column(String)

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )