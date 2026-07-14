from pathlib import Path

from repositories.base_repository import BaseRepository
from models.project_model import Project


class ProjectRepository(BaseRepository):

    def __init__(self):
        super().__init__(Path("knowledge_base") / "projects.json")

        self._cache = None
    def get_all_projects(self):

     if self._cache is not None:
        return self._cache

     data = self.load_json()

     projects = [
        Project(**project)
        for project in data["projects"]
    ]

     self._cache = projects

     return projects
    def get_project_by_id(self, project_id: str):

     for project in self.get_all_projects():

        if project.id == project_id:
            return project

     return None


    def get_project_by_name(self, name: str):

     for project in self.get_all_projects():

        if project.name.lower() == name.lower():
            return project

     return None