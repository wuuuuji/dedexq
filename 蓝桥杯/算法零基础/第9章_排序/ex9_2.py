def selection_sort(nLst):
    """ 选择排序 """
    for i in range(len(nLst) - 1):
        index = i  # 最小值的索引
        for j in range(i + 1, len(nLst)):  # 找最小值的索引
            if nLst[index][1] < nLst[j][1]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass  # 不更动
        else:
            nLst[i], nLst[index] = nLst[index], nLst[i]  # 资料对调
    return nLst


language = [("Python", 98789),
            ("C", 56532),
            ("C#", 88721),
            ("Java", 90397),
            ("C++", 63122),
            ("PHP", 58000)
            ]

print("程序语言使用率排序")
selection_sort(language)
for i in range(len(language)):
    print("{}:{:7s}-- 使用次数 {}".format(i + 1, language[i][0], language[i][1]))