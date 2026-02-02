import json
from src.services.llm_service import OllamaService

class ReflectionAgent:

    SYSTEM_PROMPT = """
You are a strict AI reviewer.

You are given:
- A news title
- An evaluation decision
- A relevance score
- A reason

Your task:
Check if the decision and score are reasonable.

Respond ONLY in valid JSON:
{
  "approved": boolean,
  "adjusted_score": number (0-10),
  "feedback": string
}
"""

    @classmethod
    def review(cls, title: str, evaluation: dict):
        prompt = f"""
{cls.SYSTEM_PROMPT}

News title:
"{title}"

Evaluation:
{json.dumps(evaluation, indent=2)}
"""

        raw = OllamaService.generate(prompt)

        try:
            return json.loads(raw)
        except Exception:
            raise ValueError("Reflection agent returned invalid JSON")
