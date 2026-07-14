from services.knowledge_manager import KnowledgeManager

manager = KnowledgeManager()

print(manager.get_skill_by_id("SKILL_001"))

print(manager.get_skill_by_name("Python"))

print(manager.get_skills_by_category("Programming"))