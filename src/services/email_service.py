import os
from aiosmtplib import send
from email.message import EmailMessage
from dotenv import load_dotenv
from src.utils.email_html import build_email_html

load_dotenv()


class EmailService:

    async def send(self, intelligence: dict, pdf_path: str):
        msg = EmailMessage()

        msg["From"] = os.getenv("SMTP_USER")
        msg["To"] = os.getenv("EMAIL_TO")
        msg["Subject"] = f"AI Intelligence Digest — {intelligence['date']}"

        html_content = build_email_html(intelligence)
        msg.add_alternative(html_content, subtype="html")

        # Attach PDF
        with open(pdf_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="pdf",
                filename="AI_Intelligence_Report.pdf"
            )

        await send(
            msg,
            hostname=os.getenv("SMTP_HOST"),
            port=int(os.getenv("SMTP_PORT")),
            username=os.getenv("SMTP_USER"),
            password=os.getenv("SMTP_PASS"),
            start_tls=True
        )
