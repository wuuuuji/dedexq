def selection_sort(nLst):
    ''' 选择排序 '''
    for i in range(len(nLst) - 1):
        index = i  # 最小值的索引
        for j in range(i + 1, len(nLst)):  # 找最小值的索引
            if nLst[index][2] < nLst[j][2]:
                index = j
        if i == index:  # 如果目前索引是最小值索引
            pass  # 不更动
        else:
            nLst[i], nLst[index] = nLst[index], nLst[i]  # 资料对调
    return nLst


music = [('李宗盛', '山丘', 24740000),
         ('赵传', '我是一只小小鸟', 8310000),
         ('五佰', '挪威的森林', 34130000),
         ('林忆莲', '听说爱情回来过', 12710000)
         ]

print("YouTube点播排行")
selection_sort(music)
for i in range(len(music)):
    print("{}:{} {} -- 点播次数 {}".format(i + 1, music[i][0], music[i][1], music[i][2]))