import asyncio


async def schedule_workflow(
    workflow_func,
    interval_seconds=60
):

    while True:

        await workflow_func()

        await asyncio.sleep(interval_seconds)