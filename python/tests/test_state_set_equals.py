from python import ConjuntoEstados
from python import Estado

import secrets
import string

state_set_1 = ConjuntoEstados.StateSet()
state_set_2 = ConjuntoEstados.StateSet()

for i in range(50):
    size = 40  # Tamanho da string desejada
    caracteres = string.ascii_letters + string.digits  # Letras maiúsculas, minúsculas e dígitos

    random_str = ''.join(secrets.choice(caracteres) for _ in range(size))
    state = Estado.State(random_str)
    state_set_1.include(state)
    state_set_2.include(state)
    
state_set_3 = ConjuntoEstados.StateSet()
for i in range(50):
    size = 40  # Tamanho da string desejada
    caracteres = string.ascii_letters + string.digits  # Letras maiúsculas, minúsculas e dígitos

    random_str = ''.join(secrets.choice(caracteres) for _ in range(size))
    state = Estado.State(random_str)
    state_set_3.include(state)
    

assert state_set_1 == state_set_2
assert state_set_3 != state_set_2