x = 123567894521
epsilon = 0.0001
numGuesses = 0
low = 1.0
high = x
ans = (high + low) / 2.0

while abs(ans * ans - x) >= epsilon:
    numGuesses += 1
    if ans * ans < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
        
print("Number of guesses: ", numGuesses)

print(str(ans), "is the square root of", str(x))