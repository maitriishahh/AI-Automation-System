from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.services.workflow_service import WorkflowService
from app.services.log_service import LogService

from app.schemas.workflow_schema import (
    WorkflowCreate,
    WorkflowResponse,
    WorkflowRunResponse
)

from app.auth.dependencies import get_current_user

from app.models.user_model import User

router = APIRouter(
    prefix="/workflows",
    tags=["Workflows"]
)


@router.post("/execute/{template_name}")
async def execute_workflow(
    template_name: str,
    payload: dict,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    try:

        result = await WorkflowService.execute_template_workflow(
            db=db,
            template_name=template_name,
            payload=payload,
            workspace_id=current_user.workspace_id
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/", response_model=WorkflowResponse)
def create_workflow(
    workflow_data: WorkflowCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    try:

        workflow = WorkflowService.create_workflow(
            db=db,
            workflow_data=workflow_data,
            workspace_id=current_user.workspace_id
        )

        return workflow

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/{workflow_id}/execute")
async def execute_db_workflow(
    workflow_id: int,
    payload: dict,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    try:

        result = await WorkflowService.execute_db_workflow(
            db=db,
            workflow_id=workflow_id,
            payload=payload,
            workspace_id=current_user.workspace_id
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/runs/all",
    response_model=list[WorkflowRunResponse]
)
def get_workflow_runs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    runs = LogService.get_workflow_runs(
        db=db,
        workspace_id=current_user.workspace_id
    )

    return runs


@router.get("/", response_model=list[WorkflowResponse])
def get_workflows(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    workflows = WorkflowService.get_all_workflows(
        db=db,
        workspace_id=current_user.workspace_id
    )

    return workflows


@router.get(
    "/{workflow_id}",
    response_model=WorkflowResponse
)
def get_workflow(
    workflow_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    workflow = WorkflowService.get_workflow_by_id(
        db=db,
        workflow_id=workflow_id,
        workspace_id=current_user.workspace_id
    )

    return workflow


@router.patch("/{workflow_id}/toggle")
def toggle_workflow(
    workflow_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    workflow = WorkflowService.toggle_workflow_status(
        db=db,
        workflow_id=workflow_id,
        workspace_id=current_user.workspace_id
    )

    return {
        "message": "Workflow status updated",
        "workflow_id": workflow.id,
        "is_active": workflow.is_active
    }