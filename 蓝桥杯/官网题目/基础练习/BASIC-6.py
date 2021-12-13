while True:
    try:
        n = int(input())
        num = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(n):
                if j == 0:
                    num[i][j] == 1
                else:
                    num[i][j] == num[i-1][j-1]+num[i-1][j]

        for i in range(n):
            for j in range(n):
                if num[i][j] != 0:
                    print(num[i][j], end=' ')
            print()

    except:
        break