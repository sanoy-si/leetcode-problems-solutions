# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findDepth(root, len):
            if root:
                len += 1
                if not(root.left or root.right):return len
                if root.left and root.right:return max(findDepth(root.left,len),findDepth(root.right,len)) 
                if root.right: return findDepth(root.right,len) 
                if root.left: return findDepth(root.left,len) 
        len=findDepth(root,0)

        return len if len else 0
                
                
        