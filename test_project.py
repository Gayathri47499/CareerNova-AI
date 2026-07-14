from services.knowledge_manager import KnowledgeManager

manager = KnowledgeManager()

print(manager.get_all_projects())

print(manager.get_project_by_id("PROJECT_001"))

print(manager.get_project_by_name("AI Career Copilot"))