# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:20:31 2020

@author: pauls
"""

import random

x = [1, 2, 3]
y = [1, 4, 9]

def learning(inp, output):
    # List of thetas
    ths = [
           [],
           []
           ]
    
    # List of computed outputs
    hs = []
    
    # List of js
    js = []
    
    # Create 10 js
    for it in range(0, 10):
        # Working outputs
        w = []
        # Compute outputs
        for i in inp:
            th0, th1 = random.random(), random.random()
            ths[0].append(th0)
            ths[1].append(th1)
            h = th0 + th1 * i
            w.append(h)
            hs.append(h) # Add computed output to corresponded list
            
        # Compute j
        j = ((w[0]-y[0])**2+(w[1]-y[1])**2+(w[2]-y[2])**2) / 6
        js.append(j) # Add j to js list
        
    # Gradient Descent Algo
    alpha = 0.1
    gda = []
    gda_item = 0
    
    print(hs)
    

learning(x, y)
    
# I'm literally crying it's very hard for me :(