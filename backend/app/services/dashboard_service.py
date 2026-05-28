from sqlalchemy.orm import Session

from app.models.workflow_model import Workflow
from app.models.workflow_run_model import WorkflowRun
from app.models.integration_model import Integration


class DashboardService:

    @staticmethod
    def get_overview(
        db: Session,
        workspace_id: int
    ):

        total_workflows = db.query(
            Workflow
        ).filter(
            Workflow.workspace_id == workspace_id
        ).count()

        workflow_runs = db.query(
            WorkflowRun
        ).filter(
            WorkflowRun.workspace_id == workspace_id
        ).count()

        successful_runs = db.query(
            WorkflowRun
        ).filter(
            WorkflowRun.workspace_id == workspace_id,
            WorkflowRun.status == "completed"
        ).count()

        failed_runs = db.query(
            WorkflowRun
        ).filter(
            WorkflowRun.workspace_id == workspace_id,
            WorkflowRun.status == "failed"
        ).count()

        pending_jobs = db.query(
            WorkflowRun
        ).filter(
            WorkflowRun.workspace_id == workspace_id,
            WorkflowRun.status == "pending"
        ).count()

        success_rate = 0

        if workflow_runs > 0:

            success_rate = round(
                (
                    successful_runs /
                    workflow_runs
                ) * 100,
                2
            )

        return {

            "total_workflows":
            total_workflows,

            "workflow_runs":
            workflow_runs,

            "successful_runs":
            successful_runs,

            "failed_runs":
            failed_runs,

            "pending_jobs":
            pending_jobs,

            "success_rate":
            success_rate
        }

    @staticmethod
    def get_workflow_stats(
        db: Session,
        workspace_id: int
    ):

        workflows = db.query(
            Workflow
        ).filter(
            Workflow.workspace_id == workspace_id
        ).all()

        results = []

        for workflow in workflows:

            total_runs = db.query(
                WorkflowRun
            ).filter(
                WorkflowRun.workspace_id == workspace_id,
                WorkflowRun.workflow_name == workflow.name
            ).count()

            successful_runs = db.query(
                WorkflowRun
            ).filter(
                WorkflowRun.workspace_id == workspace_id,
                WorkflowRun.workflow_name == workflow.name,
                WorkflowRun.status == "completed"
            ).count()

            failed_runs = db.query(
                WorkflowRun
            ).filter(
                WorkflowRun.workspace_id == workspace_id,
                WorkflowRun.workflow_name == workflow.name,
                WorkflowRun.status == "failed"
            ).count()

            results.append({

                "workflow_id":
                workflow.id,

                "workflow_name":
                workflow.name,

                "total_runs":
                total_runs,

                "successful_runs":
                successful_runs,

                "failed_runs":
                failed_runs
            })

        return results

    @staticmethod
    def get_logs(
        db: Session,
        workspace_id: int
    ):

        logs = db.query(
            WorkflowRun
        ).filter(
            WorkflowRun.workspace_id == workspace_id
        ).order_by(
            WorkflowRun.id.desc()
        ).all()

        return logs

    @staticmethod
    def get_integrations(
        db: Session,
        workspace_id: int
    ):

        integrations = db.query(
            Integration
        ).filter(
            Integration.workspace_id == workspace_id
        ).all()

        return integrations