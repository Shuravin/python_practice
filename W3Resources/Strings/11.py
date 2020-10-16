# 11. Write a Python program to remove the characters which have odd index values of a given string

s = input("Type your sentence: ")
result = ""
for char in range(0, len(s)):
    # print(s[char])
    if char % 2 != 0:
        result = result + s[char]

print(result)
