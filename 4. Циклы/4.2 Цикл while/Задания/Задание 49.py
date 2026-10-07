sum = 0
count = 0
while (a := int(input())) != 0:   # моржовый оператор
    count += 1
    sum += a
print(sum / count)