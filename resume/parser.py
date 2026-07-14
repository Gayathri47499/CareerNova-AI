import fitz
import docx


class ResumeParser:

    def read_pdf(self, path):

        text = ""

        document = fitz.open(path)

        for page in document:

            text += page.get_text()

        return text

    def read_docx(self, path):

        document = docx.Document(path)

        text = ""

        for paragraph in document.paragraphs:

            text += paragraph.text + "\n"

        return text