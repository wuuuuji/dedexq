class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data > self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            if data < self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def postorder(self):
        if self.right:
            self.right.postorder()
        if self.left:
            self.left.postorder()
        print(self.data)


class Delete_Node():
    def deleteNode(self, root: Node, key):
        if root is None:    # 二叉树不存在返回
            return None
        if key < root.data:
            root.left = self.deleteNode(root.left, key)
            return root
        if key > root.data:
            root.right = self.deleteNode(root.right, key)
            return root
        if root.left is None:
            new_root = root.right
            return new_root
        if root.right is None:
            new_root = root.left
            return new_root
        minroot = self.min_node(root.left)
        tmp = Node(minroot.data)
        tmp.left = root.left
        tmp.right = self.right_node(root.right)
        root.left = None
        root.right = None
        return tmp


    def right_node(self, node: Node):
        """找出原删除节点右树"""
        if node.left is None:
            new_root = node.right
            return new_root
        node.left = self.right_node(node.left)
        return node

    def min_node(self, node: Node):
        """找寻最小值节点"""
        while node.left:
            node = node.left
        return node



tree = Node()
datas = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32]
for d in datas:
    tree.insert(d)  # 分别插入数据
tree.postorder()
del_data = 10
print("删除节点"+str(del_data)+"后")
delete_obj = Delete_Node()
result = delete_obj.deleteNode(tree, del_data)
result.postorder()
