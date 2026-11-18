def is_armstrong(n):
    if n <= 0:
        return False
    t = n
    d1 = 0
    while t > 0:
        d1 += 1
        t //= 10
    all = 0
    t = n
    while t > 0:
        d2 = t % 10
        all += d2 ** d1
        t //= 10
    return all == n
a = int(input())
b = int(input())
count = 0
for i in range(a, b + 1):
    if is_armstrong(i):
        print(i, end = ' ')
        count += 1
if count == 0:
    print("Нет чисел Армстронга")