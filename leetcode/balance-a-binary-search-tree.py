# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        in_order = []

        def dfs(node):
            if node:
                dfs(node.left)
                in_order.append(node.val)
                dfs(node.right)
            
        def build_tree(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2

            node = TreeNode(in_order[mid])
            node.left = build_tree(left, mid - 1)
            node.right = build_tree(mid + 1, right)

            return node
        
        dfs(root)

        return build_tree(0, len(in_order) - 1)
