import httpx
from bs4 import BeautifulSoup
from datetime import datetime
from src.tools.source_base import SourceAdapter

class HackerNewsAdapter(SourceAdapter):

    async def fetch_items(self, hours: int = 24) -> list[dict]:
        url = "https://news.ycombinator.com/newest"
        items = []

        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            rows = soup.select("tr.athing")

            for row in rows[:20]:
                title_tag = row.select_one(".titleline a")
                if not title_tag:
                    continue

                title = title_tag.text.strip()
                link = title_tag["href"]

                # Normalize HN relative URLs
                link = (
                    link
                    if link.startswith("http")
                    else f"https://news.ycombinator.com/{link}"
                )

                article_text = ""

                # Fetch article body if external link
                if link.startswith("http"):
                    try:
                        article_resp = await client.get(link, timeout=8)
                        article_soup = BeautifulSoup(article_resp.text, "html.parser")
                        paragraphs = article_soup.find_all("p")

                        article_text = " ".join(
                            p.get_text(strip=True) for p in paragraphs[:6]
                        )
                    except Exception:
                        article_text = ""

                items.append({
                    "source": "HackerNews",
                    "title": title,
                    "content": article_text,   # ✅ REAL CONTENT
                    "url": link,
                    "published_at": datetime.utcnow().isoformat(),
                    "engagement": 0
                })

        return items
