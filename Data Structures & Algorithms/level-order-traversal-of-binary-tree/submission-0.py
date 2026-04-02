# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()

        queue.append((root, 0))
        currLevel = 0
        currList = []
        while queue:
            node, level = queue.popleft()

            if node:
                print(f"exploring node: {node.val}")
                if level != currLevel:
                    res.append(currList)
                    currList = []
                
                currLevel = level
                currList.append(node.val)
                
                queue.append((node.left, currLevel + 1))
                queue.append((node.right, currLevel + 1))
        
        if len(currList) != 0:
            res.append(currList)

        return res


