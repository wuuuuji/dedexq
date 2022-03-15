import random

def quick_sort(nLst):
    """ 快速排序法 """
    if len(nLst) <= 1:
        return nLst

    left = []       # 左边列表
    right = []      # 右边列表
    piv = []        # 基准列表
    pivot = random.choice(nLst)     # 随机设定脊椎
    for val in nLst:        # 分类
        if val == pivot:
            piv.append(val)     # 加入基准列表
        elif val < pivot:       # 如果小于基准
            left.append(val)    # 加入左边列表
        else:
            right.append(val)   # 加入右边列表
    return quick_sort(left) + piv + quick_sort(right)


data = [6, 1, 5, 7, 3, 9, 4, 2, 8]
print("原始列表 : ", data)
print("排序结果 : ", quick_sort(data))
