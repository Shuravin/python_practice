# 12. Write a Python program to count the occurrences of each word in a given sentence.

s = input("Type your sentence: ")
s_list = s.split(sep=" ")

for word in s_list:
    print(word, "occurs", s_list.count(word), "times.")
