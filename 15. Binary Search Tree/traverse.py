# Write a 4 instance methods for binary search tree class to traverse the BST
# Method 1 = traverse the tree breadth first
# Method 2 = traverse the tree depth first(Inorder)
# Method 3 = traverse the tree depth first(Preorder)
# Method 4 = traverse the tree depth first(Postorder)
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def dfs_in_order(self):
        res = []
        if not self.root:
            return res
        def inorder(node):
            if node.left:
                inorder(node.left)
            res.append(node.value)
            if node.right:
                inorder(node.right)
        inorder(self.root)
        return res

    def dfs_pre_order(self):
        res = []
        if not self.root:
            return res
        def preorder(node):
            res.append(node.value)
            if node.left:
                preorder(node.left)
            if node.right:
                preorder(node.right)
        preorder(self.root)
        return res
    def dfs_post_order(self):
        res = []
        if not self.root:
            return res
        def postorder(node):
            if node.left:
                postorder(node.left)
            if node.right:
                postorder(node.right)
            res.append(node.value)
        postorder(self.root)
        return res

bst = BinarySearchTree()
bst.root = Node(10)
bst.root.left = Node(5)
bst.root.right = Node(15)
bst.root.left.left =Node(2)
bst.root.left.right =  Node(7)
bst.root.right.right = Node(20)
print("DFS In-order Traversal: ", bst.dfs_in_order())
print("DFS Pre-order Traversal: ", bst.dfs_pre_order())
print("DFS Post-order Traversal: ", bst.dfs_post_order())