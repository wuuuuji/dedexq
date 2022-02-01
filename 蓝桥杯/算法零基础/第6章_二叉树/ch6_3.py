class Node():
    def __init__(self, data):
        """建立二叉树的节点"""
        self.data = data
        self.left = None
        self.right = None

    def print_root(self):
        print(self.data)


root = Node(20)
root.print_root()
