from agents.career_agent import CareerAgent

from prompts.resume_prompt import RESUME_ANALYZER_PROMPT


class ResumeAgent(CareerAgent):

    def analyze(

        self,

        resume,

        question

    ):

        return super().ask(

            RESUME_ANALYZER_PROMPT,

            question,

            resume=resume

        )