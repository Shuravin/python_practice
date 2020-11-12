# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:59:16 2020

@author: pauls
"""

def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n+1):
        yield i ** 2
        
gen = squares(10)

def cubes(n=10):
    print('Generating cubes from 1 to {0}'.format(n ** 3))
    for i in range(1, n+1):
        yield i ** 3
        
gen2 = cubes(10)

gen3 = (x ** 2 for x in range(100))
for x in gen3:
    print(x, end = " ")