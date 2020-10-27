# 3. Write a Python program to get the largest number from a list.

# arr = str(input("Type several integers: "))
my_list = []


def input_list():
    i = False
    while i == False:
        answ = input(
            'Type a number and press enter. If you want to stop, type "stop" without parenthesis: ')
        if answ == "stop":
            i = True
        else:
            my_list.append(answ)


input_list()
print(my_list)

# def validate_list(array):
#     for x in array:
#         if x == " " or x == ",":
#             continue
#         else:
#             x = int(x)
#             my_list.append(x)


# validate_list(arr)


def max_number(array):
    array = sorted(array)
    print(array)
    print(array[-1])


max_number(my_list)
