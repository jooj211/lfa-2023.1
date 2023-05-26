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
    

state_set_intersection_1_2 = state_set_1.intersection(state_set_2)

assert len(state_set_intersection_1_2) == len(state_set_1)

names_2 = ["ka", "kb", "kc", "kd"]
state_list = []
state_set_3 = ConjuntoEstados.StateSet()
state_set_4 = ConjuntoEstados.StateSet()

for i in range(4):
    stat = Estado.State(names_2[i])
    state_list.append(stat)
    

for i in range(3):
    state_set_3.include(state_list[i])
    state_set_4.include(state_list[i + 1])
    
state_set_intersection_3_4 = state_set_3.intersection(state_set_4)

assert len(state_set_intersection_3_4) == 2