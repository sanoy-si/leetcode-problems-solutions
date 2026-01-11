# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        rob = defaultdict(int)
        skip = defaultdict(int)
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            dfs(node.right)
            rob[node] = skip[node.left] + skip[node.right] + node.val
            skip[node] = max(skip[node.left], rob[node.left]) + max(skip[node.right], rob[node.right])
            
        dfs(root)
        return max(rob[root], skip[root])

            
