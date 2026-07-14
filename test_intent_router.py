from orchestrator.intent_router import IntentRouter

router = IntentRouter()

questions = [

    "Improve my resume",

    "Check ATS score",

    "How can I become an AI Engineer?",

    "Ask me Java interview questions",

    "Tell me about Python"
]

for q in questions:

    print(q)

    print("→", router.route(q))

    print()