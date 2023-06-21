class State:
    def __init__(self, _name: str) -> None:
        self.name = _name
    
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
    
    def clone(self):
        state = State(self.name)
        return state
    
    def equal(self, state):
        return state.getName() == self.name
    
    def __str__(self) -> str:
        return self.getName()
    
    def __eq__(self, __value: object) -> bool:
        type_str = str(type(self)).split("'")[1]
        type_str_2 = str(type(__value)).split("'")[1]
        if(type_str_2 == 'NoneType' and type_str == 'NoneType'):
            return True
        if(type_str_2 == 'NoneType'):
            return False
        return self.getName() == __value.name
    
    