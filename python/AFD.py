from SymbolSet import SymbolSet
from ConjuntoEstados import StateSet
from DeterministicTransitionSet import DeterministicTransitionSet
from DeterministicTransition import DeterministicTransition
from Estado import State
from Symbol import Symbol

import xml.etree.ElementTree as ET

class AFD:
    def __init__(self, _symbols: SymbolSet = SymbolSet(), 
        _states: StateSet = StateSet(), 
        _program_function: DeterministicTransitionSet = 
        DeterministicTransitionSet(), _initial_state: State = State(""),
        _final_states: StateSet = StateSet()
        ) -> None:
        self.symbols = _symbols
        self.states = _states
        self.program_function = _program_function
        self.initial_state = _initial_state
        self.final_states = _final_states
        
    def clone(self):
        return AFD(self.symbols, 
                   self.states, self.program_function, 
                   self.initial_state, self.final_states)
        
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
        transition_set_list = list(self.program_function.individuals)
        for transition in transition_set_list:
            final_str += "\n\t\t<elemento origem=\"" + transition.origin.name + "\" simbolo=\"" + transition.symbol.symbol + "\" destino=\"" + transition.destiny.name + "\"/>"
        final_str += "\n\t</funcaoPrograma>"
        final_str += "\n\t<estadoInicial valor=\"" + self.initial_state.name + "\"/>"
        final_str += "\n</AFD>"
        file = open(filename, "w")
        file.write(final_str)
        file.close()    
        
    def from_xml(self, filename):
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
            
        program_function = root.find("funcaoPrograma")
        states = program_function.findall("elemento")
        for state in states:
            origin = state.get("origem")
            origin_s = State(origin)
            destiny = state.get("destino")
            destiny_s = State(destiny)
            symbol = state.get("simbolo")
            symbol_s = Symbol(symbol)
            dt = DeterministicTransition(origin_s, destiny_s, symbol_s)
            self.program_function.include(dt)
        
        initial_state = root.find("estadoInicial")
        initial = initial_state.get("valor")
        self.initial_state = State(initial)
        
    
    def p(self, state: State, symbol: Symbol) -> State:
        fp = self.program_function
        list_fp = list(fp.individuals)
        for tmp in list_fp:
            if(tmp.origin == state and tmp.symbol == symbol):
                return tmp.destiny
        
        return None
        
    def pe(self, state: State, word: str) -> State:
        tmpState = state
        index = 0
        while(index < len(word)):
            symbol = Symbol(word[index])
            tmpState = self.p(tmpState, symbol)
            if(tmpState == None):
                return None
            index += 1
        return tmpState
    
    def accept(self, word: str):
        return self.final_states.belongsTo(self.pe(self.initial_state, word))
        
    def __str__(self) -> str:
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
        transition_set_list = list(self.program_function.individuals)
        for transition in transition_set_list:
            final_str += "\n\t\t<elemento origem=\"" + transition.origin.name + "\" simbolo=\"" + transition.symbol.symbol + "\" destino=\"" + transition.destiny.name + "\"/>"
        final_str += "\n\t</funcaoPrograma>"
        final_str += "\n\t<estadoInicial valor=\"" + self.initial_state.name + "\"/>"
        final_str += "\n</AFD>"
        return final_str
        
    def getInitialState(self):
        return self.getInitialState()
    
    
        