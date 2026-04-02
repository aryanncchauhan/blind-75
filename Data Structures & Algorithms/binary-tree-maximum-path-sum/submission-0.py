# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
    
        def traverse(node):
            nonlocal res
            if node is None:
                return 0
            left  = max(traverse(node.left), 0)   # ignore negative gains
            right = max(traverse(node.right), 0)
            res = max(res, node.val + left + right) # path through this node
            return node.val + max(left, right)      # best single arm upward
        
        traverse(root)
        return res
            