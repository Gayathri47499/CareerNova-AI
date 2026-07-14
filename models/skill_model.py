from pydantic import BaseModel
from typing import List


class Skill(BaseModel):
    id: str
    name: str
    category: str
    level: str
    confidence: int
    description: str

    evidence: List[str]

    related_projects: List[str]

    related_experience: List[str]

    related_certifications: List[str]

    related_skills: List[str]

    last_used: str