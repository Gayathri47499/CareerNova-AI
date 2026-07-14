from llm.groq_client import llm
from services.ai_service import AIService


class CareerAgent:

    def __init__(self):

        self.ai = AIService()

    # ---------------------------------------------------
    # Generic AI Pipeline
    # ---------------------------------------------------

    def ask(

        self,

        system_prompt,

        question,

        resume=None,

        ats=None,

        interview=None,

        analytics=None

    ):

        return self.ai.ask(

            system_prompt,

            question,

            resume,

            ats,

            interview,

            analytics

        )

    # ---------------------------------------------------
    # Backward Compatibility
    # ---------------------------------------------------

    def chat(self, prompt):

        response = llm.invoke(prompt)

        return response.content

    # ---------------------------------------------------
    # Career Report
    # ---------------------------------------------------

    def generate_career_report(

        self,

        profile,

        question

    ):

        prompt = f"""
You are CareerNova AI.

You are an expert AI Career Coach.

Candidate Profile

{profile}

User Request

{question}

Generate a detailed career report.

Include:

1. Current Career Level

2. Strengths

3. Weaknesses

4. Missing Skills

5. Recommended Learning Path

6. Best Career Roles

7. Interview Preparation Tips

8. Final Career Advice
"""

        return self.chat(prompt)