from sentence_transformers import SentenceTransformer

import faiss

import numpy as np
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
class VectorIndex:

    def __init__(self):

        self.index = None

        self.documents = []
    def build(self, documents):

     self.documents = documents

     vectors = model.encode(
        documents,
        convert_to_numpy=True
    )

     dimension = vectors.shape[1]

     self.index = faiss.IndexFlatL2(
        dimension
    )

     self.index.add(vectors)
    def search(self, query, k=5):

     query_vector = model.encode(
        [query],
        convert_to_numpy=True
    )

     distances, indices = self.index.search(
        query_vector,
        k
    )

     return [
        self.documents[i]
        for i in indices[0]
    ]