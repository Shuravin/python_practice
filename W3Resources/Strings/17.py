# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). Go to the editor
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

s = input("Type your sentence (at least 2 characters length): ")


def insert_end(string):
    end = string[-2:] * 4
    print(end)


insert_end(s)
