from resume.resume_service import ResumeService

from knowledge_graph.builder import GraphBuilder

from knowledge_graph.query import GraphQuery

service = ResumeService()

resume = service.process_pdf(

    "sample_data/sample_resume.pdf"

)

builder = GraphBuilder()

graph = builder.build(resume)

query = GraphQuery(graph)

print("Nodes")

print(query.nodes())

print("\nEdges")

for edge in graph.graph.edges(data=True):

    print(edge)