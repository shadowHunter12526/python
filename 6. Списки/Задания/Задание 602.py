line = list(map(int, input().split()))
x = int(input())
pos = 1
for i in range(len(line)):
    if line[i] >= x:
        pos += 1
    else:
        break
print(pos)
