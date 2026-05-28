from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.services.workflow_service import (
    WorkflowService
)


router = APIRouter(
    prefix="/webhooks",
    tags=["Webhooks"]
)


@router.post("/{workflow_id}")
async def webhook_trigger(
    workflow_id: int,
    payload: dict,
    db: Session = Depends(get_db)
):

    try:

        result = await WorkflowService.execute_db_workflow(
            db=db,
            workflow_id=workflow_id,
            payload=payload,
            workspace_id=None
        )

        return {
            "status": "success",
            "workflow_id": workflow_id,
            "result": result
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )