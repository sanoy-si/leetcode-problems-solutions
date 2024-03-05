# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.levels = defaultdict(lambda: [float('inf'), float('-inf')])

        def dfs(node, depth, column):
            if node:

                self.levels[depth][0] = min(column, self.levels[depth][0])
                self.levels[depth][1] = max(column, self.levels[depth][1])

                dfs(node.left, depth + 1, column + column)
                dfs(node.right, depth + 1, column + column + 1)
        
        dfs(root, 0, 0)

        max_width = 0
        for level in self.levels.values():
            max_width = max(level[1] - level[0] + 1, max_width)
        
        return max_width


