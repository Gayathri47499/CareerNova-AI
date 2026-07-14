from tools.tool_registry import ToolRegistry

tools = ToolRegistry()

print(tools.get_all_skills())

print()

print(
    tools.get_project_by_name(
        "Pet Adoption and Rescue Management Portal"
    )
)