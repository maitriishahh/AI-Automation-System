from sqlalchemy.orm import Session
from datetime import datetime, UTC

from app.models.workflow_run_model import WorkflowRun


class LogService:

    @staticmethod
    def create_workflow_run(
        db: Session,
        workflow_name: str,
        workspace_id: int
    ):

        workflow_run = WorkflowRun(
            workflow_name=workflow_name,
            status="running",
            workspace_id=workspace_id
        )

        db.add(workflow_run)

        db.commit()

        db.refresh(workflow_run)

        return workflow_run

    @staticmethod
    def complete_workflow_run(
        db: Session,
        workflow_run: WorkflowRun,
        execution_results: dict
    ):

        workflow_run.status = "completed"

        workflow_run.finished_at = datetime.utcnow()

        workflow_run.execution_results = execution_results

        db.commit()

    @staticmethod
    def fail_workflow_run(
        db: Session,
        workflow_run: WorkflowRun,
        error_message: str
    ):

        workflow_run.status = "failed"

        workflow_run.finished_at = datetime.now(UTC)

        workflow_run.error_message = error_message

        db.commit()

    @staticmethod
    def get_workflow_runs(
        db: Session,
        workspace_id: int
    ):

        runs = db.query(WorkflowRun).filter(
            WorkflowRun.workspace_id == workspace_id
        ).all()

        return runs