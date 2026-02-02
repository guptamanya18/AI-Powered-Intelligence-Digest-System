import aiosmtplib
from email.message import EmailMessage
import os

class EmailService:

    async def send(self, subject: str, html_body: str):
        msg = EmailMessage()
        msg["From"] = os.getenv("SMTP_USER")
        msg["To"] = os.getenv("EMAIL_TO")
        msg["Subject"] = subject

        # Plain-text fallback (optional but good practice)
        msg.set_content("Your email client does not support HTML.")

        # HTML content
        msg.add_alternative(html_body, subtype="html")

        await aiosmtplib.send(
            msg,
            hostname=os.getenv("SMTP_HOST"),
            port=int(os.getenv("SMTP_PORT")),
            username=os.getenv("SMTP_USER"),
            password=os.getenv("SMTP_PASS"),
            start_tls=True
        )
