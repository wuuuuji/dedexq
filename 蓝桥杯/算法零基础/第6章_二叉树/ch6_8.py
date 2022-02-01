class Node():
    def __init__(self, data=None):
        """建立二叉树的节点"""
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        """建立二叉树"""
        if self.data:  # 如果根节点存在
            if data < self.data:  # 插入值小于目前节点值
                if self.left:
                    self.left.insert(data)  # 递归调用下一层
                else:
                    self.left = Node(data)  # 建立新节点存放数据
            else:  # 插入值大于目前节点值
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:  # 如果根节点不存在
            self.data = data  # 建立根节点

    def inorder(self):
        """中序打印"""
        if self.left:  # 如果左节点存在
            self.left.inorder()  # 递归调用下一层
        print(self.data)
        if self.right:  # 如果右节点存在
            self.right.inorder()  # 递归调用下一层

    def preorder(self):
        """前序打印"""
        print(self.data)
        if self.left:  # 如果左节点存在
            self.left.preorder()  # 递归调用下一层
        if self.right:  # 如果右节点存在
            self.right.preorder()  # 递归调用下一层

    def postorder(self):
        """后序打印"""
        if self.left:  # 如果左节点存在
            self.left.preorder()  # 递归调用下一层
        if self.right:  # 如果右节点存在
            self.right.preorder()  # 递归调用下一层
        print(self.data)

    def search(self, val):
        """搜寻特定值"""
        if val < self.data:  # 如果搜寻值小于目前节点值
            if not self.left:  # 如果左子树不存在
                return str(val) + " 不存在 "
            return self.left.search(val)  # 递归继续往左子树进行寻找
        elif val > self.data:  # 如果搜寻值大于目前节点值
            if not self.right:  # 如果右子树不存在
                return str(val) + " 不存在 "
            return self.right.search(val)  # 递归继续往右子树进行寻找
        else:
            return str(val) + ' 找到了 '


class Delete_Node():
    def deleteNode(self, root: Node, key):
        if root is None:    # 二叉树不存在返回
            return None
        if key < root.data:     # 删除值小于root值则往左
            root.left = self.deleteNode(root.left, key)
            return root
        if key > root.data:     # 删除值大于root值则往右
            root.right = self.deleteNode(root.right, key)
            return root
        if root.left is None:   # 左边节点不存在
            new_root = root.right
            return new_root
        if root.right is None:  # 右边节点不存在
            new_root = root.left
            return new_root
        succ = self.max_node(root.left)     # 找出左子树中最大值的节点
        tmp = Node(succ.data)   # 用次最大值建立节点
        tmp.left = self.left_node(root.left)    # 串接节点的左子树
        tmp.right = root.right  # 节点串接原删除节点的右子树
        return tmp

    def left_node(self, node: Node):
        """找出原删除节点左子树"""
        if node.right is None:  # 右节点不存在
            new_root = node.left    # 使用左节点
            return new_root
        node.right = self.left_node(node.right)     # 进入下一层
        return node

    def max_node(self, node: Node):
        """找寻最大值节点"""
        while node.right:       # 如果是否则node是最大值节点
            node = node.right
        return node


tree = Node()
datas = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]
for d in datas:
    tree.insert(d)  # 分别插入数据
tree.inorder()  # 中序打印
del_data = 5
print("删除节点后")
delete_obj = Delete_Node()      # 建立删除节点对象
result = delete_obj.deleteNode(tree, del_data)      # 删除操作
result.inorder()  # 中序打印
