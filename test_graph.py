from graph.career_graph import career_graph

response = career_graph.invoke(
    {
        "question": "What is Python?"
    }
)

print(response["answer"])