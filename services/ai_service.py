from context.context_builder import ContextBuilder
from prompt_builder.prompt_builder import PromptBuilder
from memory.session_memory import SessionMemory
from retrieval.knowledge_retriever import KnowledgeRetriever
from llm.groq_client import llm


class AIService:

    def __init__(self):

        self.context = ContextBuilder()

        self.memory = SessionMemory()

        self.retriever = KnowledgeRetriever()

        self.prompt = PromptBuilder()

    def ask(

        self,

        system_prompt,

        question,

        resume=None,

        ats=None,

        interview=None,

        analytics=None

    ):

        context = self.context.build(

            resume,

            ats,

            interview,

            analytics

        )

        retrieved = self.retriever.retrieve(

            resume,

            ats,

            interview,

            analytics

        )

        history = self.memory.history()

        final_prompt = self.prompt.build(

            system_prompt,

            {

                "context": context,

                "retrieved": retrieved,

                "history": history

            },

            question

        )

        response = llm.invoke(

            final_prompt

        )

        answer = response.content

        self.memory.add(

            "user",

            question

        )

        self.memory.add(

            "assistant",

            answer

        )

        return answer