class CareerAnalytics:

    def __init__(self, memory):

        self.memory = memory

    def total_events(self):

        return len(

            self.memory.all()

        )