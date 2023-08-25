# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findDepth(root):
            if not root:return 0
            if not(root.left or root.right):return 1
            return max(findDepth(root.right),  findDepth(root.left)) + 1
        len=findDepth(root)

        return len if len else 0

                
        