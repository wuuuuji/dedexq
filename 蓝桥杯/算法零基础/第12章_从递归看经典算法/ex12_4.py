def myfib(n: int):
    if n == 1:
        return 0.5
    else:
        return myfib(n - 1) + n / (n + 1)


n = int(input("请输入整数 : "))
for i in range(1, n+1):
    print(f"f({i}) = ", myfib(i))
