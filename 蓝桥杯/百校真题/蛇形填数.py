"""
如下图所示，小明用从 1 开始的正整数“蛇形”填充无限大的矩阵。
1  2  6  7  15 ...
3  5  8  14 ...
4  9  13 ...
10 12 ...
11 ...
...
容易看出矩阵第二行第二列中的数是 5。请你计算矩阵中第 20 行第 20 列的数是多少？
"""
x, y = eval(input("请输入 : "))
t = (max(x, y)-1)*2+1
a = [[0 for i in range(t)] for j in range(t)]
tem = 1
num = 1
a[0][0] = 1
while True:
    if a[x - 1][y -1 ] > 0:
        break
    if tem % 2 != 0:
        for i in range(tem+1):
            num += 1
            a[i][tem-i] = num
        tem += 1
    if tem % 2 == 0:
        for i in range(tem+1):
            num += 1
            a[tem-i][i] = num
        tem += 1

print(a[x - 1][y - 1])
