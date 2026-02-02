import httpx

OLLAMA_EMBED_URL = "http://localhost:11434/api/embeddings"
MODEL_NAME = "llama3:8b-instruct-q4_K_M"

class EmbeddingService:

    @staticmethod
    def embed(text: str) -> list[float]:
        payload = {
            "model": MODEL_NAME,
            "prompt": text
        }

        response = httpx.post(OLLAMA_EMBED_URL, json=payload)
        response.raise_for_status()

        return response.json()["embedding"]
