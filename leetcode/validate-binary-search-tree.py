# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.list = []
        
        def dfs(node):
            if not node:
                return 

            dfs(node.left)

            self.list.append(node.val)
            
            dfs(node.right)
        
        dfs(root)

        return len(self.list) == len(set(self.list)) and sorted(self.list) == self.list 
