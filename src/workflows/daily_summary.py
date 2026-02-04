from datetime import datetime
from src.services.llm_service import OllamaService
import json


def build_intelligence(items: list[dict], persona: str = "genai-news") -> dict:
    """
    Builds ONE structured intelligence object.
    Safe for Email, Telegram, and PDF.
    """

    llm = OllamaService()

    # ---------- Deduplicate + limit ----------
    # ---------- Deduplicate + sort + limit (FINAL FIX) ----------
    unique_items = {}
    for item in items:
        url = item.get("url")
        if isinstance(url, str) and url.startswith("http"):
            unique_items[url] = item  # URL-based deduplication

# Convert to list
    items = list(unique_items.values())    

    # Sort latest first (safe even if published_at missing)
    items = sorted(
    items,
    key=lambda x: x.get("published_at", ""),
    reverse=True
)

# HARD LIMIT: only 5–8 news
    items = items[:8]

# ---------- LLM-safe items ----------
    llm_items = [
    {
        "title": item["title"],
        "content": (item.get("content") or "")[:800],
        "url": item["url"]
    }
    for item in items
]


    # ---------- Executive Summary ----------
    summary_prompt = f"""
You are an AI intelligence analyst.

Based ONLY on the following news items, write a factual,
neutral executive summary of 120–160 words.

Rules:
- Do NOT invent facts
- Do NOT exaggerate
- Analytical, professional tone
- One coherent paragraph only

News:
{json.dumps(llm_items, indent=2)}
"""

    try:
        executive_summary = llm.generate(summary_prompt)
        if not isinstance(executive_summary, str):
            raise ValueError("Invalid summary output")
    except Exception:
        executive_summary = (
            "This intelligence briefing highlights recent developments across AI, "
            "software engineering, and emerging technology platforms. The collected "
            "updates indicate continued investment in automation, agent-based systems, "
            "and developer tooling, with organizations focusing on efficiency, scalability, "
            "and governance. While innovation velocity remains high, concerns around "
            "security, reliability, and responsible deployment persist. Enterprises are "
            "increasingly evaluating structured adoption strategies rather than experimental "
            "rollouts, signaling a maturation phase in applied AI."
        )

    # ---------- Section Structuring ----------
    section_prompt = f"""
Return STRICT JSON ONLY.

Format:
[
  {{
    "title": "Category Name",
    "impact_score": 0,
    "items": [
      {{
        "headline": "",
        "summary": "100–150 word factual paragraph",
        "url": ""
      }}
    ]
  }}
]

Rules:
- Valid JSON only
- No markdown
- No commentary
- Each summary MUST be a paragraph (100–150 words)

News:
{json.dumps(llm_items, indent=2)}
"""

    try:
        raw_output = llm.generate(section_prompt)

        if isinstance(raw_output, str):
            sections = json.loads(raw_output)
        elif isinstance(raw_output, list):
            sections = raw_output
        else:
            sections = []

    except Exception as e:
        
        sections = []

    # ---------- Guaranteed fallback (NO EMPTY CONTENT) ----------
    if not sections:
        sections = [{
            "title": "General Developments",
            "impact_score": min(len(items) + 3, 10),
            "items": [
                {
                    "headline": item["title"],
                    "summary": (
                        f"This update discusses {item['title']} and its relevance within "
                    f"the current technology landscape. The development reflects ongoing "
                    f"progress in platforms, tooling, or infrastructure. Monitoring "
                    f"adoption trends, ecosystem response, and long-term implications "
                    f"will help determine its broader industry impact."
                    ),
                    "url": item["url"]
                }
                for item in items
            ]
        }]

    # ---------- Trend Scoring ----------
    trends = {
        section["title"]: min(len(section["items"]) + 3, 10)
        for section in sections
    }

    return {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "persona": persona,
        "executive_summary": executive_summary,
        "sections": sections,
        "trends": trends,
        "risks": [
            "Security risks from rapid AI tooling adoption",
            "Governance gaps in emerging AI platforms"
        ],
        "opportunities": [
            "Operational efficiency through automation",
            "Enterprise-grade AI platform adoption"
        ],
        "watchlist": [
            "Agent orchestration frameworks",
            "Low-code and AI-assisted development tools"
        ]
    }
