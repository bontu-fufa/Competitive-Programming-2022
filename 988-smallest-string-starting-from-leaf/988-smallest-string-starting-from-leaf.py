# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.min_path = "z" * 8500
        def paths(node,curr_path):
            curr_path += chr(node.val + ord('a'))
            
            if not node.left and not node.right:
                self.min_path = min(curr_path[::-1],self.min_path)
                return
            if node.left: paths(node.left, curr_path)
            if node.right: paths(node.right, curr_path)
            
        paths(root,"")
        return self.min_path
      