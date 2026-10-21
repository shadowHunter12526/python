import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Кол-во простых чисел: "))
a = 2
count = 0
while count < num:
    if is_prime(a):
        print(a)
        count += 1
    a += 1
