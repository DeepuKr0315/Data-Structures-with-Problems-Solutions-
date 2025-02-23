# problem link = https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
# 129. Sum Root to Leaf Numbers

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root):
    def helper(node, currSum):
        if not node:
            return 0
        if not node.left and not node.right:
            return currSum * 10 + node.val
        return helper(node.left, currSum * 10 + node.val) + helper(node.right, currSum * 10 + node.val)
    return helper(root, 0)