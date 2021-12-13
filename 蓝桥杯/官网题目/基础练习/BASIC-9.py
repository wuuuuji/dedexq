n = int(input())
if 1 <= n <= 54:
    if n % 2 == 0:
        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 10):
                    if i + j + k == int(n / 2):
                        a= "{0}{1}{2}{2}{1}{0}".format(i, j, k)
                        print(int(a))

    else:
        for i in range(1, 10):
            for j in range(0, 10):
                if 0 <= (n - 2*i - 2*j) <= 9:
                    a = "{0}{1}{2}{1}{0}".format(i, j, n - 2*i - 2*j)
                    print(int(a))


n = int(input(''))
x = []
for i in range(100, 1000):
    if sum(map(int, str(i) + (str(i)[:2])[::-1])) == n:
        x.append(str(i) + (str(i)[:2])[::-1])
    if sum(map(int, str(i) + str(i)[::-1])) == n:
        x.append(str(i) + str(i)[::-1])
for j in sorted(map(int, x)):
    print(j)