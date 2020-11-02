# 2. Write a Python script to add a key to a dictionary. Go to the editor

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

mydict = {0: 10, 1: 20}


def add_key(dict):
    dict.update({2: 30})
    print(dict)


add_key(mydict)