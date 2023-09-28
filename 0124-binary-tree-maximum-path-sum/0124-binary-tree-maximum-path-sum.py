# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ma = root.val
        def dfs(root):
            if not root:return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.ma = max(self.ma, root.val + max(left,0) + max(right,0))
            return root.val + max(0,left,right)
        left = dfs(root.left)
        right = dfs(root.right)
        self.ma = max(self.ma,root.val + max(left,0) + max(right,0))
            
        return self.ma

