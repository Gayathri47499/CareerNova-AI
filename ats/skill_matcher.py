class SkillMatcher:
    """
    Compares resume skills with job description skills.
    """

    def match(self, resume, job_keywords):

        resume_skills = []

        # Collect all resume skills
        for category in resume.skills.model_dump().values():

            for skill in category:

                resume_skills.append(skill.lower())

        matched = []
        missing = []

        for keyword in job_keywords:

            if keyword.lower() in resume_skills:

                matched.append(keyword)

            else:

                missing.append(keyword)

        percentage = 0

        if len(job_keywords) > 0:

            percentage = round(

                len(matched) /

                len(job_keywords) * 100,

                2

            )

        return {

            "matched": matched,

            "missing": missing,

            "percentage": percentage

        }