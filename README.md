# 🧠 AI-Powered Intelligence Digest System

An automated AI-driven system that ingests daily GenAI-related news, summarizes it using a Large Language Model (LLM), and delivers a clean, professional intelligence digest via **Email** and **Telegram**.

---

## 📌 Overview

The **AI-Powered Intelligence Digest System** continuously collects artificial intelligence and generative AI news from reliable sources, filters relevant items, and produces a concise, well-structured daily summary.

The system is designed with a strong focus on:
- Professional output quality  
- Modular architecture  
- Asynchronous execution  
- Real-world production readiness  

---

## 🏗️ Project Structure

AI-Powered Intelligence Digest System/
│
├── run.py
├── .env
├── requirements.txt
│
├── src/
│ ├── services/
│ │ ├── ingestion.py
│ │ ├── database.py
│ │ ├── email_service.py
│ │ ├── telegram_service.py
│ │ ├── scheduler_service.py
│ │ └── llm_service.py
│ │
│ ├── tools/
│ │ └── hackernews.py
│ │
│ └── workflows/
│ └── daily_summary.py
│
└── README.md

## ✨ Key Features

- 🔄 **Automated News Ingestion**
  - Fetches AI and GenAI news from Hacker News
  - Filters and stores only relevant items

- 🧠 **LLM-Based Summarization**
  - Uses Ollama to generate neutral, factual summaries
  - Automatically groups related news into sections
  - Keeps content concise and readable

- 📩 **Email Delivery**
  - Sends a professionally formatted daily digest
  - Clear headings and bullet points for easy scanning

- 📬 **Telegram Notifications**
  - Delivers structured summaries via Telegram
  - Clean, readable formatting suitable for daily consumption

- ⏰ **Scheduler Support**
  - Supports scheduled daily execution
  - Manual and automated modes available

---


---

## ⚙️ Tech Stack

- Python 3.11+
- Asyncio
- SQLite
- Ollama (LLM)
- aiosmtplib (Email service)
- python-telegram-bot
- python-dotenv

---



