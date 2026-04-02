# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        res = False

        while stack:
            node = stack.pop()

            if node:
                if node.val == subRoot.val and self.checkSubtree(node, subRoot):
                    res = True
                stack.append(node.left)
                stack.append(node.right)

        return res
    
    def checkSubtree(self, root, subRoot):
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return self.checkSubtree(root.left, subRoot.left) and self.checkSubtree(root.right, subRoot.right)

        return False