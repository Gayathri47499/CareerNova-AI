from agents.interview_agent import InterviewAgent
import re


class InterviewService:

    def __init__(self):
        self.agent = InterviewAgent()

    def generate_questions(self, company, role, difficulty):

        raw = self.agent.generate_questions(
            company,
            role,
            difficulty
        )

        questions = []

        for line in raw.split("\n"):

            line = line.strip()

            if re.match(r"^\d+\.", line):
                question = re.sub(r"^\d+\.\s*", "", line)
                questions.append(question)

        return questions

    def evaluate(self, question, answer):

        return self.agent.evaluate_answer(
            question,
            answer
        )