m = 0
c = 1
num1 = 0
num2 = 0
while (n := int(input())) != 0:
    c += 1
    if m < n:
        num1 = c-1
        m = n
    elif m == n:
        num2 = c-1
    if num1 > num2:
        num2 = num1
print(num1, num2)