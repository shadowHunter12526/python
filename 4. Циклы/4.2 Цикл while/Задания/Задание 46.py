a = int(input())
b = int(input())
while a != b:
    if a % 2 == 0 and a > b and a // 2 >= b:
        a //= 2
        print(":2")
    elif a > b:
        a -= 1
        print("-1")