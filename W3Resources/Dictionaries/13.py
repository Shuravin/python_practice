# 13. Write a Python program to map two lists into a dictionary.

list1 = ["fname", "lname", "age", "gender", "job"]
list2 = ["John", "Doe", 28, "male", "pizza maker"]


def map_list(list1, list2):
    result = {}
    # Validation: check if lists lengths are equal
    if len(list1) != len(list2):
        print("Can't create dictionary: lists are not equal")
    else:
        # Dict creation
        i = 0
        while i < len(list1):
            result.update({list1[i]: list2[i]})
            i += 1
        print(result)


map_list(list1, list2)
