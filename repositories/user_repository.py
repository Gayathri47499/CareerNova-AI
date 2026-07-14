from data.database import get_connection


class UserRepository:

    def create_user(

        self,

        full_name,

        email,

        password_hash

    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(

            """
            INSERT INTO users(
                full_name,
                email,
                password
            )
            VALUES(?,?,?)
            """,

            (

                full_name,

                email,

                password_hash

            )

        )

        conn.commit()

        conn.close()

    def get_user(

        self,

        email

    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(

            """

            SELECT *

            FROM users

            WHERE email=?

            """,

            (

                email,

            )

        )

        user = cursor.fetchone()

        conn.close()

        return user