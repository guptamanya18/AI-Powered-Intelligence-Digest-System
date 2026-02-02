from datetime import datetime, timedelta
from src.services.config import Config

class PreFilterService:

    def __init__(self):
        self.keywords = [k.lower() for k in Config.KEYWORDS]

    def is_relevant(self, item: dict) -> bool:
        text = f"{item['title']} {item['content']}".lower()
        return any(keyword in text for keyword in self.keywords)

    def within_time_window(self, item: dict, hours: int = 24) -> bool:
        published = datetime.fromisoformat(item["published_at"])
        return published >= datetime.utcnow() - timedelta(hours=hours)

    def apply(self, items: list[dict]) -> list[dict]:
        filtered = []

        for item in items:
            if not self.is_relevant(item):
                continue
            if not self.within_time_window(item):
                continue

            filtered.append(item)

        return filtered
