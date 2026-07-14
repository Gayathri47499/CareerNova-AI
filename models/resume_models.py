from typing import List

from pydantic import BaseModel


# -------------------------
# Education
# -------------------------

class Education(BaseModel):

    degree: str

    field: str

    university: str

    duration: str

    cgpa: str


# -------------------------
# Project
# -------------------------

class Project(BaseModel):

    name: str

    technologies: List[str]

    description: str


# -------------------------
# Experience
# -------------------------

class Experience(BaseModel):

    role: str

    duration: str

    achievements: List[str]


# -------------------------
# Skills
# -------------------------

class Skills(BaseModel):

    languages: List[str]

    backend: List[str]

    databases: List[str]

    cloud: List[str]

    ai_genai: List[str]

    tools: List[str]


# -------------------------
# Career Profile
# -------------------------

class CareerProfile(BaseModel):

    career_level: str

    recommended_roles: List[str]

    technical_strengths: List[str]

    soft_skills: List[str]

    missing_skills: List[str]


# -------------------------
# Resume
# -------------------------

class ResumeData(BaseModel):

    name: str

    email: str

    phone: str

    education: List[Education]

    skills: Skills

    projects: List[Project]

    experience: List[Experience]

    certifications: List[str]

    career_profile: CareerProfile