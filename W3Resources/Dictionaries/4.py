# 4. Write a Python script to check whether a given key already exists in a dictionary.

mydict = {
    "name": "John",
    "lname": "Doe",
    "age": 28,
    "gender": "male",
    "job": "pizza maker"
}


def contains_key(dict, key):
    keys = list(dict.keys())
    try:
        keys.index(key)
    except ValueError:
        print(f"Dictionary DOESN'T contain key {key}")
    else:
        print(f"Dictionary contains key {key}")


contains_key(mydict, "gender")