# 5. Write a Python program to iterate over dictionaries using for loops.

mydict = {
    "name": "John",
    "lname": "Doe",
    "age": 28,
    "gender": "male",
    "job": "pizza maker"
}


def dict_loop(dict):
    for x in dict:
        print(f"The value of '{x}' is '{dict[x]}'")


dict_loop(mydict)