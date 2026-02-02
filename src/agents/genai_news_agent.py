import json
from src.services.llm_service import OllamaService
from src.models.evaluation import EvaluationResult

class GenAINewsAgent:

    SYSTEM_PROMPT = """
You are an expert AI analyst.

Your task:
Evaluate whether the following news item is relevant to Generative AI.

Respond ONLY in valid JSON with this schema:
{
  "is_relevant": boolean,
  "relevance_score": number (0-10),
  "reason": string
}

Do not include any extra text.
"""

    @classmethod
    def evaluate(cls, title: str, topics: list[str]) -> EvaluationResult:
        prompt = f"""
{cls.SYSTEM_PROMPT}

User topics of interest: {topics}

News title:
"{title}"
"""

        raw_output = OllamaService.generate(prompt)

        try:
            parsed = json.loads(raw_output)
            return EvaluationResult(**parsed)
        except Exception as e:
            raise ValueError(f"Invalid LLM output: {raw_output}") from e
