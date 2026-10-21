equal = 0
cn = 0
length = 1
while (n := int(input())) != 0:
    if cn == n:
        length += 1
    else:
        cn = n
        length = 1
    if equal < length:
        equal = length
print(equal)
