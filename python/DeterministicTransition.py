from Estado import State
from Symbol import Symbol

class DeterministicTransition:
    def __init__(self, origin: State, destiny: State, symbol: Symbol) -> None:
        self.origin = origin
        self.destiny = destiny
        self.symbol = symbol
    
    def clone(self):
        clone = DeterministicTransition(self.origin, self.destiny, self.symbol)
        return clone
    
    def __eq__(self, __value: object) -> bool:
        if(self == None and __value == None):
            return True
        if(__value == None):
            return False
        return self.destiny == __value.destiny and self.origin == __value.origin and self.symbol == __value.symbol
    
    def __str__(self) -> str:
        ret_str = "{},{},{}".format(self.origin, self.symbol, self.destiny)
        return ret_str