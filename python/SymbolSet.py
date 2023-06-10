import Symbol
from collections import OrderedDict

class SymbolSet:
    def __init__(self) -> None:
        self.individuals = OrderedDict()
        
    def isEmpty(self):
        return len(self.individuals) == 0
    
    def clear(self):
        self.individuals.clear()
        
    def include(self, symbol: Symbol.Symbol):
        self.individuals[symbol.getSymbol()] = symbol
        
    def belongsTo(self, symbol: Symbol.Symbol):
        return symbol.getSymbol() in self.individuals

    def union(self, symbolSet):
        newSymbolSet = self.clone()
        for individual in symbolSet.individuals:
            newSymbolSet.include(individual)
        return newSymbolSet

    def intersection(self, symbolSet):
        newSymbolSet = SymbolSet()
        for individual in symbolSet.individuals:
            if self.belongsTo(individual):
                newSymbolSet.include(individual)
        return newSymbolSet

    def __eq__(self, __value: object) -> bool:
        tmp = self.clone()
        for individual in tmp.individuals:
            if(not __value.belongsTo(individual)):
                return False
        
        tmp = __value.clone()
        for individual in tmp.individuals:
            if(not self.belongsTo(individual)):
                return False
        
        return True
    
    def __ne__(self, __value: object) -> bool:
        tmp = self.clone()
        for individual in tmp.individuals:
            if(not __value.belongsTo(individual)):
                return True
        
        tmp = __value.clone()
        for individual in tmp.individuals:
            if(not self.belongsTo(individual)):
                return True
        
        return False

    def clone(self):
        newSet = SymbolSet()
        newSet.setSymbolSet(self.individuals)
        return newSet
    
    def __str__(self) -> str:
        resp = "{"
        index = len(self.individuals)
        for key in self.individuals:
            resp += key
            if(index > 1):
                resp += ', '
            index -= 1
        resp += "}"
        return resp
            
        
    def setSymbolSet(self, individuals: OrderedDict):
        self.individuals = individuals