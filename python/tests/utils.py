import secrets
import string
import DeterministicTransition
import DeterministicTransitionSet
import Symbol
import SymbolSet
import Estado
import ConjuntoEstados
import random

def random_str(_size):
    size = _size  # Tamanho da string desejada
    caracteres = string.ascii_letters + string.digits  # Letras maiúsculas, minúsculas e dígitos

    random_str = ''.join(secrets.choice(caracteres) for _ in range(size))
 
    return random_str
 

def make_random_transition():
    name_1 = random_str(1)
    name_2 = random_str(1)
    name_3 = random_str(1)
    state_1 = Estado.State(name_1)
    state_2 = Estado.State(name_2)
    symbol = Symbol.Symbol(name_3)
    ret = DeterministicTransition.DeterministicTransition(state_1, state_2, symbol)
    return ret

def make_random_symbol_set(size = 100):
    symbols = SymbolSet.SymbolSet()
    for i in range(size):
        symbol = Symbol.Symbol(random_str(1))
        symbols.include(symbol)
    return symbols

def make_random_state_set(size = 100):
    state_set = ConjuntoEstados.StateSet()
    for i in range(size):
        state = Estado.State(random_str(15))
        state_set.include(state)
        
    return state_set

def make_transition(states, symbol):
    id_1 = random.randint(0, 51)
    id_2 = random.randint(0, 51)
    