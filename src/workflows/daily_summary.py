from src.services.llm_service import OllamaService

class DailySummaryComposer:

    SYSTEM_PROMPT = """
You are a professional AI newsletter editor.

Create a concise daily GenAI digest from the following news items.

Rules:
- Group related items under clear section headings
Section headings MUST be bold 
- Use bullet points
- Be factual and neutral
- No hype, no emojis
- Keep it under 200 words
"""

    @classmethod
    def compose(cls, items: list[dict]) -> str:
        content = "\n".join(
            f"- {item['title']}" for item in items
        )

        prompt = f"""
{cls.SYSTEM_PROMPT}

News items:
{content}
"""

        return OllamaService.generate(prompt)
