# random 함수
# from importlib.metadata import packages_distributions
# import numbers
import random #from random import *

# print(random.choice(range(1, 7))) #주사위

# lottery 
numbers = list(range(1, 46))
lottery = [ ] #list

for i in range(6):
    lottery.append(random.choice(numbers))

print(lottery)