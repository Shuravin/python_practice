# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:12:24 2020

@author: pauls
"""
import random

# Example dataset
data = {
        "area": [10, 12, 13, 15],
        "price": [150, 148, 152, 160]
        }

# Cost function
def cost_function(data):
    # generate test outputs
    output_dict = []
    for x in data["area"]:
        th0 = random.randrange(-100, 100, 1)
        th1 = random.randrange(-100, 100, 1)
        h = th0 + th1 * x
        output_dict.append(h)
    

    # cost function results dictionary
    cost_dict = {
        "th0": [],
        "th1": [],
        "j": []
        }
        
    # initial testing - loop throug output dict
    for i in range(0, len(data["price"])):
        
        if output_dict[i] > data["price"][i]:
            th0 = random.randrange(-100, th0, 1)
            th1 = random.randrange(-100, th1, 1)
        elif output_dict[i] < data["price"][i]:
            th0 = random.randrange(th0, 100, 1)
            th1 = random.randrange(th1, 100, 1)
        else:
            continue
        cost_dict["th0"].append(th0)
        cost_dict["th1"].append(th1)
        
        h = th0 + th1 * x
        output_dict.append(h)
        
        squares = 0
        for j in range(0, len(data["price"])):
            squares += (output_dict[j] - data["price"][j])**2
        j = 0.5 * (squares) / len(output_dict)
        cost_dict["j"].append(j)
        
    #Choose smallest j, th0 and th1
    res_j = cost_dict["j"].copy()
    res_j.sort()
    ind = cost_dict["j"].index(res_j[0])
    
    res_th0 = cost_dict["th0"][ind]
    res_th1 = cost_dict["th1"][ind]
    
    print(f"Smallest J: {res_j[0]}\nTh0: {res_th0}\nTh1: {res_th1}")
    
    
            
    
cost_function(data)