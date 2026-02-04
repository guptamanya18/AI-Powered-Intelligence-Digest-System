from reportlab.lib.pagesizes import A4

from reportlab.lib.units import inch
import matplotlib.pyplot as plt
import tempfile

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4



class PDFReportService:

    @staticmethod
    def _generate_trend_chart(sections: list) -> str:
        """
        Generates a bar chart image for section impact scores
        """
        titles = [s["title"] for s in sections]
        scores = [s.get("impact_score", 5) for s in sections]

        plt.figure(figsize=(6, 4))
        plt.barh(titles, scores)
        plt.xlabel("Impact Score (0–10)")
        plt.title("AI Trend Impact Snapshot")
        plt.xlim(0, 10)

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        plt.tight_layout()
        plt.savefig(temp_file.name)
        plt.close()

        return temp_file.name

    @staticmethod
    def generate(intelligence: dict, output_path: str):
        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=36,
            leftMargin=36,
            topMargin=36,
            bottomMargin=36
        )

        styles = getSampleStyleSheet()

        styles.add(ParagraphStyle(
            name="Heading",
            fontSize=14,
            spaceAfter=10,
            spaceBefore=12,
            leading=18,
            bold=True
        ))

        styles.add(ParagraphStyle(
            name="Body",
            fontSize=10,
            leading=14,
            spaceAfter=8
        ))

        styles.add(ParagraphStyle(
            name="Link",
            fontSize=9,
            textColor="blue",
            spaceAfter=12
        ))

        story = []

        # -------- Title --------
        story.append(Paragraph("AI Intelligence Daily Digest", styles["Title"]))
        story.append(Spacer(1, 12))

    # -------- Executive Summary --------
        story.append(Paragraph("Executive Summary", styles["Heading"]))
        story.append(Paragraph(intelligence["executive_summary"], styles["Body"]))

        # -------- Sections --------
        for section in intelligence["sections"]:
            story.append(Spacer(1, 14))
            story.append(Paragraph(section["title"], styles["Heading"]))

            for item in section["items"]:
                story.append(Paragraph(f"<b>{item['headline']}</b>", styles["Body"]))
                story.append(Paragraph(item["summary"], styles["Body"]))

                # ✅ SAFE LINK CHECK
                url = item.get("url", "").strip()
                if url.startswith("http"):
                    story.append(
                        Paragraph(
                            f'<link href="{url}">Read source</link>',
                            styles["Link"]
                        )
                    )

        doc.build(story)