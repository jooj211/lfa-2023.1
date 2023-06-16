class Symbol:
    def __init__(self, symbol: str) -> None:
        if len(symbol) != 1:
            raise Exception("Simbolos do alfabeto apenas podem ser representados por um caractere")
        
        self.symbol = symbol
    
    def getSymbol(self):
        return self.symbol
    
    def setSymbol(self, symbol):
        if len(symbol) != 1:
            raise Exception("Simbolos do alfabeto apenas podem ser representados por um caractere")
        
        self.symbol = symbol
        
    def clone(self):
        symbol_ = Symbol(self.symbol)
        return symbol_
    
    def __eq__(self, __value: object) -> bool:
        return self.symbol == __value.getSymbol()
    
    def __ne__(self, __value: object) -> bool:
        return self.symbol != __value.getSymbol()
    
    def __str__(self) -> str:
        return self.symbol
    
    