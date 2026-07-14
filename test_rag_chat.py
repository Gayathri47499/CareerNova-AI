from resume.resume_service import ResumeService

from rag.rag_service import RAGService


resume = ResumeService().process_pdf(

    "sample_data/sample_resume.pdf"

)

rag = RAGService()

rag.build(resume)

print(

    rag.ask(

        "Explain my Pet Adoption project."

    )

)