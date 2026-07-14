class DashboardService:

    def get_dashboard(self, profile):

        if profile is None:

            return {

                "projects": 0,

                "skills": 0,

                "experience": 0,

                "education": 0

            }

        return {

            "projects": len(profile.projects),

            "skills": (

                len(profile.skills.languages)

                + len(profile.skills.backend)

                + len(profile.skills.databases)

                + len(profile.skills.cloud)

                + len(profile.skills.ai_genai)

                + len(profile.skills.tools)

            ),

            "experience": len(profile.experience),

            "education": len(profile.education)

        }