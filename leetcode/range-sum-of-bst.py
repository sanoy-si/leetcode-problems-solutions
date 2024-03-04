# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        
        def dfs(node, low, high):
            nonlocal total
            if node:
                if low <= node.val <= high:
                    total += node.val
                dfs(node.left, low, high)
                dfs(node.right, low, high)
        
        dfs(root, low, high)

        return total