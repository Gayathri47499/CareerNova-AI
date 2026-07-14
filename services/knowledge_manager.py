from repositories.skill_repository import SkillRepository
from repositories.project_repository import ProjectRepository


class KnowledgeManager:

    def __init__(self):

        self.skill_repository = SkillRepository()
        self.project_repository = ProjectRepository()

    def get_all_skills(self):

        return self.skill_repository.get_all_skills()
    def get_skill_by_id(self, skill_id: str):

        return self.skill_repository.get_skill_by_id(skill_id)
    def get_skill_by_name(self, name: str):
        return self.skill_repository.get_skill_by_name(name)
    def get_skills_by_category(self, category: str):
        return self.skill_repository.get_skills_by_category(category)
    def get_all_projects(self):
      return self.project_repository.get_all_projects()


    def get_project_by_id(self, project_id: str):
     return self.project_repository.get_project_by_id(project_id)


    def get_project_by_name(self, name: str):
     return self.project_repository.get_project_by_name(name)
    def get_candidate_profile(self):

     return {
        "skills": [
            skill.model_dump()
            for skill in self.get_all_skills()
        ],
        "projects": [
            project.model_dump()
            for project in self.get_all_projects()
        ]
    }