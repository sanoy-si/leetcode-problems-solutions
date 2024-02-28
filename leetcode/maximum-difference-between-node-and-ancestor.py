# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max = float("-inf")
        self.min_stack = []
        self.max_stack = []

        def dfs(node):
            if node:
                if self.min_stack:
                    self.max = max(abs(self.min_stack[-1].val - node.val), self.max)
                    
                if self.max_stack:
                    self.max = max(abs(self.max_stack[-1].val - node.val), self.max)

                if not self.min_stack or node.val > self.min_stack[-1].val:
                    self.min_stack.append(node)

                if not self.max_stack or node.val < self.max_stack[-1].val:
                    self.max_stack.append(node)

                dfs(node.left)
                dfs(node.right)

                if self.min_stack and node == self.min_stack[-1]:
                    self.min_stack.pop()

                if self.max_stack and node == self.max_stack[-1]:
                    self.max_stack.pop()
        dfs(root)

        return self.max
