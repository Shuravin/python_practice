# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:01:17 2020

@author: pauls
"""

mylist = ["cat", "dog", "fish"]
mapping = {}

for i, v in enumerate(mylist):
    mapping[v] = i
    

poe_classes = ["Witch", "Shadow", "Ranger", "Duelist", "Marauder", "Templar", "Scion"]
indexes = {}

for poeclass, ind in enumerate(poe_classes):
    indexes[ind] = poeclass
    
print(indexes)