def max_num(n):
    if n >= 10:
        return max(n % 10, max_num(n // 10))
    else:
        return n
a = int(input())
print(max_num(a))