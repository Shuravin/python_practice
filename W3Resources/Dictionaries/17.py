# 17. Write a Python program to remove duplicates from Dictionary.

mydict = {
    "name": "John",
    "lname": "Doe",
    "age": 28,
    "gender": "male",
    "gender": "male",
    "gender": "female",
    "gender": "male",
    "job": "pizza maker"
}


def remove_dupl(dict):
    result = {}

    for key, value in dict.items():
        if value not in result.values():
            result[key] = value

    print(result)


remove_dupl(mydict)

# print(mydict.get(1))