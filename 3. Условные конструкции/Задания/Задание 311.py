n = int(input())

match n // 100:
    case 1:
        print(f"сто", end="")
    case 2:
        print(f"двести", end="")
    case 3:
        print(f"триста", end="")
    case 4:
        print(f"четыреста", end="")
    case 5:
        print(f"пятьсот", end="")
    case 6:
        print(f"шестьсот", end="")
    case 7:
        print(f"семьсот", end="")
    case 8:
        print(f"восемьсот", end="")
    case 9:
        print(f"девятьсот", end="")
if n // 10 % 10 != 1:
    match n // 10 % 10:
        case 2:
            print(f" двадцать", end="")
        case 3:
            print(f" тридцать", end="")
        case 4:
            print(f" сорок", end="")
        case 5:
            print(f" пятьдесят", end="")
        case 6:
            print("f шестьдесят", end="")
        case 7:
            print(f" семьдесят", end="")
        case 8:
            print(" восемьдесят", end="")
        case 9:
            print(f" девяносто", end="")
    match n % 10:
        case 1:
            print(" один")
        case 2:
            print(" два")
        case 3:
            print(" три")
        case 4:
            print(" четыре")
        case 5:
            print(" пять")
        case 6:
            print(" шесть")
        case 7:
            print(" семь")
        case 8:
            print(" восемь")
        case 9:
            print(" девять")
else:
    match n % 100:
        case 10:
            print(" десять")
        case 11:
            print(" одиннадцать")
        case 12:
            print(" двенадцать")
        case 13:
            print(" тринадцать")
        case 14:
            print(" четырнадцать")
        case 15:
            print(" пятнадцать")
        case 16:
            print(" шестнадцать")
        case 17:
            print(" семнадцать")
        case 18:
            print(" восемнадцать")
        case 19:
            print(" девятнадцать")
