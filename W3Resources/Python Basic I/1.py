# 1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are

mystring = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
print(mystring)


def song(string):
    for char in string:
        if char == "T":
            print("\n", char, sep="", end="")
        elif char == "H":
            print("\n\t", char, sep="", end="")
        elif char == "U" or char == "L":
            print("\n\t\t", char, sep="", end="")
        else:
            print(char, sep="", end="")


song(mystring)