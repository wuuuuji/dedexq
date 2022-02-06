import heapq


def heapsort(iterable):
    h = []
    for data in iterable:
        heapq.heappush(h, data)
    return [heapq.heappop(h) for i in range(len(h))]


h = [10, 21, 5, 9, 13, 28, 3]
print("排序前 ", h)
print("排序后 ", heapsort(h))
