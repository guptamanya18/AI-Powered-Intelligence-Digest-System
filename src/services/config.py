import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Personas
    GENAI_NEWS_ENABLED = os.getenv("PERSONA_GENAI_NEWS_ENABLED", "false").lower() == "true"
    PRODUCT_IDEAS_ENABLED = os.getenv("PERSONA_PRODUCT_IDEAS_ENABLED", "false").lower() == "true"

    # Topics
    TOPICS = [t.strip() for t in os.getenv("TOPICS", "").split(",") if t.strip()]

    # LLM
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

    # Delivery
    EMAIL_ENABLED = os.getenv("EMAIL_ENABLED", "false").lower() == "true"
    TELEGRAM_ENABLED = os.getenv("TELEGRAM_ENABLED", "false").lower() == "true"

    KEYWORDS = [k.strip() for k in os.getenv("KEYWORDS", "").split(",") if k.strip()]

