from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from app.db.database import Base


class Lead(Base):

    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)

    workspace_id = Column(
        Integer,
        ForeignKey("workspaces.id")
    )

    name = Column(String)

    email = Column(String)

    lead_score = Column(Integer, default=0)

    status = Column(String, default="new")