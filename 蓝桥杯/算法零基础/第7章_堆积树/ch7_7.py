import heapq

h = []
heapq.heappush(h, (100, '牛肉面'))
heapq.heappush(h, (60, '阳春面'))
heapq.heappush(h, (80, '肉丝面'))
heapq.heappush(h, (90, '大卤面'))
heapq.heappush(h, (70, '家常面'))
print(h)
print(heapq.heappop(h))