class Node():
    """节点"""

    def __init__(self, data=None):
        self.data = data  # 数值
        self.next = None  # 指标


class linked_list():
    """链表"""

    def __init__(self):
        self.head = None  # 链表第一个节点

    def print_list(self):
        """打印列表"""

        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def ending(self, newdata: int):
        """从尾部加入链表"""

        new_code = Node(newdata)
        if self.head is None:
            self.head = new_code
            return
        last_ptr = self.head
        while last_ptr.next:
            last_ptr = last_ptr.next
        last_ptr.next = new_code

    def find_data(self, find_int: int) -> int:
        counts = 0
        ptr = self.head
        while ptr:
            if find_int == ptr.data:
                counts += 1
            ptr = ptr.next
        return counts


link = linked_list()
input_node = [5, 15, 5]
for i in input_node:
    link.ending(i)
print("所建的链表")
link.print_list()

find_node = [5, 15, 20]
print("分别列出数值", end='')
for i in find_node:
    print("{} ".format(i), end='')
print("的出现次数")
for i in find_node:
    print("{0}  出现 {1} 次".format(i, link.find_data(i)))