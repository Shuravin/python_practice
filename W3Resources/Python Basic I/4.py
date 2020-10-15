# Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

import math
radius = float(input("Enter the circle radius: "))


def area(r):
    return math.pi * (r**2)


print(area(radius))