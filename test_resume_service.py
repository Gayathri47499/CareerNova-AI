from resume.resume_service import ResumeService

service = ResumeService()

resume = service.process_pdf(
    "sample_data/sample_resume.pdf"
)

print(resume)