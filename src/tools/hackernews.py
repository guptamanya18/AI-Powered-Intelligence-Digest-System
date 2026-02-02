import httpx
from bs4 import BeautifulSoup
from datetime import datetime
from src.tools.source_base import SourceAdapter

class HackerNewsAdapter(SourceAdapter):

    async def fetch_items(self, hours: int = 24) -> list[dict]:
        url = "https://news.ycombinator.com/"
        items = []

        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            rows = soup.select("tr.athing")

            for row in rows[:20]:  # limit for safety
                title_tag = row.select_one(".titleline a")
                if not title_tag:
                    continue

                title = title_tag.text.strip()
                link = title_tag["href"]

                items.append({
                    "source": "HackerNews",
                    "title": title,
                    "content": title,  # HN has no body
                    "url": link,
                    "published_at": datetime.utcnow().isoformat(),
                    "engagement": 0
                })

        return items
