def bubble_sort(nList):
    length = len(nList)
    for i in range(length-1):
        print("第 %d 次外圈排序" % (i + 1))
        for j in range(length - 1 - i):
            if nList[j] < nList[j + 1]:
                nList[j], nList[j + 1] = nList[j + 1], nList[j]
            print("第 %d 次内圈排序 : " % (j + 1), nList)
    return nList


data = [6, 1, 5, 7, 3]
print("原始列表 : ", data)
print("排序结果 : ", bubble_sort(data))