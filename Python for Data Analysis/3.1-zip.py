# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:07:27 2020

@author: pauls
"""

pitchers = [("John", "Doe"), ("Sarah", "Smith"), ("Vladimir", "Putin")]

fnames, lnames = zip(*pitchers)

print(fnames)
print(lnames)