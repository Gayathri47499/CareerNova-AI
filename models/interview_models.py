from pydantic import BaseModel
from typing import List


class InterviewQuestion(BaseModel):

    question: str

    category: str

    difficulty: str


class InterviewReport(BaseModel):

    company: str

    role: str

    score: int

    strengths: List[str]

    improvements: List[str]

    feedback: str