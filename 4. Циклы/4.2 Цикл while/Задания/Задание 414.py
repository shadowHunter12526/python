equal = 0
cn = 0
l = 1
while (n := int(input())) != 0:
    if cn == n:
        l+=1
    else:
        cn = n
        l = 1
    if equal < l:
        equal = l
print(equal)