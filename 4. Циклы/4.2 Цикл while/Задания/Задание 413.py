m = 0
c = 1
num1 = 0
num2 = 0
while (n := int(input())) != 0:
    if n > m:
        num1 = c
        num2 = c
        m = n
    elif m == n:
        num2 = c
    c += 1
print(num1, num2)
