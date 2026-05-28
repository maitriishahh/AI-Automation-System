import asyncio
import traceback

from app.queue.queue_manager import (
    get_next_job
)

from app.db.session import SessionLocal

from app.services.workflow_service import (
    WorkflowService
)

from app.models.workflow_model import Workflow

from app.integrations.gmail_service import (
    send_email
)

from app.workflows.constants import (

    EXECUTION_RUNNING,
    EXECUTION_SUCCESS,
    EXECUTION_FAILED
)


async def start_worker():

    print("Worker started...")

    while True:

        job = get_next_job()

        if job:

            db = SessionLocal()

            try:

                print(f"\nExecuting job: {job}")

                job_type = job.get("type")

                payload = job.get("payload")

                workspace_id = job.get(
                    "workspace_id"
                )

                # ==========================================
                # DATABASE WORKFLOW EXECUTION
                # ==========================================

                if job_type == "database":

                    workflow_id = job.get(
                        "workflow_id"
                    )

                    # GET WORKFLOW

                    workflow = db.query(
                        Workflow
                    ).filter(
                        Workflow.id == workflow_id
                    ).first()

                    # EXECUTE WORKFLOW

                    result = await WorkflowService.execute_db_workflow(
                        db=db,
                        workflow_id=workflow_id,
                        payload=payload,
                        workspace_id=workspace_id
                    )

                    print(EXECUTION_SUCCESS)

                    print(result)

                    # ==========================================
                    # NODE-BASED WORKFLOW EXECUTION
                    # ==========================================

                    if workflow:

                        workflow_json = (
                            workflow.workflow_json
                        )

                        nodes = workflow_json.get(
                            "nodes",
                            []
                        )

                        for node in nodes:

                            node_type = node.get(
                                "type"
                            )

                            service = node.get(
                                "service"
                            )

                            config = node.get(
                                "config",
                                {}
                            )

                            # ==========================================
                            # GMAIL ACTION NODE
                            # ==========================================

                            if (
                                node_type == "action"
                                and service == "gmail"
                            ):

                                recipient_email = config.get(
                                    "recipient_email"
                                )

                                if recipient_email:

                                    email_payload = {

                                        "email":
                                        recipient_email,

                                        "subject":
                                        "Workflow Executed Successfully 🚀",

                                        "body": f"""
                                        <h2>
                                        AI Automation Platform
                                        </h2>

                                        <p>
                                        Workflow
                                        <strong>
                                        {workflow.name}
                                        </strong>
                                        executed successfully.
                                        </p>

                                        <p>
                                        Queue orchestration completed.
                                        </p>
                                        """
                                    }

                                    gmail_result = await send_email(
                                        email_payload
                                    )

                                    print(
                                        "\n===== GMAIL RESULT ====="
                                    )

                                    print(gmail_result)

                    else:

                        print(
                            "Workflow not found"
                        )

                # ==========================================
                # TEMPLATE WORKFLOW EXECUTION
                # ==========================================

                elif job_type == "template":

                    template_name = job.get(
                        "template_name"
                    )

                    result = await WorkflowService.execute_template_workflow(
                        db=db,
                        template_name=template_name,
                        payload=payload,
                        workspace_id=workspace_id
                    )

                    print(EXECUTION_SUCCESS)

                    print(result)

            except Exception as e:

                print(EXECUTION_FAILED)

                traceback.print_exc()

            finally:

                db.close()

        await asyncio.sleep(1)