from agents.career_agent import CareerAgent


class InterviewAgent(CareerAgent):

    def generate_questions(

        self,

        company,

        role,

        difficulty

    ):

        prompt = f"""
You are an expert AI Interviewer.

Generate 10 interview questions.

Company:
{company}

Role:
{role}

Difficulty:
{difficulty}

Return only the numbered questions.
"""

        return self.chat(prompt)

    def evaluate_answer(

        self,

        question,

        answer

    ):

        prompt = f"""
You are an expert AI Technical Interviewer.

Interview Question

{question}

Candidate Answer

{answer}

Evaluate the answer.

Give:

1. Technical Score (/10)

2. Communication Score (/10)

3. Strengths

4. Weaknesses

5. Improvements

6. Final Feedback
"""

        return self.chat(prompt)