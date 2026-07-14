from services.command_center_service import CommandCenterService

service = CommandCenterService()

questions = [
    "Improve my resume",
    "Check my ATS score",
    "Prepare me for an AI Engineer interview",
    "How do I become an AI Engineer?"
]

for q in questions:

    result = service.process(q)

    print(q)
    print(result)
    print("-" * 40)