class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rob(root):
    def helper(node):
        if node is None:
            return [0, 0]
        leftPair = helper(node.left)
        rightPair = helper(node.right)
        rob_current = node.val + leftPair[1] + rightPair[1]
        skip_current = max(leftPair) + max(rightPair)
        return [rob_current, skip_current]
    return max(helper(root))

# Example usage
root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)
print(rob(root))  # Output: 7