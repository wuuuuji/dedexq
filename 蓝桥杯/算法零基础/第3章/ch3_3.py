class Node():
    """节点"""

    def __init__(self, data=None):
        self.data = data  # 数组
        self.next = None  # 指标


class Linked_list():
    """链表"""

    def __init__(self):
        self.head = None  # 链表第一个节点

    def print_list(self):
        """打印链表"""

        ptr = self.head  # 指标指向链表第一个节点
        while ptr:
            print(ptr.data)  # 打印节点
            ptr = ptr.next  # 移动指标到下一个节点

    def begining(self, newdata):
        """在第一个节点前插入新节点"""
        new_node = Node(newdata)        # 建立新节点
        new_node.next = self.head       # 新节点指向旧的第1个节点
        self.head = new_node            # 更新链表的第一个节点

link = Linked_list()
link.head = Node(5)     # 节点1
n2 = Node(15)   # 节点2
n3 = Node(25)   # 节点3
link.head.next = n2     # 节点1指向节点2
n2.next = n3        # 节点2指向节点3
link.print_list()       # 打印链表link
print("新的链表")
link.begining(100)
link.print_list()       # 打印新链表link
