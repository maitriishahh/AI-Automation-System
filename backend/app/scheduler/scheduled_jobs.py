from app.scheduler.scheduler import (
    scheduler
)

from app.queue.queue_manager import (
    add_to_queue
)


def schedule_workflow_job(
    workflow_id,
    workspace_id
):

    add_to_queue({

        "type": "database",

        "workflow_id": workflow_id,

        "payload": {
            "to_email": "maitridj01@gmail.com",

            "subject": "Scheduled Workflow Test",

            "body": "APScheduler working successfully"},

        "workspace_id": workspace_id
    })

    print(
        f"Scheduled workflow added to queue: {workflow_id}"
    )


scheduler.add_job(

    schedule_workflow_job,

    trigger="cron",

    hour=9,
    minute=0,
    args=[5, 5]
)