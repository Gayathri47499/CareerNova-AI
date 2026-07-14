import json

from data.database import get_connection


class ResumeStorage:

    """
    Handles Resume Database Operations.
    """

    def save(self, resume):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO resumes(

                user_id,

                name,

                email,

                phone,

                resume_json

            )

            VALUES(?,?,?,?,?)
            """,
            (

                1,

                resume.name,

                resume.email,

                resume.phone,

                json.dumps(
                    resume.model_dump(),
                    indent=4
                )

            )
        )

        connection.commit()

        connection.close()

        print("Resume Stored Successfully!")