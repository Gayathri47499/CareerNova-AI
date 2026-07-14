from ai_service.ai_service import AIService

ai = AIService()

text = """
Python is a powerful programming language.
It is used for AI, machine learning, web development,
automation, cloud computing, and data science.
"""

print(ai.summarize(text))