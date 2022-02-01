def factorial(n):
    global fact
    """计算n的阶层，n必须是正整数"""
    if n == 1:
        print("factorial(%d)调用前 %d! = %d" % (n, n, fact))
        print("到达递归条件终止 n=1")
        fact = 1
        print("factorial(%d)返回后 %d! = %d" % (n, n, fact))
        return fact
    else:
        print("factorial(%d)调用前 %d! = %d" % (n, n, fact))
        fact = n * factorial(n-1)
        print("factorial(%d)返回后 %d! = %d" % (n, n, fact))
        return fact


fact = 0
N = eval(input("请输入阶层数: "))
print(N, " 的阶层结果是 = ", factorial(N))