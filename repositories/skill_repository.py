from pathlib import Path

from repositories.base_repository import BaseRepository
from models.skill_model import Skill


class SkillRepository(BaseRepository):

    def __init__(self):
       super().__init__(Path("knowledge_base") / "skills.json")

       self._cache = None

    def get_all_skills(self):

      if self._cache is not None:
        return self._cache

      data = self.load_json()

      skills = []

      for skill in data["skills"]:
        skills.append(
            Skill(**skill)
        )

      self._cache = skills

      return skills
    def refresh_cache(self):

      self._cache = None

      return self.get_all_skills()

        
    def get_skill_by_id(self, skill_id: str):

       skills = self.get_all_skills()

       for skill in skills:

        if skill.id == skill_id:

          return skill

       return None
    def get_skill_by_name(self, name: str):

       skills = self.get_all_skills()

       for skill in skills:

        if skill.name.lower() == name.lower():

            return skill

       return None
    def get_skills_by_category(self, category: str):

      skills = self.get_all_skills()

      return [
        skill
        for skill in skills
        if skill.category.lower() == category.lower()
    ]