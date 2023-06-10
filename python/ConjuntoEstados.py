# Autor: Gustavo Gonçalves Silva
# Coautor: Jona-San

from collections import OrderedDict
import Estado

class StateSet:
    def __init__(self) -> None:
        self.individuals = OrderedDict()
    
    def isEmpty(self):
        return len(self.individuals) == 0

    def clear(self):
        self.individuals.clear()
    
    def include(self, elem: Estado.State):
        self.individuals[elem.getName()] = elem
    
    def belongsTo(self, elem: Estado.State):
        if(elem == None):
            return False
        
        if elem.getName() in self.individuals:
            return True

        return False

    def clone(self):
        newSet = StateSet()
        for key in self.individuals:
            stat = self.individuals[key]
            newSet.include(stat)
        return newSet
    
    def union(self, elem):
        newStateSet = StateSet()
        newStateSet = self.clone()
        for key in elem.individuals:
            state = elem.individuals[key]
            if(not newStateSet.belongsTo(state)):
                newStateSet.include(state)
                
        return newStateSet
    
    def intersection(self, elem):
        newStateSet = StateSet()
        for key in elem.individuals:
            state = elem.individuals[key]
            if(self.belongsTo(state)):
                newStateSet.include(state)
        return newStateSet
            
    def __eq__(self, __value: object) -> bool:
        if(self == None and __value == None):
            return True
        if(__value == None):
            return False
        newStateSet: StateSet = __value.clone()
        for key in newStateSet.individuals:
            state = newStateSet.individuals[key]
            if(not self.belongsTo(state)):
                return False
        
        newStateSet = self.clone()
        for key in newStateSet.individuals:
            state = newStateSet.individuals[key]
            if(not __value.belongsTo(state)):
                return False
        
        return True

    def __ne__(self, __value: object) -> bool:
        if(self == None and __value == None):
            return False
        if(__value == None):
            return True
        newStateSet: StateSet = __value.clone()
        for key in newStateSet.individuals:
            state = newStateSet.individuals[key]
            if(not self.belongsTo(state)):
                return True
        
        newStateSet = self.clone()
        for key in newStateSet.individuals:
            state = newStateSet.individuals[key]
            if(not __value.belongsTo(state)):
                return True
        
        return False
    
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
    
    def __len__(self):
        return len(self.individuals)
        