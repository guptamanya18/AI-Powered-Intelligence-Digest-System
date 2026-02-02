from src.services.llm_service import OllamaLLMService
from src.agents.evaluator_agent import EvaluatorAgent

def run_evaluation(items, persona, topics, cursor):
    llm = OllamaLLMService(model="llama3")
    agent = EvaluatorAgent(llm, persona, topics)

    kept = 0

    for item in items:
        result = agent.evaluate(item)

        cursor.execute("""
        INSERT INTO evaluations (item_id, keep, relevance_score, reason)
        VALUES (?, ?, ?, ?)
        """, (
            item["id"],
            result["keep"],
            result["relevance_score"],
            result["reason"]
        ))

        if result["keep"]:
            kept += 1

    print(f"[INFO] LLM kept {kept}/{len(items)} items")
