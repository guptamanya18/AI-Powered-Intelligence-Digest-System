from telegram import Bot
import os
from dotenv import load_dotenv

load_dotenv()

class TelegramService:
    def __init__(self):
        self.bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")

    async def send(self, message: str):
        await self.bot.send_message(
            chat_id=self.chat_id,
            text=message,
            parse_mode="Markdown"
        )
