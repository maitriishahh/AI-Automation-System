async def send_email(payload: dict):

    """
    Mock Gmail integration.
    Later this will use real Gmail APIs.
    """
    try:

        recipient = payload.get("email")

        print("\n===== GMAIL SERVICE =====")
        print(f"Sending email to: {recipient}")
        print("Payload:", payload)

        return {
            "status": "success",
            "service": "gmail",
            "recipient": recipient
        }

    except Exception as e:

        raise Exception("Gmail Failed")