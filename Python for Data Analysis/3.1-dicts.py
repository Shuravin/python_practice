# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:12:41 2020

@author: pauls
"""

fnames = ["Maria", "Anna", "Helen", "Sarah", "Aglava"]
lnames = ["Doe", "Smith", "Atkinson", "Lovelace", "Balaklava"]

users = {}
for key, value in zip(fnames, lnames):
    users[key] = value
    
# # # # #

countries = ["USA", "England", "France", "China", "Russia", "Switzerland", "Germany", "Romania", "Czech Republic", "Bosnia", "Israel", "Egypt"]
by_letter = {}

for country in countries:
    letter = country[0]
    if letter not in by_letter.keys():
        by_letter[letter] = [country]
    else:
        by_letter[letter].append(country)
        
for word in countries:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)
        
print(by_letter)