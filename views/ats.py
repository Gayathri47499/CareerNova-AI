import streamlit as st

from resume.resume_service import ResumeService
from agents.ats_agent import ATSAgent
from components.ui.score_card import score_card
from components.ui.hero_score import hero_score
from components.ui.skill_group import skill_group
from components.ui.recommendation_card import recommendation_card
from components.ui.explanation_card import explanation_card
from repositories.ats_repository import ATSRepository
from components.ui.chart_card import ats_trend_chart
from reports.pdf_generator import PDFGenerator


def show():

    st.title("🎯 ATS Intelligence")

    st.write(
        "Analyze your resume against any job description."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    job_description = st.text_area(
        "Paste Job Description",
        height=250
    )

    if st.button(
        "🚀 Analyze ATS",
        use_container_width=True
    ):

        if uploaded_file is None:

            st.warning(
                "Please upload your resume."
            )

            return

        if job_description == "":

            st.warning(
                "Please enter the Job Description."
            )

            return

        st.info(
            "Analyzing Resume..."
        )

        with open(
            "sample_data/sample_resume.pdf",
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        service = ResumeService()

        resume = service.process_pdf(
            "sample_data/sample_resume.pdf"
        )

        agent = ATSAgent()

        result = agent.analyze(
            resume,
            job_description
        )

        st.success("Analysis Complete!")

        ats = result["ats"]
        repository = ATSRepository()

        repository.save_analysis(

    "AI Engineer",

    ats

)

        hero_score(ats["score"])

        st.divider()

        st.progress(
         ats["match_percentage"] / 100
)

        st.caption(
         f"Match Percentage : {ats['match_percentage']}%"
)

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

         skill_group(

        "🟢 Matched Skills",

        ats["matched_skills"],

        "#22C55E"

    )

        with col2:

         skill_group(

        "🔴 Missing Skills",

         ats["missing_skills"],

        "#EF4444"

    )

        st.divider()

        recommendation_card(

         result["explanation"]

)
        pdf = PDFGenerator()

        filename = pdf.generate_ats_report(

          ats,

          result["explanation"]

)

        with open(

          filename,

    "rb"

        ) as file:

         st.download_button(

        "📄 Download ATS Report",

        file,

        file_name=filename,

        mime="application/pdf",

        use_container_width=True

    )

        st.divider()

        explanation_card(

          "🧠 Why did I get this score?",

    [
          f"{len(ats['matched_skills'])} matching skills were found.",

          f"{len(ats['missing_skills'])} important skills are missing.",

          "Resume was successfully parsed.",

          "Job Description keywords were analyzed."
    ],

          success=True

)

        explanation_card(

         "🚀 Skill Gap Analysis",

          ats["missing_skills"],

          success=False

)
        st.divider()

        st.header("📈 ATS History")

        history = repository.get_history()

        if history:

           for item in history:

             st.info(

              f"""

🎯 {item['job']}

Score : {item['score']}%

Match : {item['match']}%

"""

        )

    else:

     st.write(

        "No history available."

    )
     st.divider()

     st.header("📈 ATS Trend")

     ats_trend_chart(history)

    if history:

     scores = [item["score"] for item in history]

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Average Score",

            f"{round(sum(scores)/len(scores))}%"

        )

    with col2:

        st.metric(

            "Highest",

            f"{max(scores)}%"

        )

    with col3:

        st.metric(

            "Lowest",

            f"{min(scores)}%"

        )

