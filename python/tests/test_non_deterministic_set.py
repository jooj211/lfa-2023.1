from python import NonDeterministicTransition
from python import Estado
from python import Symbol
from python import NonDeterministicTransitionSet
from python.utils import random_str, make_random_transition


first_set = NonDeterministicTransitionSet.NonDeterministicTransitionSet()
second_set = NonDeterministicTransitionSet.NonDeterministicTransitionSet()

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