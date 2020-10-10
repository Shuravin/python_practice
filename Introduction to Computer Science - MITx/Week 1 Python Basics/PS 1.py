s = "dsfailewbafilweafi"

count = 0
index = 0
while index < len(s):
    if s[index] == "a":
        count += 1
    elif s[index] == "e": 
        count += 1
    elif s[index] == "i":
        count += 1
    elif s[index] == "o":
        count += 1
    elif s[index] == "u":
        count += 1
    else:
        count = count + 0
    index += 1
    
print("Number of vowels:", count)