# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:51:59 2020

@author: pauls
"""

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("fivethirtyeight")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)
# ax.scatter(2, 4, s = 200)

# set chart title and label axes
ax.set_title("Squares", fontsize = 18)
ax.set_xlabel("Value", fontsize = 16)
ax.set_ylabel("Square of Value", fontsize = 16)

# set size of tick labels
ax.tick_params(axis = "both", which = "major", labelsize = 14)

# Set the range of each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()