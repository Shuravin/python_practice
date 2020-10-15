# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

fullname = str(input("Enter your first and last name (e.g. John Doe): "))
namelist = fullname.split(sep=" ")
print(namelist[1], namelist[0])