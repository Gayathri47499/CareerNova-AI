from resume.resume_service import ResumeService
from rag.rag_service import RAGService

resume = ResumeService().process_pdf(
    "sample_data/sample_resume.pdf"
)

rag = RAGService()

store = rag.build(resume)

print("Vector Store Built Successfully!")