from python import ConjuntoEstados
from python import Estado

import secrets
import string


state_set_1 = ConjuntoEstados.StateSet()
state_set_2 = ConjuntoEstados.StateSet()

names = []

for i in range(50):
    size = 40  # Tamanho da string desejada
    caracteres = string.ascii_letters + string.digits  # Letras maiúsculas, minúsculas e dígitos

    random_str = ''.join(secrets.choice(caracteres) for _ in range(size))
    state = Estado.State(random_str)
    state_set_1.include(state)
    state_set_2.include(state)
    names.append(random_str)
    
assert len(state_set_1) == 50