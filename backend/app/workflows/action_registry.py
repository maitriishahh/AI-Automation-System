from app.integrations.gmail_service import send_email
from app.integrations.telegram_service import send_telegram_message
from app.integrations.webhook_service import trigger_webhook
from app.integrations.google_sheets_service import append_to_google_sheet


ACTION_REGISTRY = {
    "gmail":send_email,
    "telegram":send_telegram_message,
    "webhook":trigger_webhook,
    "google_sheets":append_to_google_sheet
}

def get_action(service_name: str):

    action = ACTION_REGISTRY.get(service_name)

    if not action:
        raise ValueError(f"No action found for service: {service_name}")

    return action