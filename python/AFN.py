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
                 initial_state: State = State(""), 
                 final_states: StateSet = StateSet()) -> None:
        self.symbols = symbols.clone()
        self.states = states.clone()
        self.program_function = program_function.clone()
        self.initial_state = initial_state
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
    
    def toXML(self, filename: str):
        final_str = "<AFD>\n\t<simbolos>"
        for symbol in self.symbols.individuals:
            final_str += "\n\t\t<elemento valor=\""+str(symbol)+"\"/>"
        final_str += "\n\t</simbolos>"
        final_str += "\n\t<estados>"
        for state in self.states.individuals:
            final_str += "\n\t\t<elemento valor=\""+str(state)+"\"/>"
        final_str += "\n\t</estados>"
        final_str += "\n\t<estadosFinais>"
        for state in self.final_states.individuals:
            final_str += "\n\t\t<elemento valor=\""+str(state)+"\"/>"
        final_str += "\n\t</estadosFinais>"
        final_str += "\n\t<funcaoPrograma>"
        for tmp in self.program_function.individuals:
            final_str += tmp.parse_in_elements()
        final_str += "\n\t</funcaoPrograma>"
        final_str += "\n\t<estadoInicial valor=\"" + self.initial_state.name + "\"/>"
        
        final_str += "\n</AFD>"
        print(final_str)
    
    def from_xml(self, filename: str):
        tree = ET.parse(filename)
        root = tree.getroot()  
        symbols_tag = root.find("simbolos")
        symbols = symbols_tag.findall("elemento")
        for symbol in symbols:
            value = symbol.get("valor")
            self.symbols.include(Symbol(value))
            
        states_tag = root.find("estados")
        states = states_tag.findall("elemento")
        for state in states:
            value = state.get("valor")
            self.states.include(State(value))
            
        final_states_tag = root.find("estadosFinais")
        states = final_states_tag.findall("elemento")
        for state in states:
            value = state.get("valor")
            self.final_states.include(State(value))
            
        initial_state = root.find("estadoInicial")
        initial = initial_state.get("valor")
        self.initial_state = State(initial)
        dic:NonDeterministicTransition = {}
        program_function = root.find("funcaoPrograma")
        states = program_function.findall("elemento")
        for state in states:
            origin = state.get("origem")
            origin_s = State(origin)
            symbol = state.get("simbolo")
            symbol_s = Symbol(symbol)
            key = origin + symbol
            if key in dic:
                destiny = state.get("destino")
                destiny_s = State(destiny)
                dic[key].destiny.include(destiny_s)
            else:
                state_s = StateSet()
                destiny = state.get("destino")
                destiny_s = State(destiny)
                state_s.include(destiny_s)
                dic[key] = NonDeterministicTransition(origin_s, state_s, symbol_s)
        program = NonDeterministicTransitionSet()
        for key in dic:
            program.include(dic[key])
        self.program_function = program
        
    def p(self, state: State, symbol: Symbol) -> StateSet:
        fp = self.program_function
        list_fp = list(fp.individuals)
        destiny = StateSet()
        for tmp in list_fp:
            if(tmp.origin == state and tmp.symbol == symbol):
                destiny.include(tmp.destiny)
            
        return destiny

    def pe(self, state: State, word: str) -> StateSet:
        destiny = StateSet()
        index = 0
        while(index < len(word)):
            symbol = Symbol(word[index])
            tmpStateSet = self.p(state, symbol)
            for state in tmpStateSet.individuals:
                destiny.include(state)
            index += 1
            
        return destiny

