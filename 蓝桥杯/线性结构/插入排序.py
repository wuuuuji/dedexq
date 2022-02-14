def insertion_sort(nList):
    """插入排序"""
    n = len(nList)
    if n == 1:      # 只有1个数据
        print("第 %d 次循环排序" % n, nList)
        return nList
    print("第 1 次循环排序 : ", nList)
    for i in range(1, n):   # 循环
        for j in range(i, 0, -1):
            if nList[j] < nList[j-1]:
                nList[j], nList[j-1] = nList[j-1], nList[j]
            else:
                break
        print("第 %d 次循环排序 : " % (i+1), nList)
    return nList


data = [6, 1, 5, 7, 3]
print("原始列表 : ", data)
print("排序结果 : ", insertion_sort(data))