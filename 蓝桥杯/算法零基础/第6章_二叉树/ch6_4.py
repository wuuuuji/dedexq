class Node():
    def __init__(self, data=None):
        """建立二叉树的节点"""
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        """建立二叉树"""
        if self.data:    # 如果根节点存在
            if data < self.data:    # 插入值小于目前节点值
                if self.left:
                    self.left.insert(data)      # 递归调用下一层
                else:
                    self.left = Node(data)      # 建立新节点存放数据
            else:       # 插入值大于目前节点值
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:   # 如果根节点不存在
            self.data = data    # 建立根节点

    def inorder(self):
        """中序打印"""
        if self.left:   # 如果左节点存在
            self.left.inorder()     # 递归调用下一层
        print(self.data)
        if self.right:  # 如果右节点存在
            self.right.inorder()    # 递归调用下一层


tree = Node()
datas = [10, 21, 5, 9, 13, 28]
for d in datas:
    tree.insert(d)      # 分别插入数据
tree.inorder()      # 中序打印
