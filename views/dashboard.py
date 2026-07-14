import streamlit as st

from components.welcome_banner import show_banner
from components.ui.stat_card import stat_card
from components.ui.section_title import section_title
from components.ui.info_card import info_card
from components.ui.progress_card import progress_card
from components.ui.ai_command_center import ai_command_center
from components.ui.ai_pipeline import run_pipeline

from services.dashboard_service import DashboardService
from services.command_center_service import CommandCenterService
from components.ui.hero_dashboard import hero_dashboard
from components.ui.health_card import health_card


def show():

    # =====================================================
    # Load Resume Profile
    # =====================================================

    profile = st.session_state.get("resume_profile")

    dashboard = DashboardService().get_dashboard(profile)

    # =====================================================
    # Header
    # =====================================================

    user = st.session_state.get("user")

    if user:

     hero_dashboard(

        user[1]

    )

    else:

     hero_dashboard(

        "Guest"

    )
     health = 91

     health_card(health)



    st.divider()

    section_title(
        "Career Dashboard",
        "Track your AI career growth."
    )

    # =====================================================
    # Statistics Cards
    # =====================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        stat_card(
            "Projects",
            dashboard["projects"],
            "Live"
        )

    with col2:

        stat_card(
            "Skills",
            dashboard["skills"],
            "Resume"
        )

    with col3:

        stat_card(
            "Experience",
            dashboard["experience"],
            "Jobs"
        )

    with col4:

        stat_card(
            "Education",
            dashboard["education"],
            "Degrees"
        )

    
    st.divider()

    st.subheader("📅 Recent Activity")

    st.info("Resume uploaded successfully.")

    st.info("ATS analysis completed.")

    st.info("Interview session finished.")
    st.divider()

    st.subheader("🧠 AI Recommendation")

    st.success(

"""
You are close to becoming interview-ready.

Focus on:

• Docker

• Kubernetes

• LangGraph

• AWS Deployment

"""
)
    st.subheader("📅 Today's Goal")

    st.success(

"""
Complete one ATS analysis.

Finish one interview session.

Learn one missing skill.

"""
)
    st.divider()

    st.subheader("🔥 AI Career Roadmap")

    st.info(

"""
Current Level

AI Student

↓

Next

AI Engineer

↓

Senior AI Engineer

↓

AI Architect

"""
)

    # =====================================================
    # Recommendation
    # =====================================================

    info_card(
        "Today's Recommendation",
        "Upload your latest resume and use ATS Intelligence to discover missing skills for your dream role."
    )

    st.divider()

    # =====================================================
    # Career Progress
    # =====================================================

    progress = 0

    if profile:

        progress = min(
            100,
            dashboard["skills"] * 3
            + dashboard["projects"] * 10
            + dashboard["experience"] * 15
        )

    progress_card(
        "Career Progress",
        progress
    )

    st.divider()

    # =====================================================
    # AI Command Center
    # =====================================================

    analyze, question = ai_command_center()

    if analyze:

        if profile is None:

            st.warning(
                "Please upload your resume first from the Resume page."
            )

            return

        run_pipeline()

        service = CommandCenterService()

        result = service.process(
            question,
            profile
        )

        st.divider()

        st.subheader("🤖 CareerNova AI")

        st.markdown(
            f"### {result['title']}"
        )

        st.write(
            result["response"]
        )