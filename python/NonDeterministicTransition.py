from Estado import State
from ConjuntoEstados import StateSet
from Symbol import Symbol

class NonDeterministicTransition:
    def __init__(self, origin: State, destiny: StateSet, symbol: Symbol) -> None:
        self.origin = origin
        self.destiny = destiny
        self.symbol = symbol
    
    def clone(self):
        return NonDeterministicTransition(self.origin, self.destiny, self.symbol)
    
    def __eq__(self, __value: object) -> bool:
        if(self.origin == __value.origin and self.destiny == __value.destiny and self.symbol == __value.symbol):
            return True
        return False
    
    def __hash__(self) -> int:
        st = str(self).replace('(', '').replace(')', '')
        sum = 0
        for c in st:
            sum += ord(c)
        return sum
    
    def __str__(self) -> str:
        final_str = "("
        final_str += str(self.origin) + ","
        final_str += str(self.symbol) + ","
        final_str += str(self.destiny)
        final_str += ")"
        return final_str