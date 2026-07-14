from mcp.server.fastmcp import FastMCP

from services.knowledge_manager import KnowledgeManager
from utils.response_formatter import ResponseFormatter

mcp = FastMCP("AI Career Copilot")

knowledge_manager = KnowledgeManager()


@mcp.tool()
def get_all_skills():
    """
    Returns all skills from the knowledge base.
    """

    skills = knowledge_manager.get_all_skills()

    return ResponseFormatter.format(skills)


if __name__ == "__main__":
    mcp.run()
@mcp.tool()
def get_skill_by_id(skill_id: str):
    """
    Returns one skill using its ID.
    """

    skill = knowledge_manager.get_skill_by_id(skill_id)

    if skill is None:
        return {"error": "Skill not found"}

    return ResponseFormatter.format(skill)
@mcp.tool()
def get_skill_by_name(name: str):
    """
    Returns one skill using its name.
    """

    skill = knowledge_manager.get_skill_by_name(name)

    if skill is None:
        return {"error": "Skill not found"}

    return ResponseFormatter.format(skill)
@mcp.tool()
def get_skills_by_category(category: str):
    """
    Returns all skills in a category.
    """

    skills = knowledge_manager.get_skills_by_category(category)

    return [
        {
            "id": skill.id,
            "name": skill.name,
            "level": skill.level,
            "confidence": skill.confidence,
        }
        for skill in skills
    ]
@mcp.tool()
def get_all_projects():

    projects = knowledge_manager.get_all_projects()

    return ResponseFormatter.format(projects)
@mcp.tool()
def get_project_by_id(project_id: str):

    project = knowledge_manager.get_project_by_id(project_id)

    return ResponseFormatter.format(project)
@mcp.tool()
def get_project_by_name(name: str):

    project = knowledge_manager.get_project_by_name(name)

    return ResponseFormatter.format(project)