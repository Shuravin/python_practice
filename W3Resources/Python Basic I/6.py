# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

input = str(input("Enter sequence of numbers through comma: "))
result = input.split(sep=", ")
print(list(result))
print(tuple(result))