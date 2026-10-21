def is_perfect_number(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n


a = 1
count = 0
num = int(input())
while count < num:
    if is_perfect_number(a):
        print(a, end=' ')
        count += 1
    a += 1