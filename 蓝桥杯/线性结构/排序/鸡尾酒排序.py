def cocktail_sort(nList):
    """鸡尾酒排序"""
    n = len(nList)
    is_sored = True
    start = 0  # 前端索引
    end = n - 1  # 后端索引
    while is_sored:
        is_sored = False  # 重置是否排序完成
        for i in range(start, end):  # 往后比较
            if nList[i] > nList[i + 1]:
                nList[i], nList[i + 1] = nList[i + 1], nList[i]
                is_sored = True
        print("往后排序过程 : ", nList)
        if not is_sored:  # 如果没有交换就结束
            break

        end = end - 1  # 末端索引左移一个索引
        for i in range(end - 1, start - 1, -1):  # 往左移动
            if nList[i] > nList[i + 1]:
                nList[i], nList[i + 1] = nList[i + 1], nList[i]
                is_sored = True
        start = start + 1     # 末端索引右移一个索引
        print("往前排序过程 : ", nList)
    return nList


data = [6, 1, 5, 7, 3]
print("原始列表 : ", data)
print("排序结果 : ", cocktail_sort(data))