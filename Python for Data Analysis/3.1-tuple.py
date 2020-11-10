# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:51:13 2020

@author: pauls
"""

tup = 4, 5, 6
#print(tup)

nested_tup = (4, 5, 6), (7, 8)
#print(nested_tup)

mylist = [1, 3, 5, 8]
#print(tuple(mylist))

tup = tuple("Hello world!")
#print(tup)

#for x in tup:
#    print(f"{x} grates you!")
    
an_tup = "foo", [2, 3], 38
an_tup[1].append(4)
#print(an_tup)

#a, b, c = an_tup

seq1 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
#for a, b, c in seq1:
#    print('a={0}, b={1}, c={2}'.format(a, b, c))

values = 1, 2, 3, 4, 5

a, b, *rest = values
a, b, *_ = values
print(_)