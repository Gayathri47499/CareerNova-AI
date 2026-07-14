from pydantic import BaseModel
from typing import List, Dict


class Project(BaseModel):
    id: str
    name: str
    short_description: str
    problem_statement: str
    solution: str

    technologies: List[str]
    features: List[str]

    architecture: Dict

    challenges: List[str]
    solutions: List[str]

    results: List[str]

    metrics: Dict

    related_skills: List[str]

    related_experience: List[str]

    github: str

    demo: str

    interview_notes: Dict

    metadata: Dict