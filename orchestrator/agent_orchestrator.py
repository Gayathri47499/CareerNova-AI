from orchestrator.intent_router import IntentRouter

from agents.resume_agent import ResumeAgent
from agents.ats_agent import ATSAgent
from agents.chat_agent import ChatAgent


class AgentOrchestrator:

    """
    Central AI Router

    Every AI request passes through here.
    """

    def __init__(self):

        self.router = IntentRouter()

        self.resume_agent = ResumeAgent()

        self.ats_agent = ATSAgent()

        self.chat_agent = ChatAgent()

    def execute(

        self,

        question,

        resume=None,

        job_description=None,

        interview=None,

        analytics=None

    ):

        intent = self.router.route(question)

        # -------------------------
        # Resume
        # -------------------------

        if intent == "resume":

            answer = self.resume_agent.analyze(

                resume,

                question

            )

            return {

                "intent": intent,

                "answer": answer

            }

        # -------------------------
        # ATS
        # -------------------------

        elif intent == "ats":

            answer = self.ats_agent.analyze(

                resume,

                job_description

            )

            return {

                "intent": intent,

                "answer": answer

            }

        # -------------------------
        # Default Chat
        # -------------------------

        else:

            answer = self.chat_agent.ask(

                resume,

                question,

                ats=None,

                interview=interview,

                analytics=analytics

            )

            return {

                "intent": "chat",

                "answer": answer

            }