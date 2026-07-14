from typing import TypedDict

from langgraph.graph import StateGraph, END

from ai_service.ai_service import AIService


class CareerState(TypedDict):
    question: str
    answer: str


# Create AI Service Object
ai = AIService()


def llm_node(state: CareerState):

    answer = ai.ask(state["question"])

    return {
        "answer": answer
    }


graph = StateGraph(CareerState)

graph.add_node("llm", llm_node)

graph.set_entry_point("llm")

graph.add_edge("llm", END)

career_graph = graph.compile()