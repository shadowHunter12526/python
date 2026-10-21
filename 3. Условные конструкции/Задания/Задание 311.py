n = int(input())

match n // 100:
    case 1:
        print("сто", end="")
    case 2:
        print("двести", end="")
    case 3:
        print("триста", end="")
    case 4:
        print("четыреста", end="")
    case 5:
        print("пятьсот", end="")
    case 6:
        print("шестьсот", end="")
    case 7:
        print("семьсот", end="")
    case 8:
        print("восемьсот", end="")
    case 9:
        print("девятьсот", end="")
if n // 10 % 10 != 1:
    match n // 10 % 10:
        case 2:
            print(" двадцать", end="")
        case 3:
            print(" тридцать", end="")
        case 4:
            print(" сорок", end="")
        case 5:
            print(" пятьдесят", end="")
        case 6:
            print(" шестьдесят", end="")
        case 7:
            print(" семьдесят", end="")
        case 8:
            print(" восемьдесят", end="")
        case 9:
            print(" девяносто", end="")
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
