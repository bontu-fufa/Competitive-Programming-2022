# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total = [0]
        def do_difference(root):
            if not root : return 0        

            if not root.left and not root.right: return root.val

            left = do_difference(root.left)
            right = do_difference(root.right)

            # print(left,right)
            
            total[0] += abs(left - right)
            
            return left + right + root.val
        do_difference(root)
        return total[0]