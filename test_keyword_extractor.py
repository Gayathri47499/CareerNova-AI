from ats.keyword_extractor import KeywordExtractor

extractor = KeywordExtractor()

jd = """

We are hiring an AI Engineer.

Requirements

Python

AWS

Docker

Git

SQL

LangChain

Machine Learning

"""

keywords = extractor.extract(jd)

print(keywords)