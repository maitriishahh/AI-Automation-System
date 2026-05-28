from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/overview")
def get_overview(db: Session = Depends(get_db)):
    return DashboardService.get_overview(db)

@router.get("/workflows")
def get_workflow_stats(db: Session = Depends(get_db)):
    return DashboardService.get_workflow_stats(db)

@router.get("/logs")
def get_logs(db: Session = Depends(get_db)):
    return DashboardService.get_logs(db)

@router.get("/integrations")
def get_integrations(db: Session = Depends(get_db)):
    return DashboardService.get_integrations(db)