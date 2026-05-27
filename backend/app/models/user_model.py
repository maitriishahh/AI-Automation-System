from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)

from sqlalchemy.sql import func

from app.db.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, nullable=False)

    hashed_password = Column(String, nullable=False)

    workspace_id = Column(
        Integer,
        ForeignKey("workspaces.id")
    )

    role = Column(String, default="member")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )