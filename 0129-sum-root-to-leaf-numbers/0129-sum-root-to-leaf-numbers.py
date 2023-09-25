# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def dfs(root,s):
            if not root:
                return
            s = s + str(root.val)
            if not root.left and not root.right:
                self.sum = self.sum + int(s) if s else self.sum
                return
            dfs(root.left,s)
            dfs(root.right,s)
        dfs(root,'')
        return self.sum 
        