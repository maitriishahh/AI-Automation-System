from collections import deque

execution_queue = deque()


def add_to_queue(job: dict):

    execution_queue.append(job)

    print(f"Job added to queue: {job}")


def get_next_job():

    if execution_queue:
        return execution_queue.popleft()

    return None


def get_queue_size():

    return len(execution_queue)