from rag.chunker import ResumeChunker
from rag.embedder import ResumeEmbedder
from rag.vector_store import ResumeVectorStore
from rag.retriever import ResumeRetriever
from rag.answer_generator import AnswerGenerator


class RAGService:

    def __init__(self):

        self.chunker = ResumeChunker()

        self.embedder = ResumeEmbedder()

        self.store = ResumeVectorStore()
        self.generator = AnswerGenerator()

    def build(self, resume):

        chunks = self.chunker.chunk(resume)

        embeddings = self.embedder.embed(chunks)

        self.store.build(

            embeddings,

            chunks

        )

    def retriever(self):

        return ResumeRetriever(

            self.store

        )
    def ask(

     self,

     question

):

     retriever = self.retriever()

     chunks = retriever.retrieve(question)

     context = "\n".join(chunks)

     return self.generator.answer(

        question,

        context

    )