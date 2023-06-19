import DeterministicTransition

class DeterministicTransitionSet:
    def __init__(self) -> None:
        self.individuals = set()
    
    def isEmpty(self):
        if(len(self.individuals) == 0):
            return True
        return False

    def clear(self):
        self.individuals.clear()
    
    def include(self, transition: DeterministicTransition.DeterministicTransition):
        self.individuals.add(transition.clone())
        
    def includes(self, transition: DeterministicTransition.DeterministicTransition):
        for key in self.individuals:
            individual = key
            if(individual == transition):
                return True
        return False
    
    def union(self, c1):
        newSet = DeterministicTransitionSet()
        newSet = self.clone()
        for item in c1.individuals:
            newSet.include(item)
        return newSet
    
    def intersection(self, c1):
        newSet = DeterministicTransitionSet()
        for item in self.individuals:
            if(c1.includes(item)):
                newSet.include(item)
        return newSet
        
        
    def clone(self):
        newSet = DeterministicTransitionSet()
        for item in self.individuals:
            newSet.include(item)
        return newSet
    
    def __eq__(self, __value: object) -> bool:
        cmpSet = self.clone()
        for item in cmpSet.individuals:
            if(not __value.includes(item)):
                return False
        cmpSet = __value.clone()
        for item in cmpSet.individuals:
            if(not self.includes(item)):
                return False
            
        return True
    
    def __ne__(self, __value: object) -> bool:
        cmpSet = self.clone()
        for item in cmpSet.individuals:
            if(not __value.includes(item)):
                return True
        cmpSet = __value.clone()
        for item in cmpSet.individuals:
            if(not self.includes(item)):
                return True
            
        return False
    
    def __str__(self) -> str:
        ret_str = "{"
        ret_str_len = len(self.individuals)
        for item in self.individuals:
            ret_str_len -= 1
            ret_str += str(item)
            if(ret_str_len != 0):
                ret_str += ','
        ret_str += "}"
        return ret_str
            