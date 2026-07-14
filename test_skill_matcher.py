from resume.resume_service import ResumeService
from ats.keyword_extractor import KeywordExtractor
from ats.skill_matcher import SkillMatcher

resume = ResumeService().process_pdf(
    "sample_data/sample_resume.pdf"
)

jd = """
Python
AWS
Docker
Git
REST API
"""

keywords = KeywordExtractor().extract(jd)

matcher = SkillMatcher()

result = matcher.match(

    resume,

    keywords

)

print(result)