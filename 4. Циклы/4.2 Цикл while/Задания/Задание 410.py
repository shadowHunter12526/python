m = 0

while (n := int(input())) != 0:
    if m < n:
        m = n
    if n == 0:
        break
print(m)