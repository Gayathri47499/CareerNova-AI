from ats.job_parser import JobParser

parser = JobParser()

jd = """

Python Developer


Must know Python

Django


REST APIs


AWS


"""

clean = parser.clean(jd)

print(clean)