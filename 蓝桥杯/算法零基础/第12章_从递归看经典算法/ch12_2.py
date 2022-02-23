def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i - 1) + fib(i-2)


n = eval(input("请输入斐波那契的数字 : "))
for i in range(n+1):
    print("n = {}, Fib({}）= {}".format(i, i, fib(i)))
