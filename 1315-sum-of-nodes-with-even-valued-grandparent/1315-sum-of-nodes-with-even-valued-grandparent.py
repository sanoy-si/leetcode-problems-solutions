# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.s = 0
        def dfs(parent,gparent,root):
            if root == None:return 
            if gparent and gparent.val %2 == 0:self.s += root.val
            dfs(root,parent,root.left)
            dfs(root,parent,root.right)
        dfs(None,None,root)
        return self.s

        