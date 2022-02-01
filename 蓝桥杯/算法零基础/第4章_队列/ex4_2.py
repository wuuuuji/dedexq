class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)
        print("成功插入 {} 至队列".format(data))

    def size(self):
        return len(self.queue)

    def dequeue(self):



q = Queue()
a = ['汉堡', '薯条', '可乐']
for i in a:
    q.enqueue(i)
print("队列输出")
