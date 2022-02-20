from array import *

x = []
print("数组内容如下：")
while len(x) < 6:
    x.append(input())

while True:
    a = eval(input("请输入欲删除的索引"))
    if len(x) < a < 0:
        print("输入错误")
    else:
        del x[a]
        for i in x:
            print(i)
        break
