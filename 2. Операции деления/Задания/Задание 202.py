num = int(input()) # номер урока
t = 540 #минимум - 9:00 - 540 минут
longbreak = 15 # после четного
shortbreak = 5 # после нечетного
if num % 2 == 0:
    t = t + 45 * num + (5 * num//2) + (15 * ((num//2) - 1))
    h = t // 60
    m = t % 60
    print(f'{h} {m}')
else:
    t = t + 45 * num + (5 * ((num-1)//2)) + (15 * (num//2))
    h = t // 60
    m = t % 60
    print(f'{h} {m}')
