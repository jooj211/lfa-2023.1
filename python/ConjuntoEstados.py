from collections import OrderedDict

class StateSet:
    def __init__(self) -> None:
        self.individuals = OrderedDict()
    
    def isEmpty(self):
        return len(self.individuals) == 0

    def clear(self):
        self.individuals.clear()
    
    