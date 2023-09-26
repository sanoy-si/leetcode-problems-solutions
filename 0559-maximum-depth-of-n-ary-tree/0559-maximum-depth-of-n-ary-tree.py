"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.ma = 0
        def dfs(root,val):
            if root:
                val += 1
                self.ma = max(self.ma,val)
                for child in root.children:
                    dfs(child,val)
        dfs(root,0)
        return self.ma
                
        