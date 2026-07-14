from services.knowledge_manager import KnowledgeManager

manager = KnowledgeManager()

skills = manager.get_all_skills()

for skill in skills:
    print(skill.name)