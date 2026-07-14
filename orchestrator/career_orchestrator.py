from agents.resume_agent import ResumeAgent
from agents.ats_agent import ATSAgent
from agents.career_agent import CareerAgent


class CareerOrchestrator:

    def __init__(self):
        self.resume_agent = ResumeAgent()
        self.ats_agent = ATSAgent()
        self.career_agent = CareerAgent()

    def execute(self, intent, profile, question):

        result = {}

        if intent == "resume":

            result["resume"] = self.resume_agent.analyze(question)

        elif intent == "career":

            result["career"] = self.career_agent.generate_career_report(
                profile,
                question
            )

        elif intent == "ats":

            result["ats"] = self.ats_agent.analyze(
                profile,
                question
            )

        else:

            result["chat"] = (
                "This feature will be connected in the next phase."
            )

        return result