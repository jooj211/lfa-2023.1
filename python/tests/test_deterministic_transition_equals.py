from python import DeterministicTransition
from python import Estado
from python import Symbol

state_1 = Estado.State("q1")
state_2 = Estado.State("q2")
symbol = Symbol.Symbol("a")


det_1 = DeterministicTransition.DeterministicTransition(state_1, state_2, symbol)
det_2 = DeterministicTransition.DeterministicTransition(state_1, state_2, symbol)

assert det_1 == det_2