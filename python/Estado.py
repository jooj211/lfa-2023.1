class State:
    def __init__(self, _name: str) -> None:
        self.name = _name
    
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
    
    