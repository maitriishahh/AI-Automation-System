import asyncio


async def retry_handler(
    func,
    payload,
    retries=3,
    delay=1
):

    last_exception = None

    for attempt in range(retries):

        try:

            return await func(payload)

        except Exception as e:

            last_exception = e

            print(f"Retry attempt {attempt+1}")

            await asyncio.sleep(delay)

    raise last_exception