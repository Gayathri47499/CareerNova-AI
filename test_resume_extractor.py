from resume.parser import ResumeParser

from resume.extractor import ResumeExtractor


parser = ResumeParser()

extractor = ResumeExtractor()

text = parser.read_pdf(

    "sample_data/sample_resume.pdf"

)

resume = extractor.extract(text)

print(resume)