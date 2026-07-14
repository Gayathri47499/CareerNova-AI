from vector_store.vector_index import VectorIndex

index = VectorIndex()

docs = [

    "Python",

    "AWS",

    "SQL",

    "Machine Learning",

    "Django REST Framework",

    "Docker"

]

index.build(docs)

results = index.search(

    "RESTful Backend APIs"

)

print(results)