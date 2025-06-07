
# Implement a binary tree with level-order insertion and verify if it is a valid BST.

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, array):
        if not array:
            return
        i = 0
        # initialize root node if tree is empty
        if self.root is None:
            if array[0] is None:return
            else:
                node = Node(array[0])
                self.root = node
                i += 1
                if i == len(array):return self
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            # insert left child
            if current.left is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.left = node
                i += 1
                if i == len(array):return self
            if current.left:queue.append(current.left)
            # insert right child
            if current.right is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.right = node
                i += 1
                if i == len(array):return self
            if current.right: queue.append(current.right)

# Function to check if a binary tree is a valid BST
def checkValidBST(root):
    return helper(root, float('-inf'), float('inf'))

def helper(node, min_val, max_val):
    if node is None:
        return True
    value = node.val
    if value <= min_val or value >= max_val:
        return False
    isLeftBST = helper(node.left, min_val, value)
    isRightBST = helper(node.right, value, max_val)
    return isLeftBST and isRightBST
