def selection_sort(nList):
    for i in range(len(nList) - 1):
        index = 1  # 最小值的索引
        for j in range(i + 1, len(nList)):  # 找最小值的索引
            if nList[index] > nList[j]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass  # 不更改
        else:
            nList[i], nList[index] = nList[index], nList[i]
        print("第 %d 次循环排序" % (i + 1), nList)
    return nList


data = [6, 1, 5, 7, 3]
print("原始列表 : ", data)
print("排序结果 : ", selection_sort(data))