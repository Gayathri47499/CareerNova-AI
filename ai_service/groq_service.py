import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq


load_dotenv()


class AIService:

    def __init__(self):

        self.llm = ChatGroq(

            model="llama-3.3-70b-versatile",

            api_key=os.getenv("GROQ_API_KEY")

        )

    def ask(self, prompt):

        response = self.llm.invoke(prompt)

        return response.content