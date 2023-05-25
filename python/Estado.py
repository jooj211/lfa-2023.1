class State:
    def __init__(self, _name: str) -> None:
        self.name = _name
    
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
    
    def clone(self):
        state = State()
        state.setName(self.name)
        return state
    
    def equal(self, state):
        return state.getName() == self.name
    
    