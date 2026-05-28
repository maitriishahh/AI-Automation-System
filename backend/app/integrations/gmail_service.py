import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.core.config import settings


async def send_email(payload: dict):

    """
    Real Gmail SMTP integration.
    Sends actual emails.
    """

    try:

        recipient = (payload.get("to_email") or
         payload.get("email"))
        subject = payload.get(
            "subject",
            "Workflow Notification"
        )

        body = payload.get(
            "body",
            "Workflow executed successfully"
        )

        if not recipient:
            raise Exception(
                "Recipient email missing"
            )

        message = MIMEMultipart()

        message["From"] = settings.EMAIL_ADDRESS
        message["To"] = recipient
        message["Subject"] = subject

        message.attach(
            MIMEText(body, "html")
        )

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        server.login(
            settings.EMAIL_ADDRESS,
            settings.EMAIL_PASSWORD
        )

        server.sendmail(
            settings.EMAIL_ADDRESS,
            recipient,
            message.as_string()
        )

        server.quit()

        print("\n===== GMAIL SERVICE =====")
        print(f"Email sent to: {recipient}")

        return {
            "status": "success",
            "service": "gmail",
            "recipient": recipient,
            "message": "Email sent successfully"
        }

    except Exception as e:

        print("\n===== GMAIL ERROR =====")
        print(str(e))

        raise Exception(
            f"Gmail Failed: {str(e)}"
        )