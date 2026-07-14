from career_memory.memory import CareerMemory

from career_memory.history import CareerHistory

from career_memory.analytics import CareerAnalytics


memory = CareerMemory()

memory.add(

    "Resume Uploaded"

)

memory.add(

    "ATS Analysis Completed"

)

memory.add(

    "Interview Questions Generated"

)

history = CareerHistory(memory)

analytics = CareerAnalytics(memory)

print(history.history())

print()

print(

    analytics.total_events()

)