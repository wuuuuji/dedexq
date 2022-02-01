class Node():
    """节点"""

    def __init__(self, data=None):
        self.data = data                # 数组
        self.next = None                # 指标


class Linked_list():
    """链表"""

    def __init__(self):
        self.head = None                # 链表第一个节点

    def print_list(self):
        """打印链表"""

        ptr = self.head                 # 指标指向链表第一个节点
        while ptr:
            print(ptr.data)             # 打印节点
            ptr = ptr.next              # 移动指标到下一个节点

    def begining(self, newdata):
        """在第一个节点前插入新节点"""
        new_node = Node(newdata)        # 建立新节点
        new_node.next = self.head       # 新节点指向旧的第1个节点
        self.head = new_node            # 更新链表的第一个节点

    def ending(self, newdata):
        """在链表末端插入新节点"""
        new_node = Node(newdata)        # 建立新节点
        if self.head is None:           # 判断是否为空链表
            self.head = new_node
            return
        last_ptr = self.head            # 设定最后指标是链表头部
        while last_ptr.next:            # 移动指标直到最后
            last_ptr = last_ptr.next
        last_ptr.next = new_node        # 将最后一个节点的

link = Linked_list()
link.head = Node(5)     # 节点1
n2 = Node(15)   # 节点2
n3 = Node(25)   # 节点3
link.head.next = n2     # 节点1指向节点2
n2.next = n3        # 节点2指向节点3
link.print_list()       # 打印链表link
print("新的链表")
link.ending(100)
link.print_list()       # 打印新链表link
