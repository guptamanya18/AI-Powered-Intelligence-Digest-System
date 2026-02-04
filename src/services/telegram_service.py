from telegram import Bot
import os
from dotenv import load_dotenv

load_dotenv()

def chunk_text(text: str, limit: int = 3800):
    chunks = []
    while len(text) > limit:
        split_at = text.rfind("\n", 0, limit)
        if split_at == -1:
            split_at = limit
        chunks.append(text[:split_at])
        text = text[split_at:]
    chunks.append(text)
    return chunks


def render_bar(score: int, max_score: int = 10) -> str:
    return "█" * score + "░" * (max_score - score) + f" {score}/{max_score}"


def format_telegram_message(intelligence: dict) -> str:
    lines = []

    lines.append(f"🧠 Daily AI Intelligence — {intelligence['date']}")
    lines.append("")
    lines.append("📊 Trends")

    for section in intelligence["sections"]:
        lines.append(
            f"{section['title']}: "
            f"{'█' * section['impact_score']}{'░' * (10 - section['impact_score'])} "
            f"{section['impact_score']}/10"
        )

    lines.append("")
    lines.append("📰 Key Developments")

    for section in intelligence["sections"]:
        lines.append("")
        lines.append(section["title"])

        for item in section["items"]:
            lines.append(f"🔹 {item['headline']}")
            lines.append(item["summary"])          # ✅ PARAGRAPH
            lines.append(f"🔗 {item['url']}")      # ✅ WORKING LINK
            lines.append("")

    lines.append("📎 Full Intelligence PDF attached")

    return "\n".join(lines)



class TelegramService:
    def __init__(self):
        self.bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")

    async def send(self, intelligence: dict, pdf_path: str | None = None):
        message = format_telegram_message(intelligence)

        # 1️⃣ Send text message in chunks
        for chunk in chunk_text(message):
            await self.bot.send_message(
                chat_id=self.chat_id,
                text=chunk
            )

        # 2️⃣ Send PDF if available (ONCE, not per chunk)
        if pdf_path and os.path.exists(pdf_path):
            with open(pdf_path, "rb") as pdf_file:
                await self.bot.send_document(
                    chat_id=self.chat_id,
                    document=pdf_file,
                    caption="📎 Full AI Intelligence Report (PDF)"
                )
