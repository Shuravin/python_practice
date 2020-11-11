# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:43:49 2020

@author: pauls
"""

strings = ["a", "as", "bat", "car", "dove", "python"]

result = [x.upper() for x in strings if len(x) >= 2]

odds = [x for x in range(0, 100) if x % 2 != 0]

#unique_lengths = {len(x) for x in strings}
unique_lengths = set(map(len, strings))

# # # # # #

all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
            ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]

names_of_interest = []
for names in all_data:
    # enough_es = [name for name in names if name.count("e") >= 2]
    enough_as = [name for name in names if name.count("a") > 1]
    names_of_interest.extend(enough_as)
    
print(names_of_interest)