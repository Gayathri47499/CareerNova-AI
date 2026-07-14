from data.database import get_connection
import json


class ATSRepository:

    def save_analysis(

        self,

        job_title,

        ats_result

    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(

            """
            INSERT INTO career_events(

                user_id,

                event_type,

                event_data

            )

            VALUES(

                ?,

                ?,

                ?

            )
            """,

            (

                1,

                "ATS",

                json.dumps({

                    "job": job_title,

                    "score": ats_result["score"],

                    "match": ats_result["match_percentage"]

                })

            )

        )

        conn.commit()

        conn.close()

    def get_history(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(

            """
            SELECT event_data

            FROM career_events

            WHERE event_type='ATS'

            ORDER BY id DESC
            """
        )

        rows = cursor.fetchall()

        conn.close()

        history = []

        for row in rows:

            history.append(

                json.loads(row[0])

            )

        return history