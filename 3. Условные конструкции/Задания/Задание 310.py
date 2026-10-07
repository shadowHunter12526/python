k = int(input()) #вместимость
m = int(input()) #минут на ОДНУ сторону
n = int(input()) #всего котлет
time = 0
if k >= n:
    time = (2*m)*n # в - 3, к - 2, м - 5 => 2 котлеты = 20 минут
elif k < n:
    time = (2*m)*k * (n // k)
print(time)