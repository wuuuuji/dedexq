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

    def between(self, pre_node, newdata):
        """在链表中间插入新节点"""
        if pre_node is None:            # 判断是否为空链表
            print("缺插入节点的前一个节点")
            return
        # 建立和插入新节点
        new_node = Node(newdata)        # 建立新节点
        new_node.next = pre_node.next   # 新节点指向前一节点的下一节点
        pre_node.next = new_node        # 前一个节点指向新建节点

    def rm_node(self, rmkey):
        """删除节点"""
        ptr = self.head                 # 临时指针
        if ptr:
            if ptr.data == rmkey:
                self.head = ptr.next    # 将第一个指标指向下一个
                return
        while ptr:
            if ptr.data == rmkey:
                break
            prev = ptr                  # 设定前一节点指标
            ptr = ptr.next              # 移动指标
        if ptr is None:                 # 如果ptr已经是末端
            return                      # 找不到所以返回
        prev.next = ptr.next            # 找到了所以将前一节点指向下一个节点

link = Linked_list()
link.ending(5)      # 节点1
link.ending(15)     # 节点2
link.ending(25)     # 节点3
link.print_list()   # 打印链表link
print("新的链表")
link.rm_node(15)
link.print_list()       # 打印新链表link
