import re


class JobParser:
    """
    Cleans and normalizes a job description.
    """

    def clean(self, job_description: str):

        # Remove multiple spaces
        text = re.sub(r"\s+", " ", job_description)

        return text.strip()