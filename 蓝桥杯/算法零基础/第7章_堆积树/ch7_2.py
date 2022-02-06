import heapq

h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("插入前 h = ", h)
heapq.heappush(h, 11)
print("第一次插入后 h = ", h)
heapq.heappush(h, 2)
print("第二次插入后 h = ", h)