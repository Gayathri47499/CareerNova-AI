from typing import Optional


class ContextBuilder:

    """
    Builds one unified AI context
    from every module inside CareerNova AI.
    """

    def build(

        self,

        resume=None,

        ats=None,

        interview=None,

        analytics=None

    ):

        context = {}

        # --------------------------
        # Resume
        # --------------------------

        if resume:

            context["candidate"] = {

                "name": resume.name,

                "email": resume.email,

                "education": [

                    e.model_dump()

                    for e in resume.education

                ],

                "skills": resume.skills.model_dump(),

                "projects": [

                    p.model_dump()

                    for p in resume.projects

                ],

                "experience": [

                    e.model_dump()

                    for e in resume.experience

                ],

                "certifications": resume.certifications

            }

        # --------------------------
        # ATS
        # --------------------------

        if ats:

            context["ats"] = ats

        # --------------------------
        # Interview
        # --------------------------

        if interview:

            context["interview"] = interview

        # --------------------------
        # Analytics
        # --------------------------

        if analytics:

            context["analytics"] = analytics

        return context