🧠 AI-Powered Intelligence Digest System
An automated AI-driven system that ingests daily GenAI-related news, summarizes it using a Large Language Model (LLM), and delivers a clean, professional intelligence digest via Email and Telegram.

📌 Overview
The AI-Powered Intelligence Digest System continuously collects artificial intelligence and generative AI news from reliable sources, filters relevant items, and produces a concise, well-structured daily summary.

The system is designed with a strong focus on:

Professional output quality
Modular architecture
Asynchronous execution
Real-world production readiness

🏗️ Project Structure

AI-Powered Intelligence Digest System/
│
├── run.py
├── .env
├── requirements.txt
│
├── src/
│ ├── services/
│ │ ├── config.py
│ │ ├── database.py
│ │ ├── email_service.py
│ │ ├── embedding_service.py
│ │ ├── filtering.py
│ │ ├── ingestion.py
│ │ ├── vector_store.py
│ │ ├── telegram_service.py
│ │ ├── scheduler_service.py
│ │ └── llm_service.py
|
│ ├── agents/
│ │ ├── evaluator_agent.py
│ │ ├── genai_news_agent.py
│ │ ├── reflection_agent.py
│ │ └── telegram_service.py

│ ├── models/
│ │ ├── evaluation.py
│ │ └── schema.py

│ ├── tools/
│ │ ├── email_html.py
│ │ └── loggers.py

│ ├── utils/
│ │ ├── source_base.py
│ │ └── hackernews.py
│ │
│ ├── workflows/
│ | ├── daily_summary.py
│ │ └── digest_workflow.py
│
└── README.md

✨ Key Features
🔄 Automated News Ingestion

Fetches AI and GenAI news from Hacker News
Filters and stores only relevant items
🧠 LLM-Based Summarization

Uses Ollama to generate neutral, factual summaries
Automatically groups related news into sections
Keeps content concise and readable
📩 Email Delivery

Sends a professionally formatted daily digest
Clear headings and bullet points for easy scanning
📬 Telegram Notifications

Delivers structured summaries via Telegram
Clean, readable formatting suitable for daily consumption
⏰ Scheduler Support

Supports scheduled daily execution
Manual and automated modes available
⚙️ Tech Stack
Python 3.11+
Asyncio
SQLite
Ollama (LLM)
aiosmtplib (Email service)
python-telegram-bot
python-dotenv
🚀 Installation
1️⃣ Clone the Repository git clone cd AI-Powered-Intelligence-Digest-System

2️⃣ Create and Activate Virtual Environment python -m venv venv venv\Scripts\activate

3️⃣ Install Dependencies pip install -r requirements.txt 🔐 Environment Variables Create a .env file in the project root:

Email Configuration
SMTP_HOST=smtp.gmail.com SMTP_PORT=587 SMTP_USER=your_email@gmail.com SMTP_PASS=your_app_password EMAIL_TO=recipient_email@gmail.com

Telegram Configuration
TELEGRAM_BOT_TOKEN=your_bot_token TELEGRAM_CHAT_ID=your_chat_id

Scheduler
SCHEDULE_TIME=09:20

Feature Toggles
ENABLE_EMAIL=true ENABLE_TELEGRAM=true

▶️ Running the Application Run Once (Manual Mode) python run.py genai-news

Run with Scheduler python run.py scheduler

🧠 Summarization Logic Neutral and factual tone

Grouped news sections

Bullet-point formatting

No hype, emojis, or promotional language

Designed for professional audiences

📬 Output Channels Email Clear subject line

Section-based layout

Bullet-point summaries

Telegram Compact, readable formatting

Bold section titles

Optimized for daily reading

🔄 Extensibility This system can be easily extended to:

Add new news sources or APIs

Support additional delivery channels (Slack, Discord)

Replace or upgrade the LLM

Store historical summaries

Add analytics or sentiment analysis

🛡️ Reliability Fully asynchronous execution

Graceful handling of empty or duplicate data

Robust error handling and logging

Safe retry mechanisms for external services

👩‍💻 Author Manya Gupta AI / ML Engineering Student Focused on building real-world AI systems that integrate automation, LLMs, and production-grade delivery pipelines.

📄 License This project is intended for educational and personal use. Commercial usage should comply with all third-party service terms and licenses.
