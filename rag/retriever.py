from rag.embedder import ResumeEmbedder


class ResumeRetriever:

    """
    Searches Resume Vector Store
    """

    def __init__(self, store):

        self.store = store

        self.embedder = ResumeEmbedder()

    def retrieve(

        self,

        question,

        k=3

    ):

        embedding = self.embedder.embed(

            [question]

        )[0]

        return self.store.search(

            embedding,

            k

        )