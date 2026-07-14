import bcrypt

from repositories.user_repository import UserRepository


class AuthService:

    def __init__(self):

        self.repository = UserRepository()

    def register(

        self,

        name,

        email,

        password

    ):

        password_hash = bcrypt.hashpw(

            password.encode(),

            bcrypt.gensalt()

        ).decode()

        self.repository.create_user(

            name,

            email,

            password_hash

        )

    def login(

        self,

        email,

        password

    ):

        user = self.repository.get_user(

            email

        )

        if user is None:

            return None

        stored_hash = user[3]

        if bcrypt.checkpw(

            password.encode(),

            stored_hash.encode()

        ):

            return user

        return None