from resume.parser import ResumeParser
from resume.extractor import ResumeExtractor


class ResumeService:

    """
    Coordinates the complete resume processing pipeline.
    """

    def __init__(self):

        self.parser = ResumeParser()

        self.extractor = ResumeExtractor()

        from resume.storage import ResumeStorage

        self.storage = ResumeStorage()

    def process_pdf(self, pdf_path):

        resume_text = self.parser.read_pdf(pdf_path)

        resume = self.extractor.extract(resume_text)

        self.storage.save(resume)

        return resume

    def process_docx(self, docx_path):

        resume_text = self.parser.read_docx(docx_path)

        resume = self.extractor.extract(resume_text)

        self.storage.save(resume)

        return resume