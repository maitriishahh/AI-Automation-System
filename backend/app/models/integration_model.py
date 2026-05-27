from sqlalchemy import (
    Column,
    Integer,
    String,
    JSON,
    ForeignKey
)

from app.db.database import Base


class Integration(Base):

    __tablename__ = "integrations"

    id = Column(Integer, primary_key=True, index=True)

    workspace_id = Column(
        Integer,
        ForeignKey("workspaces.id")
    )

    type = Column(String)

    credentials = Column(JSON)