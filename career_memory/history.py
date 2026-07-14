class CareerHistory:

    def __init__(self, memory):

        self.memory = memory

    def history(self):

        return self.memory.all()