class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)
        print("成功插入 {} 至队列".format(data))

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue("Grape")
q.enqueue("Mango")
q.enqueue("Apple")
print("队列长度为:"+str(q.size()))