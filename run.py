from src.workflows.daily_summary import build_intelligence
from src.services.ingestion import IngestionService
from src.services.telegram_service import TelegramService
from src.services.email_service import EmailService
from src.services.pdf_report_service import PDFReportService
from src.tools.hackernews import HackerNewsAdapter
import asyncio

async def main():
    ingestion = IngestionService([HackerNewsAdapter()])
    await ingestion.run()

    news_items = ingestion.db.fetch_all()

    if not news_items:
        print("No news today.")
        return

    intelligence = build_intelligence(news_items)

    pdf_path = "intelligence_report.pdf"
    PDFReportService.generate(intelligence, pdf_path)

    telegram = TelegramService()
    await telegram.send(intelligence, pdf_path)

    email = EmailService()
    await email.send(intelligence, pdf_path)

    print("✅ Intelligence pipeline completed")

if __name__ == "__main__":
    asyncio.run(main())
