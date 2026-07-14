from agents.chat_agent import ChatAgent


class ChatService:

    def __init__(self):

        self.agent = ChatAgent()

    def ask(

        self,

        profile,

        question

    ):

        return self.agent.ask(

            profile,

            question

        )