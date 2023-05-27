from Estado import State
from Symbol import Symbol

class DeterministicTransition:
    def __init__(self, origin: State, destiny: State, symbol: Symbol) -> None:
        self.origin = origin
        self.destiny = destiny
        self.symbol = symbol
    
    def clone(self):
        clon = DeterministicTransition(self.origin, self.destiny, self.symbol)
        return clon
    
    def __eq__(self, __value: object) -> bool:
        return self.destiny.equal(__value.destiny) and self.origin.equal(__value.origin) and self.symbol.equal(__value.symbol)