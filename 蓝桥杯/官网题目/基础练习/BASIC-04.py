def main():
    n = int(input())
    F1 = 1
    F2 = 1
    F3 = 0
    if n >= 3:
        for i in range(3, n+1):
            F3 = F1 + F2
            F1 = F2
            if F3 > 10007:
                F3 %= 10007
            F2 = F3
        print(F3 % 10007)
    else:
        print(1)

main()