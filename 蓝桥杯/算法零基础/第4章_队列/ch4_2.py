class Queue():
    """Queue队列"""
    def __init__(self):
        self.queue = []     # 使用列表模拟

    def enqueue(self, data):
        """data插入队列"""
        self.queue.insert(0, data)

    def size(self):
        """回传队列长度"""
        return len(self.queue)

    def dequeue(self):
        """读取队列"""
        if len(self.queue):
            return self.queue.pop()
        return "队列是空的"

q = Queue()
q.enqueue('Grape')
q.enqueue('Mango')
q.enqueue('Apple')
print('读取队列:', q.dequeue())
print('读取队列:', q.dequeue())
print('读取队列:', q.dequeue())
print('读取队列:', q.dequeue())
