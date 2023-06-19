from python import DeterministicTransition
from python import Estado
from python import Symbol
from python import DeterministicTransitionSet
from python.utils import random_str, make_random_transition


first_set = DeterministicTransitionSet.DeterministicTransitionSet()
second_set = DeterministicTransitionSet.DeterministicTransitionSet()

'''
Test union
'''

for i in range(30):
    transition = make_random_transition()
    transition_2 = make_random_transition()
    
    first_set.include(transition)
    second_set.include(transition_2)
    
union_set = first_set.union(second_set)

print(str(first_set))
print(str(second_set))    