import re

def markdown_to_html(text: str) -> str:
    # Convert **Heading** to <b>Heading</b>
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)

    # Convert bullet dots to HTML bullets
    lines = text.splitlines()
    html_lines = []

    for line in lines:
        if line.strip().startswith("•"):
            html_lines.append(f"<li>{line.replace('•', '').strip()}</li>")
        else:
            html_lines.append(f"<p>{line}</p>")

    return "<html><body>" + "".join(html_lines) + "</body></html>"
