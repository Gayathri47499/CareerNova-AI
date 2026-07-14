from agents.resume_agent import ResumeAgent

agent = ResumeAgent()

job_description = """
AI Engineer Internship

Requirements

Python

AWS

LangGraph

Docker

REST APIs

Machine Learning

Prompt Engineering
"""

result = agent.analyze(job_description)

print(result)