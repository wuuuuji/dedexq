class HeapTree():
    def __init__(self):
        self.heap = []      # 堆积树列表
        self.size = 0       # 推积树列表元素个数

    def data_down(self, i):
        """ 如果节点值大于子节点值则数据域较小的值节点值对调 """
        while (i*2+2) <= self.size:     # 如果有子节点则继续
            mi = self.get_min_index(i)      # 取得较小值的子节点
            if self.heap[i] > self.heap[mi]:
                self.heap[i],  self.heap[mi] = self.heap[mi], self.heap[i]
            i = mi

    def get_min_index(self, i):
        """ 返回较小值的子节点索引 """
        if i * 2 + 2 >= self.size:      # 只有一个左节点
            return i * 2 + 1    # 传回左子节节点
        else:
            if self.heap[i * 2 + 1] < self.heap[i * 2 + 2]:     # 如果左子节小于右子节
                return i * 2 + 1        # True传回左子节索引
            else:
                return i * 2 + 2        # False传回右子节点索引

    def build_heap(self, mylist):
        """ 建立推积树 """
        i = (len(mylist) // 2) - 1      # 从有子节点的节点开始处理
        self.size = len(mylist)     # 得到列表个数
        self.heap = mylist      # 初步建立堆积树列表
        while (i >= 0):
            self.data_down(i)   # 从下层往上层处理
            i = i - 1

    def get_min(self):
        min_ret = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.heap.pop()
        self.data_down(0)
        return min_ret


data = ['Orange', 'Banana', 'Grape', 'Watermelon', 'Pineapple', 'Strawberry', 'Apple']
print("原始列表 : ", data)
obj = HeapTree()
obj.build_heap(data)    # 建立堆积树列表
print("执行后堆积树 : ", obj.heap)
sort_fruits = []
for i in range(len(data)):
    sort_fruits.append(obj.get_min())
print("排序结果 : ")
for fruit in sort_fruits:
    print(fruit)