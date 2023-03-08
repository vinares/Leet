import numpy as np
import itertools
from functools import lru_cache

def checkType(func, a, b):
    def wrapper_check_type():
        if not isinstance(a, int) and not isinstance(a, float):
            assert("Your first input should be a number.")
        if not isinstance(b, int) and not isinstance(b, float):
            assert("Your second input should be a number.")
        func(a, b)
    return wrapper_check_type

class OPERATION:
    def __init__(self) -> None:
        self.result = []
        self.operations = {'add': 1, 'mul': 2, 'div':3}

    @checkType
    def add(self, a, b):
        self.result.append((self.operations['add'], a, b, a+b))
       
    @checkType 
    def multiply(self, a, b):
        self.checkType(a, b)
        self.result.append((self.operations['mul'], a, b, a*b))
    
    @checkType
    def division(self, a, b):
        if b == 0:
            assert("The divident is zero.")
        self.result.append((self.operations['div'], a, b, a/b))

op = OPERATION()
print(op.add('a', 1))



def func1(a, b):
    return 'abc'

def func2(a, b):
    return 'de'


num1 = ['a', 'b', 'c']
num2 = [1, 2, 3]
num3 = [func1, func2]

answer = [(x, y, z) for x in num1 for y in num2 for z in num3]
#print(answer)




for x, y, z in answer:
    print(z(x, y))




