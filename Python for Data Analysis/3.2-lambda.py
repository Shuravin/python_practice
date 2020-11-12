# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:52:13 2020

@author: pauls
"""

def short_function(x):
    return x * 2

equiv_anon = lambda x: x * 2

power = lambda x: x ** 3

def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [5, 2, 7, 12, 111]

print(apply_to_list(ints, lambda x: x + 20))