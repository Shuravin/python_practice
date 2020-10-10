s = "dksbjabcdefgdbfuiebifwweubf"

resarray = []

for start in range(0, len(s)-1):
    result = s[start]
    for n in range(start, len(s)-1):
        if s[n+1] > s[n]:
            result += s[n+1]
        else:
            resarray.append(result) 
            break
    
resarray.sort()

print("Longest substring in alphabetical order is", resarray[0])

        

