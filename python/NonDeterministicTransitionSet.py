from Estado import State
from ConjuntoEstados import StateSet
from Symbol import Symbol
from NonDeterministicTransition import NonDeterministicTransition


class NonDeterministicTransitionSet:
    def __init__(self) -> None:
        self.individuals = set()
        
    def isEmpty(self) -> bool:
        return len(self.individuals) == 0
    
    def include(self, element: NonDeterministicTransition):
        self.individuals.add(element)
        
    def includes(self, element: NonDeterministicTransition) -> bool:
        for tmp in self.individuals:
            if tmp == element:
                return True
        return False
    
    def union(self, ts):
        newSet = self.clone()
        for tmp in ts.individuals:
            if(not newSet.includes(tmp)):
                newSet.include(tmp.clone())
        return newSet
    
    def intersection(self, ts):
        newSet = NonDeterministicTransitionSet()
        for tmp in ts.individuals:
            if self.includes(tmp):
                newSet.include(tmp.clone())
                
        return newSet
    
    
    def __eq__(self, __value: object) -> bool:
        tmp = self.clone()
        for transition_tmp in tmp.individuals:
            if(not __value.includes(transition_tmp)):
                return False
        
        tmp = __value.clone()
        for transition_tmp in tmp.individuals:
            if(not self.includes(transition_tmp)):
                return False
        return True
    
    def __str__(self) -> str:
        final_str = "{"
        size = len(self.individuals)
        for tmp in self.individuals:
            size -= 1
            final_str += str(tmp)
            if size != 0:
                final_str += ','
                
        final_str += '}'
        return final_str
        
    def clone(self):
        newSet = NonDeterministicTransitionSet()
        for tmp in self.individuals:
            newSet.individuals.include(tmp.clone())
            
        return newSet