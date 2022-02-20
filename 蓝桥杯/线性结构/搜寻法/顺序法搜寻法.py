def sequential_search(nList):
    for i in range(len(nList)):
        if nList[i] == key:
            return i
    return -1


data = [6, 1, 5, 7, 3, 9, 4, 2, 8]
key = eval(input("请输入搜寻值 : "))
index = sequential_search(data)
if index != -1:
    print("在 %d 索引位置找到了共找了 %d 次" % (index, (index + 1)))
else:
    print("查无此搜寻号码")
