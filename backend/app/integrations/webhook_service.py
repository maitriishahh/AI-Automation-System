async def trigger_webhook(payload: dict):

    """
    Mock webhook trigger.
    """

    print("\n===== WEBHOOK TRIGGER =====")
    print("Received payload:", payload)

    return {
        "status": "success",
        "service": "webhook",
        "payload": payload
    }