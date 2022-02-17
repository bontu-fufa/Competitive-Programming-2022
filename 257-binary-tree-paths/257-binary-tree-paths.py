# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_paths = []
        def paths(node,curr_path):
            if not node: return
            if not node.left and not node.right:
                all_paths.append(curr_path+str(node.val))
                return
            curr_path += str(node.val)+'->'
            paths(node.left, curr_path)
            paths(node.right, curr_path)
            
        paths(root,'')
        return all_paths