class Node():
    """节点"""

    def __init__(self, data=None):
        self.data = data  # 数组
        self.next = None  # 指标


n1 = Node(5)  # 节点1
n2 = Node(15)   # 节点2
n3 = Node(25)   # 节点3
n1.next = n2
n2.next = n3
n3.next = n1
ptr = n1
counter = 1
while counter <= 6:
    print(ptr.data)
    ptr = ptr.next
    counter += 1
