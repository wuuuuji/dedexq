class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        """建立二叉树"""
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def count(self):
        global num
        if self.left:  # 如果左子节点存在
            self.left.count()  # 递归调用下一层
        if self.left is None and self.right is None:
            num += 1
        if self.right:  # 如果右子节点存在
            self.right.count()  # 递归调用下一层


num = 0
tree = Node()
datas = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]
for d in datas:
    tree.insert(d)  # 分别插入数据
tree.preorder()
tree.count()
print("叶节点数量 = ", num)
