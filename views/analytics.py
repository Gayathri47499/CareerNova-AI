import streamlit as st

from analytics.career_analytics_service import CareerAnalyticsService

from components.ui.analytics_metric import analytics_metric

from components.ui.analytics_progress import analytics_progress


def show():

    st.title("📈 Career Analytics")

    service = CareerAnalyticsService()

    data = service.generate_dashboard()

    col1,col2,col3,col4=st.columns(4)

    with col1:

        analytics_metric(

            "Career",

            data["career_readiness"]

        )

    with col2:

        analytics_metric(

            "Resume",

            data["resume_health"]

        )

    with col3:

        analytics_metric(

            "ATS",

            data["ats_average"]

        )

    with col4:

        analytics_metric(

            "Interview",

            data["interview"]

        )

    st.divider()

    analytics_progress(

        "Overall Skill Coverage",

        data["skill_coverage"]

    )

    st.divider()

    col1,col2=st.columns(2)

    with col1:

        st.subheader("🟢 Top Skills")

        for skill in data["top_skills"]:

            st.success(skill)

    with col2:

        st.subheader("🔴 Missing Skills")

        for skill in data["missing_skills"]:

            st.error(skill)

    st.divider()

    st.subheader("🤖 AI Recommendation")

    st.info(

        data["recommendation"]

    )