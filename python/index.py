from utils import make_random_symbol_set
import SymbolSet
import Symbol
from Estado import State
from ConjuntoEstados import StateSet
from DeterministicTransition import DeterministicTransition
from DeterministicTransitionSet import DeterministicTransitionSet
from AFD import AFD


symbol_set = SymbolSet.SymbolSet()
symb = ["a", "b", "c"]
symbols = []

for i in symb:
    symbol = Symbol.Symbol(i)
    symbol_set.include(symbol)
    symbols.append(symbol)
    
_states = StateSet()
_final_state_set = StateSet()
states = []

stat = ["q1", "q2", "q3"]

for i in stat:
    state = State(i)
    _states.include(state)
    states.append(state)
    
    
transition_set = DeterministicTransitionSet()
transition_1 = DeterministicTransition(states[0], states[1], symbols[0])
transition_set.include(transition_1)
transition_1 = DeterministicTransition(states[1], states[1], symbols[1])
transition_set.include(transition_1)

_final_state_set.include(states[2])

afd = AFD(symbol_set, _states, transition_set, states[0], _final_state_set)

afd.toXML("hello.xml")