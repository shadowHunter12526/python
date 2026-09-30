k = int(input())
m = int(input())
n = int(input())
if n > k:

     time = (k * (m * 2)) * (n % k)
else :
     time = n * m * 2
print(time)