from collections import deque
 
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
class BinaryTree:
    def __init__(self):
        self.root = None
 
    def insert(self, array):
        if len(array) == 0:
            return
        
        i = 0
 
        # If root is null
        if self.root is None:
            if array[0] is None:
                return
            else:
                node = Node(array[0])
                self.root = node
                i += 1
                if i == len(array):
                    return self
        
        # Insert elements
        queue = [self.root]
        while queue:
            current = queue.pop(0)
 
            # Process left child
            if current.left is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.left = node
                i += 1
                if i == len(array):
                    return self
            if current.left is not None:
                queue.append(current.left)
 
            # Process right child
            if current.right is None:
                if array[i] is not None:
                    node = Node(array[i])
                    current.right = node
                i += 1
                if i == len(array):
                    return self
            if current.right is not None:
                queue.append(current.right)
 
def level_order_traversal(root):
    if root is None:  # This operation is O(1)
        return []
    output = []
    queue = deque([root])  # Creating a queue is O(1)
    while queue:  # The outer while loop will run for n iterations (n is the total number of nodes in the tree)
        length = len(queue)  # Getting the length of the queue is O(1)
        count = 0
        curr_level_values = []
        while count < length:  # This inner while loop will run for 'length' iterations
            curr = queue.popleft()  # Removing an element from the deque is O(1)
            curr_level_values.append(curr.value)  # Appending an element is O(1)
            if curr.left: 
                queue.append(curr.left)  # Appending an element to deque is O(1)
            if curr.right: 
                queue.append(curr.right)  # Appending an element to deque is O(1)
            count += 1
        output.append(curr_level_values)  # Appending a list of length 'length' is O(length)
 
    return output        
 
# Create a binary tree and insert elements
tree = BinaryTree()
tree.insert([7, 11, 1, None, 7, 2, 8, None, None, None, 3, None, None, 5, None])