s = eval(input().strip())

if s <= 2147483647:
    res_1 = hex(s)[2:].upper()
    print(res_1)