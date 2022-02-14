def selection_sort(nList):
    """选择排序"""
    for i in range(len(nList) - 1):
        index = 1  # 最小值的索引
        for j in range(i + 1, len(nList)):  # 找最小值的索引
            if nList[index] > nList[j]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass  # 不更改
        else:
            nList[i], nList[index] = nList[index], nList[i]
    return nList


car = ['honda', 'bmw', 'toyota', 'ford']
print("原始列表 : ", car)
print("使用selection_sort( )由小排到大")
selection_sort(car)
print("排序结果 : ", car)