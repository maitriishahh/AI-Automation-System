from sqlalchemy.orm import Session

from app.workflows.engine import WorkflowEngine
from app.workflows.template_registry import get_template
from app.workflows.validators import WorkflowValidator

from app.services.log_service import LogService

from app.models.workflow_model import Workflow


class WorkflowService:

    @staticmethod
    async def execute_template_workflow(
        db: Session,
        template_name: str,
        payload: dict,
        workspace_id: int
    ):

        workflow_run = LogService.create_workflow_run(
            db=db,
            workflow_name=template_name,
            workspace_id=workspace_id
        )

        try:

            workflow_json = get_template(template_name)

            result = await WorkflowEngine.run_workflow(
                workflow_json=workflow_json,
                payload=payload
            )

            LogService.complete_workflow_run(
                db=db,
                workflow_run=workflow_run,
                execution_results=result
            )

            return result

        except Exception as e:

            LogService.fail_workflow_run(
                db=db,
                workflow_run=workflow_run,
                error_message=str(e)
            )

            raise e

    @staticmethod
    def create_workflow(
        db: Session,
        workflow_data,
        workspace_id: int
    ):

        WorkflowValidator.validate(
            workflow_data.workflow_json
        )

        workflow = Workflow(
            name=workflow_data.name,
            description=workflow_data.description,
            workflow_json=workflow_data.workflow_json,
            workspace_id=workspace_id
        )

        db.add(workflow)

        db.commit()

        db.refresh(workflow)

        return workflow

    @staticmethod
    async def execute_db_workflow(
        db: Session,
        workflow_id: int,
        payload: dict,
        workspace_id: int
    ):

        query = db.query(Workflow).filter(Workflow.id==workflow_id)

        if workspace_id is not None:
            query = query.filter(
                Workflow.workspace_id == workspace_id
            )
        workflow = query.first()

        if not workflow:
            raise Exception("Workflow not found")

        if not workflow.is_active:
            raise Exception("Workflow is inactive")

        workflow_run = LogService.create_workflow_run(
            db=db,
            workflow_name=workflow.name,
            workspace_id=workspace_id
        )

        try:

            result = await WorkflowEngine.run_workflow(
                workflow_json=workflow.workflow_json,
                payload=payload
            )

            LogService.complete_workflow_run(
                db=db,
                workflow_run=workflow_run,
                execution_results=result
            )

            return result

        except Exception as e:

            LogService.fail_workflow_run(
                db=db,
                workflow_run=workflow_run,
                error_message=str(e)
            )

            raise e

    @staticmethod
    def get_all_workflows(
        db: Session,
        workspace_id: int
    ):

        workflows = db.query(Workflow).filter(
            Workflow.workspace_id == workspace_id
        ).all()

        return workflows

    @staticmethod
    def get_workflow_by_id(
        db: Session,
        workflow_id: int,
        workspace_id: int
    ):

        workflow = db.query(Workflow).filter(
            Workflow.id == workflow_id,
            Workflow.workspace_id == workspace_id
        ).first()

        return workflow

    @staticmethod
    def toggle_workflow_status(
        db: Session,
        workflow_id: int,
        workspace_id: int
    ):

        workflow = db.query(Workflow).filter(
            Workflow.id == workflow_id,
            Workflow.workspace_id == workspace_id
        ).first()

        if not workflow:
            raise Exception("Workflow not found")

        workflow.is_active = not workflow.is_active

        db.commit()

        db.refresh(workflow)

        return workflow