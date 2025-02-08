# 94. Binary Tree Inorder Traversal
# Problem link = https://leetcode.com/problems/binary-tree-inorder-traversal/description/

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def inorderTraversal(root):
    res = []
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.right.left = TreeNode(9)

# Call inorder traversal
print("Inorder Traversal:", inorderTraversal(root))