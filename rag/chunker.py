class ResumeChunker:

    """
    Splits resume into meaningful chunks.
    """

    def chunk(self, resume):

        chunks = []

        chunks.append(
            f"""
Name:
{resume.name}
"""
        )

        for project in resume.projects:

            chunks.append(
                f"""
Project:

{project.name}

Description:

{project.description}
"""
            )

        for experience in resume.experience:

            chunks.append(
                f"""
Experience:

{experience.role}

Duration:

{experience.duration}
"""
            )

        return chunks