n = int(input())
if 11 <= n % 100 <= 14:
    print("грибов")
elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
    print("гриба")
elif n % 10 == 1:
    print("гриб")
else:
    print("грибов")