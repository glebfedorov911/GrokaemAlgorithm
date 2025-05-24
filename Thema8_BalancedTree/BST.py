


class Node:


    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

class BST:


    def insert(self, root: Node, key: int):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def inorder(self, root: Node):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

bst = BST()
root = None
for key in [10, 5, 20, 3, 7, 15, 30]:
    root = bst.insert(root, key)

bst.inorder(root)
