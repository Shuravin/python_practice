# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:06:35 2020

@author: pauls
"""
import bisect


a_list = [1, 2, 3, None]

tup = ("foo", "bar", "baz")

b_list = list(tup)

b_list[0] = "I hate everything"

r = list(range(0, 10, 2))

b_list.append("kozlina")

b_list.insert(2, "astrology")

#print("goblin" in b_list)

r.extend(b_list)

my_pets = [["Grant", "John", "Rick"], ["Kurt", "Syoma"], ["Aleister", "Chester"]]
new_list = []
for animals in my_pets:
    new_list.extend(animals)

pets = ["cat", "dog", "fish", "cow", "pigeon"]
pets.sort(key = len)

new_list = [12, 55, 22, 16, 1, 58, 98, 664, 531, 1]
print(f'Number 111 will be inserted in {bisect.bisect(new_list, 111)} position')
bisect.insort(new_list, 111)
print(new_list)