from resume.parser import ResumeParser

parser = ResumeParser()

text = parser.read_pdf(
    "sample_data/sample_resume.pdf"
)

print(text[:1000])