import re


class KeywordExtractor:
    """
    Extracts technical keywords from a job description.
    """

    def __init__(self):

        self.skills = [

            "python",
            "java",
            "c++",
            "django",
            "flask",
            "fastapi",
            "aws",
            "azure",
            "gcp",
            "docker",
            "kubernetes",
            "terraform",
            "linux",
            "git",
            "github",
            "sql",
            "mysql",
            "postgresql",
            "mongodb",
            "rest",
            "rest api",
            "api",
            "langchain",
            "langgraph",
            "machine learning",
            "deep learning",
            "tensorflow",
            "pytorch",
            "opencv",
            "pandas",
            "numpy",
            "streamlit",
            "ci/cd"
        ]

    def extract(self, job_description):

        text = job_description.lower()

        found = []

        for skill in self.skills:

            pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(pattern, text):

                found.append(skill)

        return sorted(list(set(found)))