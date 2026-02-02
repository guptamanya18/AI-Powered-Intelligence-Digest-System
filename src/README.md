🤖 AI-Powered Intelligence Digest System
📌 Overview

The AI-Powered Intelligence Digest System is a fully local, automated GenAI news pipeline that ingests AI-related content, filters relevant insights, stores them persistently, and delivers a curated daily digest via Email and Telegram.

The system is designed with a privacy-first, modular, and scalable architecture, demonstrating real-world automation, scheduling, and notification delivery.

✨ Key Features

🔍 Automated GenAI news ingestion (HackerNews)

🧠 Topic-based intelligent filtering

🗃️ Persistent storage using SQLite

📧 Email delivery via Gmail SMTP

🤖 Telegram Bot notifications

⏰ Daily scheduler with time-based execution

🔐 Lock mechanism to prevent duplicate runs

⚠️ Fault-tolerant job execution

🏗️ System Architecture
Adapters ──▶ Ingestion ──▶ Database ──▶ Notification Services
                          │
                          ▼
                      Scheduler

📁 Project Structure
AI-Powered-Intelligence-Digest-System/
│
├── src/
│   ├── adapters/
│   │   └── hackernews_adapter.py
│   │
│   ├── services/
│   │   ├── ingestion.py
│   │   ├── database.py
│   │   ├── email_service.py
│   │   ├── telegram_service.py
│   │   └── scheduler_service.py
│   │
│   └── config/
│
├── data/
│   ├── digest.db
│   └── run.lock
│
├── run.py
├── .env
├── requirements.txt
└── README.md

⚙️ Tech Stack

Python 3.13

AsyncIO

SQLite

schedule

Telegram Bot API

SMTP (Gmail App Password)

🔐 Environment Configuration

Create a .env file in the root directory:

# Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_16_char_app_password
EMAIL_TO=receiver_email@gmail.com

# Telegram Configuration
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id

# Scheduler
SCHEDULE_TIME=11:00


⚠️ Never use your normal Gmail password. Always use a Gmail App Password.

▶️ How to Run
1️⃣ Manual Execution

Runs the full ingestion → filtering → storage pipeline.

python run.py genai-news

2️⃣ Start Scheduler

Runs the system automatically once per day at the configured time.

python run.py scheduler

⏱️ Scheduler Behavior

Executes daily at SCHEDULE_TIME

Uses a run.lock file to prevent overlapping executions

Requires the system to be powered on

Stops if the terminal or system is closed

📬 Notification Delivery

📧 Email is delivered via Gmail SMTP

🤖 Telegram bot sends real-time messages

Delivery channels can be toggled via .env

⚠️ Known Limitations

Runs only on local system

Scheduler halts when system is shut down

SQLite allows only one write operation at a time

No cloud persistence (by design)

🚀 Future Enhancements

Cloud deployment (AWS / GCP)

Docker containerization

Web-based dashboard

Multi-source ingestion (Reddit, ArXiv, Blogs)

AI-based summarization using LLMs

🎥 Demo

📎 Demo Video: (Add link here)

🏆 What This Project Demonstrates

Real-world automation

Asynchronous programming

Modular system design

Secure credential handling

Scheduler-based workflows

Production-style logging and fault handling

👤 Author

Manya Gupta