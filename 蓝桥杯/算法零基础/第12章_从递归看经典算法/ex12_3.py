def myfib(n: int):
    if n == 1:
        return 1
    else:
        return myfib(n - 1) + 1.0 / n


n = int(input("请输入整数 : "))
i: int
for i in range(1, n+1):
    print("f(%d) = " % i, myfib(i))