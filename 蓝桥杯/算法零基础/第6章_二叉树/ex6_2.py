class Node():
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            if data > self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def postorder(self):
        """后序打印"""
        if self.left:  # 如果左节点存在
            self.left.postorder()  # 递归调用下一层
        if self.right:  # 如果右节点存在
            self.right.postorder()  # 递归调用下一层
        print(self.data)

    def depth(self):
        current_depth = 0
        if self.left:
            current_depth = max(current_depth, self.left.depth())
        if self.right:
            current_depth = max(current_depth, self.right.depth())
        return current_depth+1


tree = Node()
datas = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]
for d in datas:
    tree.insert(d)  # 分别插入数据
print("所建的二叉树后序打印如下 : ")
tree.postorder()
print("二叉树的深度: " + str(tree.depth()))