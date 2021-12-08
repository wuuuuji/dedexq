class Node():
    """节点"""

    def __init__(self, data=None):
        self.data = data  # 数据
        self.next = None  # 向后指标
        self.previous = None  # 向前指标


class Double_linked_list():
    """双向链表"""

    def __init__(self):
        self.head = None  # 链表头部的节点
        self.tail = None  # 链表尾部的节点

    def add_double_list(self, new_node: Node):
        """将节点接入双向链表"""
        if isinstance(new_node, Node):
            if self.head is None:
                self.head = new_node
                new_node.previous = None
                new_node.next = None
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.previous = self.tail
                self.tail = new_node
        return

    def print_list_from_head(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def print_list_from_tail(self):
        ptr = self.tail
        while ptr:
            print(ptr.data)
            ptr = ptr.previous


double_link = Double_linked_list()
week = ['Sun', 'Mon', 'Tue', 'Web', 'Thu', 'Fri', 'Sat']
for i in week:
    double_link.add_double_list(Node(i))
print("从头部打印双向链表")
double_link.print_list_from_head()
print("从尾部打印双向链表")
double_link.print_list_from_tail()
