import streamlit as st

from resume.resume_service import ResumeService


def show():

    from components.ui.page_header import page_header

    page_header(

    "Resume Center",

    "AI-powered resume understanding and profile generation.",

    "📄"

)

    st.write(
        "Upload your resume and let CareerNova AI build your professional profile."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    if uploaded_file:

        with open(
            "sample_data/uploaded_resume.pdf",
            "wb"
        ) as f:

            f.write(uploaded_file.getbuffer())

        if st.button(
            "🚀 Analyze Resume",
            use_container_width=True
        ):

            with st.spinner("Analyzing Resume..."):

                service = ResumeService()

                profile = service.process_pdf(
                    "sample_data/uploaded_resume.pdf"
                )

            st.session_state["resume_profile"] = profile

            st.success("Resume analyzed successfully!")

    if "resume_profile" not in st.session_state:
        return

    profile = st.session_state["resume_profile"]

    # ----------------------------------------------------
    # Personal Information
    # ----------------------------------------------------

    st.divider()

    st.header("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        st.write(f"**Name:** {profile.name}")

        st.write(f"**Email:** {profile.email}")

    with col2:

        st.write(f"**Phone:** {profile.phone}")

    # ----------------------------------------------------
    # Education
    # ----------------------------------------------------

    st.divider()

    st.header("🎓 Education")

    for edu in profile.education:

        with st.container(border=True):

            st.write(f"**Degree:** {edu.degree}")

            st.write(f"**Field:** {edu.field}")

            st.write(f"**University:** {edu.university}")

            st.write(f"**Duration:** {edu.duration}")

            st.write(f"**CGPA:** {edu.cgpa}")

    # ----------------------------------------------------
    # Skills
    # ----------------------------------------------------

    st.divider()

    st.header("💻 Skills")

    skills = profile.skills

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Languages")

        st.write(", ".join(skills.languages))

        st.subheader("Backend")

        st.write(", ".join(skills.backend))

        st.subheader("Databases")

        st.write(", ".join(skills.databases))

    with col2:

        st.subheader("Cloud")

        st.write(", ".join(skills.cloud))

        st.subheader("AI / GenAI")

        st.write(", ".join(skills.ai_genai))

        st.subheader("Tools")

        st.write(", ".join(skills.tools))

    # ----------------------------------------------------
    # Projects
    # ----------------------------------------------------

    st.divider()

    st.header("🚀 Projects")

    for project in profile.projects:

        with st.container(border=True):

            st.subheader(project.name)

            st.write("**Technologies**")

            st.write(", ".join(project.technologies))

            st.write("**Description**")

            st.write(project.description)

    # ----------------------------------------------------
    # Experience
    # ----------------------------------------------------

    st.divider()

    st.header("💼 Experience")

    for exp in profile.experience:

        with st.container(border=True):

            st.subheader(exp.role)

            st.write(f"**Duration:** {exp.duration}")

            st.write("**Achievements**")

            for achievement in exp.achievements:

                st.write("✅", achievement)

    # ----------------------------------------------------
    # Certifications
    # ----------------------------------------------------

    st.divider()

    st.header("📜 Certifications")

    if profile.certifications:

        for cert in profile.certifications:

            st.success(cert)

    else:

        st.info("No certifications found.")

    # ----------------------------------------------------
    # Career Profile
    # ----------------------------------------------------

    st.divider()

    st.header("🎯 AI Career Profile")

    career = profile.career_profile

    st.subheader("Career Level")

    st.success(career.career_level)

    st.subheader("Recommended Roles")

    for role in career.recommended_roles:

        st.write("✅", role)

    st.subheader("Technical Strengths")

    for skill in career.technical_strengths:

        st.write("🟢", skill)

    st.subheader("Soft Skills")

    for skill in career.soft_skills:

        st.write("⭐", skill)

    st.subheader("Missing Skills")

    for skill in career.missing_skills:

        st.write("🔴", skill)