from agents.career_agent import CareerAgent

agent = CareerAgent()

response = agent.chat(
    "Explain Python in two sentences."
)

print(response)