from services.knowledge_manager import KnowledgeManager


class ProfileRetriever:

    def __init__(self):

        self.manager = KnowledgeManager()
    def retrieve_skills(self, job_description: str):

     skills = self.manager.get_all_skills()

     matched = []

     jd = job_description.lower()
 
     for skill in skills:

        if skill.name.lower() in jd:

            matched.append(skill.model_dump())

     return matched
    def retrieve_projects(self, job_description: str):

     projects = self.manager.get_all_projects()

     matched = []

     jd = job_description.lower()

     for project in projects:

        for tech in project.technologies:

            if tech.lower() in jd:

                matched.append(project.model_dump())

                break

     return matched
    def retrieve(self, job_description: str):

     return {

        "skills": self.retrieve_skills(job_description),

        "projects": self.retrieve_projects(job_description)

    }