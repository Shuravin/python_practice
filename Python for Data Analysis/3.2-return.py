# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:43:07 2020

@author: pauls
"""

def myfunc():
    a = 1
    b = 8
    c = 1
    d = 2
    return a, b, c, d

one, two, three, four = myfunc()

print(f"Napoleon's war with Russian Empire was in {one}{two}{three}{four}")