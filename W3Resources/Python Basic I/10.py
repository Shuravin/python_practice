# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

input = int(input("Enter an integer: "))
n1 = input
n2 = int(str(input) + str(input))
n3 = int(str(input) + str(input) + str(input))
print(n1 + n2 + n3)