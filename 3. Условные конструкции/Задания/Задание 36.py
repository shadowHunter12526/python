a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    h = max(a, b, c)
    c1 = min(a, b, c)
    c2 = (a + b + c) - (h + c1)
    if c1**2 + c2**2 == h**2:
        print("Прямоугольный")
    elif c1**2 + c2**2 > h**2:
        print("Остроугольный")
    elif c1**2 + c2**2 < h**2:
        print("Тупоугольный")
else:
    print("Не существует")