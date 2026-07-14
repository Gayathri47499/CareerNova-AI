from agents.career_agent import CareerAgent
from ats.ats_engine import ATSEngine


class ATSAgent(CareerAgent):

    def __init__(self):

        super().__init__()

        self.engine = ATSEngine()

    def analyze(

        self,

        profile,

        job_description

    ):

        ats_result = self.engine.calculate_score(

            profile,

            job_description

        )

        prompt = f"""
You are an ATS Resume Expert.

Below is the ATS analysis result.

Explain it professionally.

Suggest improvements.

ATS Analysis

{ats_result}
"""

        explanation = self.chat(prompt)

        return {

            "ats": ats_result,

            "explanation": explanation

        }