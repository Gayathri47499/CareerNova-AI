from repositories.skill_repository import SkillRepository

repo = SkillRepository()

print("First Load")
skills = repo.get_all_skills()

print("Second Load")
skills = repo.get_all_skills()

print("Cache Refresh")
repo.refresh_cache()

print("Done")