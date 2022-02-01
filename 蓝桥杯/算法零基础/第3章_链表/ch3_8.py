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

    def add_double_list_end(self, new_node):
        """将节点接入双向链表尾部"""
        if isinstance(new_node, Node):  # 判断是不是节点
            if self.head is None:  # 判断链表是否为空
                self.head = new_node  # 链表头等于新节点
                new_node.previous = None
                new_node.next = None
                self.tail = new_node  # 尾节点也是new_node
            else:
                self.tail.next = new_node  # 尾节点指标指向new_node
                new_node.previous = self.tail  # 新节点前方指标指向前
                self.tail = new_node  # 新节点成为尾部节点
        return


    def add_double_list_head(self, new_node):
        """将节点接入双向链表头部"""
        if isinstance(new_node, Node):  # 判断是不是节点n
            if self.head is None:   # 判断链表是否为空
                self.head = new_node    # 链表头等于新节点
                new_node.previous = None
                new_node.next = None
                self.tail = new_node    # 尾节点也是new_node
            else:
                new_node.next = self.head
                self.head.previous = new_node
                self.head = new_node
        return

    def add_double_list_anywhere(self, pos, new_node):
        """将节点接入双向链表任意位置"""
        if isinstance(new_node, Node):  # 判断是不是节点n
            if self.head is None:   # 判断链表是否为空
                self.head = new_node  # 链表头等于新节点
                new_node.previous = None
                new_node.next = None
                self.tail = new_node  # 尾节点也是new_node



    def print_list_from_head(self):
        """从头部打印链表"""
        ptr = self.head  # 指标指向链表第1个节点
        while ptr:
            print(ptr.data)  # 打印节点
            ptr = ptr.next  # 移动指标到下一个节点

    def print_list_from_tail(self):
        """从尾部打印链表"""
        ptr = self.tail
        while ptr:
            print(ptr.data)
            ptr = ptr.previous  # 移动指针到前一个节点


double_link = Double_linked_list()  # 建立链表
n1 = Node(5)  # 第1个节点
n2 = Node(15)  # 第2个节点
n3 = Node(25)  # 第3个节点

for n in [n1, n2, n3]:
    double_link.add_double_list_end(n)
    print("从头部打印双向链表")
    double_link.print_list_from_head()

n4 = Node(30)
double_link.add_double_list_head(n4)
print("从头部打印双向链表")
double_link.print_list_from_head()

print("从尾部打印双向链表")
double_link.print_list_from_tail()
