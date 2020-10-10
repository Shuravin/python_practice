s = "doggydoggydoggydoggydoggydoggydoggy"

count = 0
start = 0
stop = 3
while stop <= len(s):
    if s[start:stop] == "dog":
        count += 1
    start += 1
    stop += 1

print("Number of times 'dog' occurs is", count)