from agents.career_agent import CareerAgent


class ChatAgent(CareerAgent):

    def ask(

        self,

        resume,

        question,

        ats=None,

        interview=None,

        analytics=None

    ):

        prompt = f"""
You are CareerNova AI.

You are an AI Career Coach.

Candidate Resume

{resume}

ATS Analysis

{ats}

Interview Report

{interview}

Career Analytics

{analytics}

User Question

{question}

Give a detailed professional answer.
"""

        return self.chat(prompt)