from agents.ats_agent import ATSAgent

agent = ATSAgent()

profile = {

    "skills":[

        {"name":"Python"},

        {"name":"AWS"},

        {"name":"SQL"}

    ]

}

jd = """

Looking for

Python

AWS

Docker

"""

result = agent.analyze(

    profile,

    jd

)

print(result)