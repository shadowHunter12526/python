n = int(input())
if 11 <= n % 100 <= 14:
    print("грибов")
elif 2 >= n % 10 >= 4:
    print("гриба")
elif n % 10 == 1:
    print("гриб")
else:
    print("грибов")

"""
if 2 <= n % 10 <= 4 and not (12 <= n % 100 <= 14):
    print("гриба")
elif n % 10 == 1 and n % 100 != 11:
    print("гриб")
else:
    print("грибов")

"""