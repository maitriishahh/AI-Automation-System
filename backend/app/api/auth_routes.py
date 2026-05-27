from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.auth_schema import (
    SignupRequest,
    LoginRequest
)

from app.services.auth_service import (
    signup_user,
    login_user
)

from app.auth.dependencies import (
    get_current_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/signup")
def signup(
    data: SignupRequest,
    db: Session = Depends(get_db)
):

    token = signup_user(data, db)

    if not token:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    return {
        "message": "User registered successfully",
        "access_token": token,
        "token_type": "bearer"
    }


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    data = LoginRequest(
        email=form_data.username,
        password=form_data.password
    )

    token = login_user(data, db)

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return {
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/me")
def me(
    current_user = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "email": current_user.email,
        "workspace_id": current_user.workspace_id
    }