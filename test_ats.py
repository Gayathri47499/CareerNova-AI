from ats.ats_engine import ATSEngine

engine = ATSEngine()

profile = {

    "skills":[

        {"name":"Python"},

        {"name":"AWS"},

        {"name":"SQL"},

        {"name":"Django"}

    ]

}

jd = """

Looking for

Python

AWS

Docker

"""

result = engine.calculate_score(

    profile,

    jd

)

print(result)