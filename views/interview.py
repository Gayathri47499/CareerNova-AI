import streamlit as st

from interview.interview_service import InterviewService
from components.ui.interview_score import interview_score
from components.ui.skill_progress import skill_progress


def show():

    st.title("🎤 AI Interview Center")

    service = InterviewService()

    # -------------------------
    # Session State
    # -------------------------

    if "questions" not in st.session_state:
        st.session_state.questions = []

    if "current_question" not in st.session_state:
        st.session_state.current_question = 0

    if "reports" not in st.session_state:
        st.session_state.reports = []

    # -------------------------
    # Interview Options
    # -------------------------

    company = st.selectbox(
        "Company",
        [
            "Google",
            "Microsoft",
            "Amazon",
            "OpenAI",
            "Meta"
        ]
    )

    role = st.selectbox(
        "Role",
        [
            "AI Engineer",
            "Machine Learning Engineer",
            "Data Scientist"
        ]
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    # -------------------------
    # Start Interview
    # -------------------------

    if st.button(
        "🚀 Start Interview",
        use_container_width=True
    ):

        st.session_state.questions = service.generate_questions(
            company,
            role,
            difficulty
        )

        st.session_state.current_question = 0
        st.session_state.reports = []

    # -------------------------
    # Interview Running
    # -------------------------

    if st.session_state.questions:

        total = len(st.session_state.questions)
        current = st.session_state.current_question

        if current < total:

            st.progress((current + 1) / total)

            question = st.session_state.questions[current]

            st.subheader(
                f"Question {current + 1} of {total}"
            )

            st.info(question)

            answer = st.text_area(
                "Your Answer",
                key=f"answer_{current}"
            )

            if st.button(
                "Evaluate",
                key=f"eval_{current}"
            ):

                report = service.evaluate(
                    question,
                    answer
                )

                st.session_state.reports.append(report)

                st.success("Answer Evaluated")

                st.markdown(report)

            if st.button(
                "Next Question",
                key=f"next_{current}"
            ):

                st.session_state.current_question += 1
                st.rerun()

        # -------------------------
        # Interview Completed
        # -------------------------

        else:

            st.success("🎉 Interview Completed!")

            interview_score(86)

            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                skill_progress("Technical", 82)
                skill_progress("Problem Solving", 79)

            with col2:
                skill_progress("Communication", 91)
                skill_progress("Confidence", 88)

            st.divider()

            st.subheader("📋 AI Feedback")

            for i, report in enumerate(
                st.session_state.reports,
                start=1
            ):

                with st.expander(
                    f"Question {i}"
                ):

                    st.markdown(report)