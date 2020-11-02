# 12. Write a Python program to remove a key from a dictionary.

mydict = {
    "name": "John",
    "lname": "Doe",
    "age": 28,
    "gender": "male",
    "job": "pizza maker"
}


def remove_key(dict, key):
    dict.pop(key)
    return dict


remove_key(mydict, "age")
print(mydict)