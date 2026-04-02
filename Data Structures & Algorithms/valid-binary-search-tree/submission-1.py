# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        treeList = []

        def getTreeList(root): 
            if root is None:
                return

            getTreeList(root.left)
            treeList.append(root.val)
            getTreeList(root.right)

        getTreeList(root)

        minVal = float("-inf")
        for val in treeList:
            if minVal >= val:
                return False
            minVal = val

        return True