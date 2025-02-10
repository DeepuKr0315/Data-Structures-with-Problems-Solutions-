# 112. Path Sum
# Problem link = https://leetcode.com/problems/path-sum/description/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    def helper(node, remSum):
        if node is None:
            return False
        if node.val == remSum and node.left is None and node.right is None:
            return True
        return helper(node.left, remSum - node.val) or helper(node.right, remSum - node.val)
    return helper(root, targetSum)