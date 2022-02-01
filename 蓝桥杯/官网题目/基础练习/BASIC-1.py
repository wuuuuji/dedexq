y = int(input())
if 1990 <= y <= 2050:
    if (y % 4) == 0:
        if (y % 400) == 0 or (y % 100) != 0:
            print("yes")
        else:
            print("no")
    else:
        print("no")
