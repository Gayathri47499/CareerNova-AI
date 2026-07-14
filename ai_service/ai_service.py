from llm.groq_client import llm
from tools.tool_registry import ToolRegistry


class AIService:

    def __init__(self):
        self.tools = ToolRegistry()

    def ask(self, prompt: str):

        response = llm.invoke(prompt)

        return response.content

    def summarize(self, text: str):

        prompt = f"""
Summarize the following text in 5 bullet points.

{text}
"""

        response = llm.invoke(prompt)

        return response.content