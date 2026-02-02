import asyncio
import os
from dotenv import load_dotenv
from src.utils.email_html import markdown_to_html


from src.services.ingestion import IngestionService
from src.tools.hackernews import HackerNewsAdapter
from src.services.database import Database
from src.workflows.daily_summary import DailySummaryComposer
from src.services.email_service import EmailService
from src.services.telegram_service import TelegramService
from src.services.scheduler_service import SchedulerService

load_dotenv()

async def run_digest(persona: str):
    print("[INFO] AI-Powered Intelligence Digest System Started")
    print(f"[INFO] Persona selected: {persona}")

    ingestion = IngestionService(
        adapters=[HackerNewsAdapter()]
    )
    await ingestion.run()

    db = Database()
    items = db.get_daily_items()

    if not items:
        print("[INFO] No items found for summary")
        return

    summary = DailySummaryComposer.compose(items)

    # EMAIL
    # EMAIL
    if os.getenv("ENABLE_EMAIL", "true").lower() == "true":
        html = markdown_to_html(summary)
        await EmailService().send(
            subject="Daily GenAI Digest",
            html_body=html
    )
    print("📩 Email sent")


    # TELEGRAM
    if os.getenv("ENABLE_TELEGRAM", "true").lower() == "true":
        await TelegramService().send(summary)

        print("📬 Telegram sent")


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python run.py [genai-news|scheduler]")
        return

    mode = sys.argv[1]

    if mode == "scheduler":
        SchedulerService().start(
            run_time=os.getenv("SCHEDULE_TIME", "09:20")
        )
    else:
        asyncio.run(run_digest(mode))


if __name__ == "__main__":
    main()
