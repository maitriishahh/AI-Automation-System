import asyncio
import traceback
from app.queue.queue_manager import (
    get_next_job
)

from app.db.session import SessionLocal

from app.services.workflow_service import (
    WorkflowService
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

                print(f"Executing job: {job}")

                job_type = job.get("type")

                payload = job.get("payload")

                workspace_id = job.get(
                    "workspace_id"
                )


                if job_type == "database":

                    workflow_id = job.get(
                        "workflow_id"
                    )

                    result = await WorkflowService.execute_db_workflow(
                        db=db,
                        workflow_id=workflow_id,
                        payload=payload,
                        workspace_id=workspace_id
                    )

                    print(EXECUTION_SUCCESS)

                    print(result)


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