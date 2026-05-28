import requests

from app.core.config import settings


async def send_telegram_message(payload: dict):

    """
    Real Telegram Bot integration.
    Sends actual Telegram messages.
    """

    try:

        message = payload.get(
            "message",
            "Workflow executed successfully 🚀"
        )

        url = (
            f"https://api.telegram.org/bot"
            f"{settings.TELEGRAM_BOT_TOKEN}"
            f"/sendMessage"
        )

        data = {
            "chat_id": settings.TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }

        response = requests.post(
            url,
            json=data
        )

        response_data = response.json()

        if not response_data.get("ok"):

            raise Exception(
                response_data
            )

        print("\n===== TELEGRAM SERVICE =====")
        print("Telegram message sent")

        return {
            "status": "success",
            "service": "telegram",
            "response": response_data
        }

    except Exception as e:

        print("\n===== TELEGRAM ERROR =====")
        print(str(e))

        raise Exception(
            f"Telegram Failed: {str(e)}"
        )