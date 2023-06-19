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
    
    def __hash__(self) -> int:
        st = str(self).replace('(', '').replace(')', '')
        sum = 0
        for c in st:
            sum += ord(c)
        return sum
    
    def __eq__(self, __value: object) -> bool:
        type_str = str(type(self)).split("'")[1]
        type_str_2 = str(type(__value)).split("'")[1]
        if(type_str_2 == 'NoneType' and type_str == 'NoneType'):
            return True
        if(type_str_2 == 'NoneType'):
            return False
        return self.destiny == __value.destiny and self.origin == __value.origin and self.symbol == __value.symbol
    
    def __str__(self) -> str:
        ret_str = "({},{},{})".format(self.origin.getName(), self.symbol, self.destiny.getName())
        return ret_str