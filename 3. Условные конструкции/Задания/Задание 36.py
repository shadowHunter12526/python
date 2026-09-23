a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    if a**2 + b**2 == c**2:
        print("Прямоугольный")
    elif a**2 + b**2 > c**2:
        print("Остроугольный")
    elif a**2 + b**2 < c**2:
        print("Тупоугольный")
else:
    print("Не существует")