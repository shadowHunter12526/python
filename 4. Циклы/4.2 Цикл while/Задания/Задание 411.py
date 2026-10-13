m = 0
count = 1

while (n := int(input())) != 0:
    if m < n:
        m = n
        count = 1
    elif m == n:
        count+=1
print(count)