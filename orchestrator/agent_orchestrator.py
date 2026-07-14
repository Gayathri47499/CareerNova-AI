from orchestrator.intent_router import IntentRouter

from agents.resume_agent import ResumeAgent
from agents.ats_agent import ATSAgent
from agents.chat_agent import ChatAgent
from agents.career_agent import CareerAgent


class AgentOrchestrator:
    """
    Central AI Router
    """

    def __init__(self):

        self.router = IntentRouter()

        self.resume_agent = ResumeAgent()

        self.ats_agent = ATSAgent()

        self.chat_agent = ChatAgent()

        self.career_agent = CareerAgent()

    def execute(

        self,

        question,

        resume=None,

        job_description=None,

        interview=None,

        analytics=None

    ):

        intent = self.router.route(question)

        # -----------------------------
        # Resume Agent
        # -----------------------------

        if intent == "resume":

            answer = self.resume_agent.analyze(

                resume,

                question

            )

            return {

                "title": "📄 Resume Analysis",

                "response": answer

            }

        # -----------------------------
        # ATS Agent
        # -----------------------------

        elif intent == "ats":

            answer = self.ats_agent.analyze(

                resume,

                job_description

            )

            return {

                "title": "🎯 ATS Intelligence",

                "response": answer

            }

        # -----------------------------
        # Career Agent
        # -----------------------------

        elif intent == "career":

            answer = self.career_agent.generate_career_report(

                resume,

                question

            )

            return {

                "title": "🚀 Career Report",

                "response": answer

            }

        # -----------------------------
        # Chat Agent
        # -----------------------------

        else:

            answer = self.chat_agent.ask(

                resume,

                question,

                ats=None,

                interview=interview,

                analytics=analytics

            )

            return {

                "title": "🤖 CareerNova AI",

                "response": answer

            }