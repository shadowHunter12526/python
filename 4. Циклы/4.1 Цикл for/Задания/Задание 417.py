n = int(input())
count_z = 0
count_m = 0
count_p = 0
average_p = 0
for i in range(n):
    a = int(input())
    if a == 0:
        count_z += 1
    elif a > 0:
        count_p += 1
        average_p += a
    elif a < 0:
        count_m += 1
print("Нулей:", count_z)
print("Отрицательных:", count_m)
print(f"Среднее положительных: {average_p / count_p:.2f}")