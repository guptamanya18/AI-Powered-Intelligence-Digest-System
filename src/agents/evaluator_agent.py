import json

class EvaluatorAgent:
    def __init__(self, llm_service, persona, topics):
        self.llm = llm_service
        self.persona = persona
        self.topics = topics

    def build_prompt(self, item):
        return f"""
You are an expert AI analyst writing a daily intelligence digest.

Persona: {self.persona}
Focus Topics: {", ".join(self.topics)}

Evaluate the following news item.

Title: {item['title']}
URL: {item['url']}

Respond ONLY in valid JSON with the following schema:

{{
  "keep": true | false,
  "relevance_score": 0-100,
  "reason": "short explanation"
}}
"""

    def evaluate(self, item):
        prompt = self.build_prompt(item)
        raw_response = self.llm.generate(prompt)

        try:
            return json.loads(raw_response)
        except json.JSONDecodeError:
            return {
                "keep": False,
                "relevance_score": 0,
                "reason": "Invalid LLM output"
            }
