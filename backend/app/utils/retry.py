import asyncio

from app.workflows.constants import (
    DEFAULT_RETRY_COUNT,
    DEFAULT_RETRY_DELAY
)


async def retry_handler(
    func,
    payload,
    retries=DEFAULT_RETRY_COUNT,
    delay=DEFAULT_RETRY_DELAY
):

    last_exception = None

    for attempt in range(retries):

        try:

            print(
                f"Execution attempt {attempt + 1}"
            )

            result = await func(payload)

            return result

        except Exception as e:

            last_exception = e

            retry_delay = delay * (attempt + 1)

            print(
                f"Retry attempt {attempt + 1} failed"
            )

            print(f"Error: {str(e)}")

            print(
                f"Retrying in {retry_delay} seconds..."
            )

            await asyncio.sleep(retry_delay)

    print("Max retries exceeded")

    raise last_exception