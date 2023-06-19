from NonDeterministicTransitionSet import NonDeterministicTransitionSet
from NonDeterministicTransition import NonDeterministicTransition
from SymbolSet import SymbolSet
from Symbol import Symbol
from ConjuntoEstados import StateSet
from Estado import State

import xml.etree.ElementTree as ET

class AFN:
    def __init__(self, symbols: SymbolSet = SymbolSet(), 
                 states: StateSet = StateSet(),
                 program_function: NonDeterministicTransitionSet = NonDeterministicTransitionSet(),
                 initial_state: State = State(), 
                 final_states: StateSet = StateSet()) -> None:
        self.symbols = symbols.clone()
        self.states = states.clone()
        self.program_function = program_function.clone()
        self.initial_state = initial_state.clone()
        self.final_states = final_states.clone()
        
    def clone(self):
        return AFN(self.symbols, self.states, self.program_function,
                   self.initial_state, self.final_states)
        
    def __str__(self) -> str:
        final_str = "("
        final_str += str(self.symbols) + ","
        final_str += str(self.states) + ","
        final_str += str(self.program_function) + ","
        final_str += str(self.initial_state) + ","
        final_str += str(self.final_states)
        final_str += ")"
        return final_str
    
    def from_xml(self, filename: str):
        tree = ET.parse(filename)
        root = tree.getroot()  
        symbols_tag = root.find("simbolos")
        symbols = symbols_tag.findall("elemento")
        for symbol in symbols:
            value = symbol.get("valor")
            self.symbols.include(Symbol(value))