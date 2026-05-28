LEAD_CAPTURE_TEMPLATE = {
    "name": "Lead Capture Workflow",
    "nodes": [
        {
            "id": "1",
            "type": "trigger",
            "service": "webhook"
        },
        {
            "id": "2",
            "type": "condition",
            "field": "lead_score",
            "operator": ">",
            "value": 50
        },
        {
            "id": "3",
            "type": "action",
            "service": "gmail"
        }
    ]
}


TELEGRAM_ALERT_TEMPLATE = {
    "name": "Telegram Alert Workflow",
    "nodes": [
        {
            "id": "1",
            "type": "trigger",
            "service": "webhook"
        },
        {
            "id": "2",
            "type": "action",
            "service": "telegram"
        }
    ]
}


TEMPLATE_REGISTRY = {
    "lead_capture": LEAD_CAPTURE_TEMPLATE,
    "telegram_alert": TELEGRAM_ALERT_TEMPLATE
}


def get_template(template_name: str):

    template = TEMPLATE_REGISTRY.get(template_name)

    if not template:
        raise ValueError(f"Template not found: {template_name}")

    return template