from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.services.dashboard_service import (
    DashboardService
)

from app.auth.dependencies import (
    get_current_user
)

from app.models.user_model import User

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/overview")
def get_overview(

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user
    )
):

    return DashboardService.get_overview(

        db,

        current_user.workspace_id
    )


@router.get("/workflows")
def get_workflow_stats(

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user
    )
):

    return DashboardService.get_workflow_stats(

        db,

        current_user.workspace_id
    )


@router.get("/logs")
def get_logs(

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user
    )
):

    return DashboardService.get_logs(

        db,

        current_user.workspace_id
    )


@router.get("/integrations")
def get_integrations(

    db: Session = Depends(get_db),

    current_user: User = Depends(
        get_current_user
    )
):

    return DashboardService.get_integrations(

        db,

        current_user.workspace_id
    )