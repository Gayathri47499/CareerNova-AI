from agents.career_agent import CareerAgent


class AnswerGenerator:

    def __init__(self):

        self.agent = CareerAgent()

    def answer(

        self,

        question,

        context

    ):

        prompt = f"""
Answer the question using ONLY the context below.

Context:

{context}

Question:

{question}
"""

        return self.agent.chat(

            prompt

        )