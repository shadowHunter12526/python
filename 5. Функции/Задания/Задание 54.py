def sum_divisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum


n = int(input())
count = 0
for i in range(1, n + 1):
    a = sum_divisors(i)
    if i < a <= n and sum_divisors(a) == i:
        if count > 0:
            print(", ", end='')
        print(f"({i}, {a})", end='')
        count += 1
if count == 0:
    print("Нет дружественных чисел")
