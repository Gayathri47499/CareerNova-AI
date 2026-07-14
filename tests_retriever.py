from resume.resume_service import ResumeService

from rag.rag_service import RAGService


resume = ResumeService().process_pdf(

    "sample_data/sample_resume.pdf"

)

rag = RAGService()

rag.build(resume)

retriever = rag.retriever()

chunks = retriever.retrieve(

    "Tell me about the Pet Adoption project"

)

print()

print("Retrieved Chunks")

print()

for chunk in chunks:

    print(chunk)

    print("=" * 50)