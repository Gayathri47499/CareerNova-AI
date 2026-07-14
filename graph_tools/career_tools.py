from langchain.tools import tool

from services.knowledge_manager import KnowledgeManager

manager = KnowledgeManager()


@tool
def get_all_skills():
    """
    Return all skills.
    """
    return [
        skill.model_dump()
        for skill in manager.get_all_skills()
    ]


@tool
def get_skill_by_name(name: str):
    """
    Return one skill by name.
    """

    skill = manager.get_skill_by_name(name)

    if skill is None:
        return {"error": "Skill not found"}

    return skill.model_dump()


@tool
def get_all_projects():
    """
    Return all projects.
    """

    return [
        project.model_dump()
        for project in manager.get_all_projects()
    ]


@tool
def get_project_by_name(name: str):
    """
    Return one project by its name.
    """

    project = manager.get_project_by_name(name)

    if project is None:
        return {"error": "Project not found"}

    return project.model_dump()
career_tools = [
    get_all_skills,
    get_skill_by_name,
    get_all_projects,
    get_project_by_name,
]