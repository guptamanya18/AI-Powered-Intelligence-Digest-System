def format_telegram_message(intelligence: dict) -> str:
    lines = []

    lines.append(f"🧠 Daily AI Intelligence — {intelligence['date']}")
    lines.append("")

    lines.append("📊 Trends")
    for topic, score in intelligence.get("trends", {}).items():
        lines.append(f"{topic}: {'█' * score} {score}/10")

    lines.append("")
    lines.append("📰 News Highlights")

    for section in intelligence["sections"]:
        lines.append(f"\n🔷 {section['title']}")
        for item in section["items"]:
            lines.append(f"🔹 {item['headline']}")
            lines.append(f"   {item['summary']}")
            lines.append(f"   🔗 {item['url']}")

    lines.append("\n📎 Full PDF report attached")

    return "\n".join(lines)
