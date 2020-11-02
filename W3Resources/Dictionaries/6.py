# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


def create_dic(number):
    result = {}
    i = 0
    while i <= number:
        result.update({i: i * i})
        i += 1
    print(result)


create_dic(10)