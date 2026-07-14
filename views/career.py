import streamlit as st

from agents.career_agent import CareerAgent


def show():

    st.title("🧠 Career Intelligence")

    st.write(
        "Generate your personalized AI career roadmap."
    )

    goal = st.text_input(
        "Your Dream Role",
        placeholder="Example: AI Engineer at Google"
    )

    if st.button(
        "🚀 Generate Career Report",
        use_container_width=True
    ):

        if "resume_profile" not in st.session_state:

            st.error(
                "Please upload your resume first."
            )

            return

        profile = st.session_state["resume_profile"]

        with st.spinner(
            "Analyzing your career..."
        ):

            report = CareerAgent().generate_career_report(
                profile,
                goal
            )

        st.success(
            "Career Report Generated!"
        )

        st.markdown(report)