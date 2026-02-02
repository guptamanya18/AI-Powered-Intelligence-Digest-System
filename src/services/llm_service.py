import httpx
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:8b-instruct-q4_K_M"

class OllamaService:
    @staticmethod
    def generate(prompt: str) -> str:
        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }

        response = httpx.post(OLLAMA_URL, json=payload, timeout=120)
        response.raise_for_status()

        return response.json()["response"]
