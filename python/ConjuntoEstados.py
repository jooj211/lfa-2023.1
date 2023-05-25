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
            
    def __eq__(self, __value: object) -> bool:
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
        