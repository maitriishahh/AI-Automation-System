from fastapi import APIRouter

from app.integrations.gmail_service import send_email
from app.integrations.telegram_service import (
    send_telegram_message
)
from app.integrations.google_sheets_service import append_to_google_sheet

router = APIRouter()


@router.get("/test-email")
async def test_email():

    payload = {
        "email": "maitridj01@gmail.com",
        "subject": "AI Automation Platform Test",
        "body": """
        <h1>Email Working Successfully 🚀</h1>
        <p>Real Gmail integration connected.</p>
        """
    }

    result = await send_email(payload)

    return result

@router.get("/test-telegram")
async def test_telegram():

    payload = {
        "message": """
🚀 AI Automation Platform

Telegram integration working successfully.
"""
    }

    result = await send_telegram_message(payload)

    return result

@router.get("/test-sheets")
async def test_sheets():

    data = [
        "Workflow Test",
        "Google Sheets Connected",
        "Success 🚀"
    ]

    result = await append_to_google_sheet(data)

    return result