num = int(input())
s = 0
while num >= 1:
    s += num % 10
    num = num // 10
print(s)
