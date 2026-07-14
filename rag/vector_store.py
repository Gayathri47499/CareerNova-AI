import faiss
import numpy as np


class ResumeVectorStore:

    def __init__(self):

        self.index = None

        self.documents = []

    def build(self, embeddings, chunks):

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(
            np.array(
                embeddings,
                dtype="float32"
            )
        )

        self.documents = chunks

    def search(
        self,
        embedding,
        k=3
    ):

        _, indices = self.index.search(
            np.array(
                [embedding],
                dtype="float32"
            ),
            k
        )

        return [

            self.documents[i]

            for i in indices[0]

        ]