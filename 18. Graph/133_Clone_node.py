# problem link = https://leetcode.com/problems/clone-graph/description/?envType=problem-list-v2&envId=graph
# CLONE NODE

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(self, node):
    """
    :type node: Node
    :rtype: Node
    """
    oldToNew = {}
    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]
        copy = Node(node.val)
        oldToNew[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy
    return dfs(node) if node else None