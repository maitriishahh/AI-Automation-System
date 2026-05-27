from sqlalchemy.orm import Session

from app.models.user_model import User
from app.models.workspace_model import Workspace

from app.auth.hashing import (
    hash_password,
    verify_password
)

from app.auth.jwt_handler import create_access_token


def signup_user(data, db: Session):

    existing_user = db.query(User).filter(
        User.email == data.email
    ).first()

    if existing_user:
        return None

    try:

        workspace = Workspace(
            name=data.workspace_name
        )

        db.add(workspace)

        db.flush()

        user = User(
            email=data.email,
            hashed_password=hash_password(data.password),
            workspace_id=workspace.id
        )

        db.add(user)

        db.commit()

        db.refresh(user)

        token = create_access_token({
            "sub": user.email,
            "workspace_id": user.workspace_id
        })

        return token

    except Exception as e:

        db.rollback()

        raise e


def login_user(data, db: Session):

    user = db.query(User).filter(
        User.email == data.email
    ).first()

    if not user:
        return None

    valid = verify_password(
        data.password,
        user.hashed_password
    )

    if not valid:
        return None

    token = create_access_token({
        "sub": user.email,
        "workspace_id": user.workspace_id
    })

    return token