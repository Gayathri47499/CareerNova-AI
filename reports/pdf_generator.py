from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


class PDFGenerator:

    def generate_ats_report(

        self,

        ats,

        explanation,

        filename="ATS_Report.pdf"

    ):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(

            Paragraph(

                "<b>CareerNova AI</b>",

                styles["Title"]

            )

        )

        story.append(

            Paragraph(

                "ATS Intelligence Report",

                styles["Heading1"]

            )

        )

        story.append(

            Spacer(1,20)

        )

        story.append(

            Paragraph(

                f"<b>ATS Score:</b> {ats['score']}%",

                styles["BodyText"]

            )

        )

        story.append(

            Paragraph(

                f"<b>Match Percentage:</b> {ats['match_percentage']}%",

                styles["BodyText"]

            )

        )

        story.append(

            Spacer(1,15)

        )

        story.append(

            Paragraph(

                "<b>Matched Skills</b>",

                styles["Heading2"]

            )

        )

        for skill in ats["matched_skills"]:

            story.append(

                Paragraph(

                    f"• {skill}",

                    styles["BodyText"]

                )

            )

        story.append(

            Spacer(1,15)

        )

        story.append(

            Paragraph(

                "<b>Missing Skills</b>",

                styles["Heading2"]

            )

        )

        for skill in ats["missing_skills"]:

            story.append(

                Paragraph(

                    f"• {skill}",

                    styles["BodyText"]

                )

            )

        story.append(

            Spacer(1,15)

        )

        story.append(

            Paragraph(

                "<b>AI Recommendation</b>",

                styles["Heading2"]

            )

        )

        story.append(

            Paragraph(

                explanation,

                styles["BodyText"]

            )

        )

        doc.build(story)

        return filename