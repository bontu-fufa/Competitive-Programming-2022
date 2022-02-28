"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        order = []
        def pre(node):
            if node: 
                order.append(node.val)
                for child in node.children:
                    pre(child)
        pre(root)
        return order