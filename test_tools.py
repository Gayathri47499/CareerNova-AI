from graph_tools.career_tools import get_skill_by_name

result = get_skill_by_name.invoke(
    {
        "name": "Python"
    }
)

print(result)