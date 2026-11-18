def is_palindrome(n):
   revn = 0
   pn = n
   while n > 0:
       r = n % 10
       revn = revn * 10 + r
       n = n // 10
   if pn == revn:
       return True
   else:
       return False
a = int(input())
b = int(input())
count = 0
for i in range(a, b+1):
   if is_palindrome(i):
       print(i, end = ' ')
       count += 1
if count == 0:
    print("Нет палиндромов")