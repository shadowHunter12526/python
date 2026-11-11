def to_bin(num):
    if num < 2:
        print(num, end='')
    else:
        to_bin(num // 2)
        print(num % 2, end='')
a = int(input())
to_bin(a)
