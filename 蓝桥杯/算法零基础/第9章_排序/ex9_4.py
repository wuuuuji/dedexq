def bubble_sort(nLst):
    length = len(nLst)
    for i in range(length - 1):
        print("第 %d 次外圈排序" % (i + 1))
        for j in range(length - 1 - i):
            if nLst[j] < nLst[j + 1]:
                nLst[j], nLst[j + 1] = nLst[j + 1], nLst[j]
            print("第 %d 次内圈排序 : " % (j + 1), nLst)
    return nLst


data = []
while True:
    val = input("请输入数值(Q或q代表输入结束) : ")
    if val == "Q" or val == "q":
        break
    data.append(int(val))
print("原始列表 : ", data)
print("排序结果 : ", bubble_sort(data))
