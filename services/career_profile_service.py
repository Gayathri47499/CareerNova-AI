from repositories.ats_repository import ATSRepository


class CareerProfileService:

    def __init__(self):
        self.ats_repository = ATSRepository()

    def build_profile(self, resume_profile):

        history = self.ats_repository.get_history()

        if history:
            scores = [item["score"] for item in history]
            ats_average = round(sum(scores) / len(scores))
        else:
            ats_average = 0

        skills = []

        if resume_profile:
            try:
                skills = resume_profile.skills.languages
                skills += resume_profile.skills.backend
                skills += resume_profile.skills.cloud
            except Exception:
                skills = []

        return {
            "resume": resume_profile,
            "ats_average": ats_average,
            "skills": skills
        }