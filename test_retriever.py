from retriever.profile_retriever import ProfileRetriever

retriever = ProfileRetriever()

job_description = """
Looking for

Python

AWS

SQL

REST APIs
"""

profile = retriever.retrieve(job_description)

print(profile)