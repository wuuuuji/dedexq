def selection_sort(nLst):
    """ 选择排序 """
    for i in range(len(nLst) - 1):
        index = i  # 最小值的索引
        for j in range(i + 1, len(nLst)):  # 找最小值的索引
            if nLst[index][1] > nLst[j][1]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass  # 不更动
        else:
            nLst[i], nLst[index] = nLst[index], nLst[i]  # 资料对调
    return nLst


hotel = [("东方酒店", 3450),
         ("北京大饭店", 4200),
         ("喜来登酒店", 5000),
         ("文华酒店", 5200),
         ("君悦酒店", 5560),
         ]

print("北京酒店定价排序")
selection_sort(hotel)
for i in range(len(hotel)):
    print("{}:{:6s} -- {}".format(i + 1, hotel[i][0], hotel[i][1]))