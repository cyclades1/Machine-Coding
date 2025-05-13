class CPU:
    def freeze(self): print("Freezing CPU...")
    def execute(self): print("Executing...")

class Memory:
    def load(self): print("Loading memory...")

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()

    def start(self):
        self.cpu.freeze()
        self.memory.load()
        self.cpu.execute()

# Usage
pc = ComputerFacade()
pc.start()
