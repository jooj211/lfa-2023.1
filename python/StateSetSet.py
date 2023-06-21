from ConjuntoEstados import StateSet

class StateStateSet: 
    def __init__(self) -> None:
        self.individuals = set()
        
    def isEmpty(self) -> bool:
        return len(self.individuals) == 0
    
    def clear(self):
        self.individuals.clear()
        
    def include(self, stateSet: StateSet):
        self.individuals.add(stateSet)
        
    def includes(self, stateSet: StateSet) -> bool:
        if stateSet in self.individuals:
            return True
        return False
    
    def union(self, stateSetSet):
        newStateSetSet = self.clone()
        for item in stateSetSet.individuals:
            if(not newStateSetSet.includes(item)):
                newStateSetSet.include(item.clone())
        return newStateSetSet
    
    def intersection(self, stateSetSet):
        newStateSet = StateStateSet()
        for item in self.individuals:
            if(stateSetSet.includes(item)):
                newStateSet.include(item.clone())
                
        return newStateSet
        
    
    def clone(self):
        newStateSetSet = StateStateSet()
        for item in self.individuals:
            newStateSetSet.include(item)
        return newStateSetSet
    
    def __eq__(self, __value: object) -> bool:
        return self.individuals == __value.individuals
    
    def internalUnion(self):
        stateSet = StateSet()
        for item in self.individuals:
            stateSet.union(item)
        return stateSet
        
    