m = 0
p = m
while (n := int(input())) != 0:
    if m < n:
        p = m
        m = n
    elif p < n:
        p = n
print(p)
