async def send_telegram_message(payload: dict):

    """
    Mock Telegram integration.
    """

    message = payload.get("message", "No message provided")

    print("\n===== TELEGRAM SERVICE =====")
    print(f"Sending Telegram message: {message}")

    return {
        "status": "success",
        "service": "telegram",
        "message": message
    }