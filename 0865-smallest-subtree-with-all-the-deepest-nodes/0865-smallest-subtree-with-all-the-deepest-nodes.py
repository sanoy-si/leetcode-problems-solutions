# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depths = {}
        def get_depth(node, depth):
            depths[node.val] = depth
            if node.left:
                get_depth(node.left, depth + 1)
            if node.right:
                get_depth(node.right, depth + 1)
        get_depth(root, 0)

        max_depth = max(depths.values())
        def get_subtree(node):
            if depths[node.val] == max_depth:
                return True, node

            left = False, None
            right = False, None
            if node.left:
                left = get_subtree(node.left)
            if node.right:
                right = get_subtree(node.right)
            
            if left[0] and right[0]:
                return True, node
            elif left[0] or right[0]:
                return left if left[0] else right
            
            return False, None
        
        return get_subtree(root)[1]

