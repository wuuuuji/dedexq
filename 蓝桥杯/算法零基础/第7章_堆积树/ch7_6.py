import heapq

h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("执行前 h = ", h)
x = heapq.heapreplace(h, 7)
print("取出值   = ", x)
print("执行后 h = ", h)