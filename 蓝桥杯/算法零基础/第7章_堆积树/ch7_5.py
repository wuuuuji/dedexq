import heapq

h = [10, 21, 5, 9, 13, 28, 3]
print("最大 3 个  : ", heapq.nlargest(3, h))
print("最小 3 个  : ", heapq.nsmallest(3, h))
print("原先数据集 : ",h)