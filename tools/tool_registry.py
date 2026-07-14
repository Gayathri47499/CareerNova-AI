from services.knowledge_manager import KnowledgeManager


class ToolRegistry:

    def __init__(self):
        self.manager = KnowledgeManager()

    def get_all_skills(self):
        return self.manager.get_all_skills()

    def get_skill_by_name(self, name: str):
        return self.manager.get_skill_by_name(name)

    def get_all_projects(self):
        return self.manager.get_all_projects()

    def get_project_by_name(self, name: str):
        return self.manager.get_project_by_name(name)