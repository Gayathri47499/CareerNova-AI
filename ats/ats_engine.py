from config.ats_weights import ATS_WEIGHTS
import re


class ATSEngine:
    """
    AI Resume ATS Engine
    """

    def calculate_score(self, profile, job_description):

        jd = job_description.lower()

        # -------------------------------------
        # Resume Skills
        # -------------------------------------

        resume_skills = []

        skills = profile.skills

        resume_skills.extend(skills.languages)
        resume_skills.extend(skills.backend)
        resume_skills.extend(skills.databases)
        resume_skills.extend(skills.cloud)
        resume_skills.extend(skills.ai_genai)
        resume_skills.extend(skills.tools)

        resume_skills = list(set([s.lower().strip() for s in resume_skills]))

        # -------------------------------------
        # Extract Skills From JD
        # -------------------------------------

        words = re.findall(r"[a-zA-Z0-9\+\#\.]+", jd)

        jd_words = list(set(words))

        matched_skills = []
        missing_skills = []

        for skill in resume_skills:

            if skill in jd_words or skill in jd:

                matched_skills.append(skill)

        # -------------------------------------
        # JD Required Skills
        # -------------------------------------

        common_ai_skills = [

            "python",
            "java",
            "c++",
            "sql",
            "aws",
            "azure",
            "gcp",
            "docker",
            "kubernetes",
            "git",
            "github",
            "tensorflow",
            "pytorch",
            "langchain",
            "langgraph",
            "rag",
            "llm",
            "genai",
            "openai",
            "groq",
            "fastapi",
            "flask",
            "django",
            "streamlit",
            "numpy",
            "pandas",
            "scikit-learn",
            "machine learning",
            "deep learning",
            "rest",
            "api"

        ]

        required = []

        for skill in common_ai_skills:

            if skill in jd:

                required.append(skill)

        required = list(set(required))

        for skill in required:

            if skill not in matched_skills:

                missing_skills.append(skill)

        # -------------------------------------
        # Score
        # -------------------------------------

        if len(required) == 0:

            percentage = 0

        else:

            percentage = len(matched_skills) / len(required)

        percentage = min(percentage, 1)

        final_score = round(

            percentage * ATS_WEIGHTS["skills"]

        )

        return {

            "score": final_score,

            "match_percentage": round(

                percentage * 100,

                2

            ),

            "matched_skills": sorted(matched_skills),

            "missing_skills": sorted(missing_skills),

            "required_skills": sorted(required)

        }