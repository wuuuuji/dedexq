def merge(left: list, right: list):
    """ 两数列合并 """
    output = []
    while left and right:
        if left[0] <= right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
    if left:
        output += left
    if right:
        output += right
    return output

def merge_sort(nList: list):
    """ 合并排序 """
    if len(nList) <= 1:     # 剩下一个或0个元素直接返回
        return nList
    mid = len(nList)//2     # 取中间索引
    # 切割(divide)数列
    left = nList[:mid]      # 取左半段
    right = nList[mid:]     # 取右半段
    # 处理左序列和右序列
    left = merge_sort(left)     # 左边排序
    right = merge_sort(right)   # 右边排序
    # 递归执行合并
    return merge(left, right)


data = [6, 1, 5, 7, 3, 9, 4]
print("原始列表 : ", data)
print("排序结果 : ", merge_sort(data))